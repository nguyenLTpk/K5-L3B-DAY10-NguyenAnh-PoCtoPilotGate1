"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 1 (Pháp lý & Chính sách): Ghim phiên bản chính sách có hiệu lực pháp lý tại ctx.as_of
    policies = ctx.tools.lookup_policies()
    pol = H.effective_policy(policies, ctx.as_of)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    if tool == "issue_refund":
        # Cổng 2A (Kinh doanh): Kiểm tra trần hoàn tiền tự động trong ngày
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        spent = ctx.tools.auto_refund_today_vnd()
        if cap is not None and not action.get("approval_id") and spent + action.get("amount_vnd", 0) > cap:
            return Verdict.escalate("Vượt trần ngân sách hoàn tiền tự động trong ngày")

        # Cổng 2B (Kinh doanh): Trần hoàn tiền cho một khách hàng trong ngày
        cust_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd", 300000)
        if action.get("amount_vnd", 0) > cust_cap:
            return Verdict.escalate("Vượt hạn mức hoàn tiền tự động cho một khách")

        # Cổng 2C (Kỹ thuật/An toàn): Kiểm tra tính hợp lệ của khoản bồi hoàn theo thực tế tracking DB
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order:
            pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            real_delay = H.db_delay_days(parcel, ctx.as_of)
            real_entitlement = H.entitlement_vnd(pol, order, real_delay, parcel.get("delay_cause"))

            if action.get("amount_vnd", 0) > real_entitlement:
                if real_entitlement == 0:
                    return Verdict.deny(f"Không đủ điều kiện hoàn: trễ thực tế {real_delay} ngày < {pol['late']['min_days_fee']} ngày quy định")
                return Verdict.modify(f"Chỉnh lại mức hoàn theo thực tế tracking DB ({real_entitlement}đ)", amount_vnd=real_entitlement)

    elif tool == "file_carrier_fault":
        # Cổng 3 (Đối tác & Pháp lý): Kiểm tra tính xác thực trước khi quy lỗi và phạt hãng vận chuyển
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order:
            pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            real_delay = H.db_delay_days(parcel, ctx.as_of)

            # Hãng chỉ chịu lỗi khi thực tế trễ thuộc phạm vi lỗi của hãng và đủ số ngày trễ quy định
            if not H.carrier_at_fault(pol, parcel, real_delay):
                return Verdict.deny("Hãng không có lỗi hoặc chưa đủ số ngày trễ quy định theo chính sách")

            # Đảm bảo gán đúng hãng vận chuyển phụ trách kiện hàng đó
            if parcel.get("carrier_id") != action.get("carrier_id"):
                return Verdict.deny("Gán sai hãng vận chuyển chịu trách nhiệm")

            # Kiểm tra yêu cầu phải có nguyên nhân chậm trễ được ghi nhận chính thức
            require_cause = (ctx.gates or {}).get("legal", {}).get("carrier_fault_requires_recorded_cause")
            if require_cause and not parcel.get("delay_cause"):
                return Verdict.deny("Chưa có nguyên nhân chậm trễ được ghi nhận trong hệ thống")

    elif tool == "notify_carrier":
        # Cổng 4 (Bảo mật PII): Không gửi thông tin cá nhân khách hàng (tên, SĐT, địa chỉ) cho hãng vận chuyển
        payload = action.get("payload", {})
        blocked_fields = (ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or []
        if "recipient_contact" in payload and any(f in ("name", "phone") for f in blocked_fields):
            clean_payload = {k: v for k, v in payload.items() if k != "recipient_contact"}
            return Verdict.modify("Bảo mật PII: loại bỏ thông tin liên hệ người nhận gửi cho bên thứ ba", payload=clean_payload)

    return Verdict.allow()
