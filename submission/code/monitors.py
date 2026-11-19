"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def llm_fallback_rate(trials):
    """Tỉ lệ ticket gặp sự cố gián đoạn LLM (429/timeout) và phải kích hoạt fallback.
    Sáng đèn khi nhà cung cấp LLM bị nghẽn (đặc biệt trong đêm cao điểm sale S4).
    """
    count = sum(1 for t in trials if any(e.get("type") == "llm_fallback" for e in t.get("events", [])))
    return round(count / max(1, len(trials)), 4)


def peak_hour_density(trials):
    """Tỉ lệ ticket dồn vào khung giờ cao điểm (phút 240..480 của ca trực).
    Theo dõi sự biến động lưu lượng để kịp thời điều phối tăng cường nhân sự trực hàng chờ.
    """
    count = sum(1 for t in trials if (t.get("arrive_min") or 0) >= 240)
    return round(count / max(1, len(trials)), 4)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "llm_fallback_rate": llm_fallback_rate, # Metric mới 1: Tỉ lệ lỗi fallback LLM
    "peak_hour_density": peak_hour_density, # Metric mới 2: Mật độ tải giờ cao điểm
}
STARTER_MONITORS = ("escalation_rate",)
