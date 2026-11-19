# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3B-DAY10-NguyenAnh-PoCtoPilotGate1 · **Thẻ đã bốc:** S4 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | R-S4-prepared-20261119-184732-59936a | S4 · prepared | Nhận thẻ đã bốc S4, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 1.0 ([1.0, 1.0]) | 1.0 | 0đ · 0 lỗi · 0 ca | 0.3902 | Cổng vòng 1 chặn triệt để lỗi ghi oan hãng và hoàn sai, nhưng vượt trần hàng chờ và trần ngân sách ngày 11.11. |
| 2 | R-S4-after-20261119-184732-59936a | S4 · after | Tăng reviewer lên 2, capacity 12 ca/h, đặt trần hoàn ngày 300k, thêm monitors | 1.0 ([1.0, 1.0]) | 1.0 | 0đ · 0 lỗi · 0 ca | 0.5122 | Xóa bỏ hoàn toàn ùn tắc hàng chờ (0 ca stuck, chờ tối đa 13 phút), kiểm soát trần hoàn ngày 292k <= 300k. |
| 3 | R-base-after-20261119-184732-59936a | base · after | Kiểm tra tính tương thích ngược (regression) trên bộ nền | 1.0 ([1.0, 1.0]) | 1.0 | 0đ · 0 lỗi · 0 ca | 0.2273 | Bộ nền duy trì pass_rate 100%, không bị ảnh hưởng tiêu cực bởi cấu hình mới. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident S4
```

- Mã lần chạy grade: `R-S4-grade-20261119-184731-59936a` · base: `R-S4-before-20261119-184732-59936a` · prepared: `R-S4-prepared-20261119-184732-59936a`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): Cổng vòng 1 (`write_gate`) đã đỡ triệt để 27 lỗi ghi phạt oan cho hãng vận chuyển (giảm từ 27 xuống 0 lỗi) và 160.000đ tiền hoàn sai (giảm từ 160.000đ xuống 0đ), nâng pass_rate từ 0.8683 lên 1.0 và pass_k từ 0.6829 lên 1.0.
- Khối kinh doanh và vận hành còn dòng nào vượt trần:
  1. Hàng chờ: 5 ca bị ùn (chờ quá 60 phút hoặc hết ca chưa tới lượt).
  2. Thời gian chờ lâu nhất: 82.0 phút > mức trần 60 phút.
  3. Tổng hoàn tự động một ngày: 422.000đ > ngân sách Finance cho ngày sale 11.11 (300.000đ).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Thuộc 2 lăng kính chính: **Con người & Vận hành** (ca trực CSKH chỉ có 1 nhân sự không đủ công suất tiếp nhận lượng ticket dồn giờ cao điểm) và **Kinh doanh** (ngân sách bồi hoàn tự động ngày sale bị vượt trần riêng 300.000đ).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? Có nằm trong dự liệu một phần: Nhóm đã dự báo rủi ro giờ cao điểm ở Phiếu B mục B7.6, nhưng chưa gắn cổng giới hạn trần ngân sách riêng theo ngày siêu sale và chưa kích hoạt ca trực 2 người tự động. Cổng vòng 1 đã đỡ được toàn bộ lỗi kỹ thuật (phạt oan hãng, hoàn sai tiền) nhưng để hở giới hạn vận hành con người và trần ngân sách ngày 11.11.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Ca trực đêm siêu sale chỉ bố trí 1 người trực (công suất tối đa 6 ca/h), trong khi lượng ticket dồn vào khung 20h–22h lên đến 14–20 ticket khiến hàng chờ bị nghẽn tới 82 phút. | Con người & Vận hành | `incidents/S4/world_patch.json` (arrive_min), `lab10/ops.py` (attach_queue), report dòng queue stuck. |
| Ngân sách hoàn tự động ngày 11.11 bị siết xuống 300.000đ nhưng config hệ thống vẫn giữ trần 2.000.000đ ngày thường khiến tài chính thất thoát quá mức cho phép. | Kinh doanh | `incidents/S4/world_patch.json` (ops_limits.daily_auto_refund_budget_vnd), `config/operating_gates.json`. |
| Nhà cung cấp LLM bị nghẽn (mã lỗi 429 Too Many Requests), hệ thống kích hoạt cơ chế fail_open tự động đề xuất hoàn tiền và phạt hãng mà thiếu kiểm soát. | Kỹ thuật & Hạ tầng | Trace ticket `S4-08@11`, các sự kiện `llm_error` và `llm_fallback` trong log trace. |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai: Hãng vận chuyển (bị phạt oan), Finance (vượt ngân sách hoàn), Đội ngũ CSKH (ngập hàng chờ) · đo bằng gì: Số lỗi phạt oan, Tiền hoàn sai, Số ca kẹt queue > 60 phút · bao nhiêu ở mốc base: 27 lỗi oan, 160.000đ hoàn sai (tổng hoàn 466.000đ), 4 ca kẹt queue (chờ lâu nhất 78 phút)

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S4-08@11`: Trace dòng `04 llm_error: 429 Too Many Requests` → dòng `06 llm_fallback: mode fail_open` → dòng `09 tool file_carrier_fault (delay_days: 4)`. Hàng trễ do shop xuất kho muộn (`cause: MERCHANT_HANDOVER`) nhưng khi LLM lỗi thì hệ thống tự động bồi hoàn và phạt hãng VNX. | Hãng vận chuyển VNX bị phạt oan và trừ tiền đối soát | Cao | Lỗi chìm (hệ thống fail-open ngầm quy lỗi hãng khi LLM gặp sự cố) |
| 2 | `S4-07@11`: Trace dòng `01 llm_extract: intent DAMAGED` → dòng `02 result: status escalated`. Hàng vỡ hỏng trợ lý không xử lý được nên dồn hết sang người duyệt. Dồn cùng lúc 14–20 ticket vào giờ cao điểm khiến ca trực 1 người bị ngập. | Trưởng ca CSKH (chị Hạnh) quá tải, khách hàng chờ quá 60 phút | Cao | Giới hạn của hệ thống (giới hạn công suất con người trước lưu lượng tăng đột biến) |
| 3 | `S4-41@11`: Tổng số tiền hoàn tự động trong ngày tích lũy đạt 466.000đ (ở base) và 422.000đ (ở prepared), vượt trần 300.000đ của Finance. | Bộ phận Finance (chị Oanh) chịu thâm hụt ngân sách chiến dịch | Cao | Ngữ cảnh (chính sách ngân sách thay đổi riêng cho ngày 11.11 nhưng hệ thống áp trần ngày thường) |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 (S4-08@11) | Lỗi 2 (S4-07@11) | Lỗi 3 (S4-41@11) |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Có (khách bảo do shop trễ nhưng LLM fallback coi như lỗi hãng) | Không | Không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | Không (DB có ghi rõ MERCHANT_HANDOVER nhưng cơ chế fallback bỏ qua) | Không | Không |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | Không | Có (trợ lý và người duyệt cùng chia sẻ hàng chờ nhưng năng lực tiếp nhận không cân xứng) | Không |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Có (LLM 429 liên tiếp $\rightarrow$ kích hoạt fallback fail_open thiếu an toàn) | Không | Không |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng bị ghi lỗi và trừ tiền phạt đối soát trong khi đơn hàng chậm trễ hoàn toàn do shop chuẩn bị hàng trễ. | Khách hàng phải chờ hơn 82 phút mới được phản hồi, vi phạm cam kết SLA 60 phút của dịch vụ CSKH. | Kế toán đối soát phát hiện chi phí bồi hoàn vượt quá trần ngân sách cho phép của ban giám đốc cho sự kiện 11.11. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Đặt cổng kiểm soát bắt buộc (`write_gate`): Chặn `file_carrier_fault` nếu `delay_cause != 'CARRIER'`. | Vận hành & Con người: Tăng số lượng nhân viên trực ca đêm sale từ 1 lên 2 người, nâng công suất lên 12 ca/h. | Cổng kinh doanh (`operating_gates.json`): Cập nhật `daily_refund_cap_vnd: 300000`, chạm trần tự chuyển người duyệt. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Lệnh ghi lỗi hãng bị chặn $\rightarrow$ chuyển ticket cho nhân viên duyệt kèm trích dẫn nguyên nhân từ shop $\rightarrow$ khách được hoàn từ nguồn hợp lý. | Hàng chờ duy trì $\le$ 3 ca $\rightarrow$ nhân viên xử lý ngay trong vòng 6–13 phút $\rightarrow$ giải tỏa 100% ca ùn tắc. | Trợ lý hoàn tự động tới 292.000đ $\rightarrow$ ticket tiếp theo tự động escalate sang nhân viên duyệt có mã phê duyệt. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | Theo dõi tỉ lệ lỗi fallback: metric `llm_fallback_rate`. | Theo dõi mật độ dồn ticket giờ cao điểm: metric `peak_hour_density`. | Theo dõi tốc độ tiêu hao ngân sách bồi hoàn trong ngày. |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund`, `file_carrier_fault`, phân ca duyệt hàng chờ

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `reviewers_on_shift` (số người trực) | INCAPABLE | Đêm 11.11 ticket dồn 14–20 ca/h, 1 nhân sự trực chỉ xử lý được 6 ca/h (`NV-HANH`) | Hàng chờ ngập, 5 ca chờ > 82 phút, vi phạm SLA 60 phút, khách hàng bức xúc | Không có cổng nào ngăn tình trạng nghẽn queue vật lý | Cổng vận hành (tầng Vận hành): Tăng ca trực lên 2 người (`reviewers_on_shift: 2`), nâng công suất lên 12 ca/h, bổ sung alert gọi người khi queue > 5 ca. |
| `daily_refund_cap_vnd` | MORE | Tổng tiền bồi hoàn tích lũy đạt 422.000đ trong ngày 11.11, vượt mức 300.000đ ngân sách chiến dịch | Thất thoát tài chính, kế toán đối soát (chị Oanh) từ chối duyệt ngân sách vượt trần | Trần cũ trong config là 2.000.000đ (dành cho ngày thường) | Cổng kinh doanh (tầng Giới hạn thiệt hại): Đặt `daily_refund_cap_vnd: 300000`, `write_gate` tự động escalate sang người duyệt khi chạm trần. |
| `delay_cause` trong `file_carrier_fault` | WRONG | Ticket `S4-08@11`, tracking ghi `cause: MERCHANT_HANDOVER` (shop trễ) nhưng LLM 429 fallback sang fail_open tự đề xuất phạt hãng VNX | Hãng VNX bị quy lỗi oan, phát sinh tranh chấp hợp đồng đối soát | Cổng vòng 1 đã có kiểm tra cơ bản nhưng cơ chế fail_open ngầm ghi đè | Cổng code (tầng Chặn): Trong `write_gate`, bắt buộc kiểm tra `delay_cause == 'CARRIER'` và `carrier_fault_requires_recorded_cause: true`, deny ngay nếu nguyên nhân do shop. |
| `llm_error` / `llm_fallback` | PERTURBED | LLM provider quá tải trả về 429 Too Many Requests liên tục trong khung giờ cao điểm đêm sale | Agent mất khả năng suy luận logic chính sách, rơi vào trạng thái đề xuất bừa bãi | Không có cơ chế circuit breaker hoặc rate-limit ở tầng agent | Cổng theo dõi (tầng Phát hiện): Metric `llm_fallback_rate` trong `monitors.py` cảnh báo khi tỉ lệ lỗi LLM vượt quá 10% để chuyển sang chế độ an toàn. |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report:
1. Vận hành: Hàng chờ xử lý thủ công không được có ca nào chờ vượt quá thời gian cam kết SLA (`queue_wait_max_min <= 60` và `queue_stuck == 0`).
2. Kinh doanh: Tổng tiền hoàn tiền tự động trong ngày không được vượt quá ngân sách chiến dịch được Finance phê duyệt (`total_auto_refund_vnd <= 300.000đ`).

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào):
- Kiểm bằng số trong report: Dòng `số ca bị ùn` (`queue_stuck`) và `chờ lâu nhất (phút)` trong khối Kinh doanh & Vận hành của report `lab10.eval` / `lab10.grade`.
- Kiểm bằng code: Nhánh kiểm tra ngân sách tích lũy trong ngày `spent + amount_vnd > cap` tại hàm `write_gate` trong `lab10/guards.py`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm):
Người thiết kế ngầm giả định rằng: "Dịch vụ API của nhà cung cấp mô hình LLM luôn sẵn sàng 100% với độ trễ thấp và không bao giờ bị nghẽn (rate limit 429), đồng thời lưu lượng yêu cầu của khách hàng phân bổ đều theo thời gian để 1 nhân viên CSKH luôn có thể xử lý kịp các ca chuyển duyệt."

Vì sao có thể sai:
1. Vào các ngày siêu sale (11.11, Black Friday), lưu lượng người dùng mua sắm và khiếu nại tăng vọt gấp 3–5 lần và tập trung dồn vào các khung giờ vàng (20h–22h), dẫn đến nghẽn cục bộ.
2. Bản thân các nhà cung cấp nền tảng AI (như OpenAI, Google, Anthropic) cũng thường xuyên bị quá tải lưu lượng trong các sự kiện mua sắm lớn toàn cầu, dẫn đến lỗi 429 hoặc timeout hàng loạt. Khi đó, nếu hệ thống dựa vào cơ chế fail-open ngây thơ thì sẽ gây thiệt hại tài chính và uy tín nghiêm trọng.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S4-before-20261119-184732-59936a`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: Vỡ trận vận hành & tài chính đêm sale 11.11 (cho ai: CSKH, Khách hàng, Hãng vận chuyển, Finance; đo bằng: 5 ca tắc hàng chờ > 82 phút, 27 lỗi phạt oan hãng, 466.000đ hoàn tiền vượt trần)
 └─ HOẶC
 ├─ [1] Hàng chờ CSKH bị tắc nghẽn, thời gian chờ vượt SLA 60 phút
 │   └─ vì: Ticket dồn gấp 3 vào khung 20h–22h trong khi chỉ bố trí 1 người trực (công suất 6 ca/h), hàng vỡ hỏng dồn sang người duyệt ── tầng: con người & vận hành (bằng chứng: ticket S4-07@11, report hàng chờ 5 ca kẹt)
 ├─ [2] Hãng vận chuyển VNX bị ghi lỗi oan và phạt tiền sai
 │   └─ vì: LLM gặp lỗi 429 liên tiếp, kích hoạt fallback fail_open tự đề xuất phạt dù đơn trễ do shop xuất kho muộn ── tầng: kỹ thuật & hạ tầng (bằng chứng: ticket S4-08@11, dòng llm_error và llm_fallback)
 └─ [3] Tổng ngân sách bồi hoàn tự động trong ngày vượt trần Finance cho phép
     └─ vì: Config hệ thống chưa cập nhật trần riêng 300.000đ cho ngày sale 11.11, vẫn giữ mức 2.000.000đ ngày thường ── tầng: kinh doanh (bằng chứng: tổng hoàn ngày 466.000đ ở base, ops_limits trong world_patch)
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Năng lực phục vụ hàng chờ phải đáp ứng lưu lượng tải đỉnh cao, không để ca nào chờ quá 60 phút SLA. | Giả định lượng ticket rải đều trong ca và 1 người trực là đủ cho mọi tình huống. |
| [2] | Không được ghi lỗi phạt đối tác vận chuyển khi nguyên nhân chậm trễ không do đối tác gây ra. | Giả định dịch vụ LLM bên thứ ba luôn phản hồi 200 OK và không bao giờ nghẽn 429. |
| [3] | Tổng tiền bồi hoàn tự động một ngày không được vượt ngân sách chiến dịch quy định trong ngày. | Giả định ngân sách bồi hoàn ngày lễ/sale cũng giống như các ngày bình thường trong năm. |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Thiếu nhân lực trực ca đêm sale dẫn đến vỡ SLA hàng chờ | `config/operating_gates.json` $\rightarrow$ `operations.reviewers_on_shift: 2`, `operations.review_capacity_per_hour: 12` | Tầng Vận hành | **NGĂN hẳn**: Tăng gấp đôi công suất tiếp nhận từ 6 lên 12 ca/h, đưa thời gian chờ tối đa từ 82 phút xuống 13 phút (0 ca kẹt). | `R-S4-after-20261119-184732-59936a` |
| [2] | LLM fallback fail_open tự đề xuất phạt oan hãng khi đơn trễ do shop | `lab10/guards.py` $\rightarrow$ nhánh `file_carrier_fault` trong `write_gate` kiểm tra đối soát tracking DB | Tầng Chặn | **NGĂN hẳn**: `write_gate` chạy độc lập ngoài model, chặn đứng mọi lệnh ghi lỗi khi `delay_cause != 'CARRIER'` hoặc thiếu căn cứ. | `R-S4-after-20261119-184732-59936a` |
| [3] | Ngân sách bồi hoàn ngày 11.11 vượt trần Finance | `config/operating_gates.json` $\rightarrow$ `business.daily_refund_cap_vnd: 300000` | Tầng Giới hạn thiệt hại | **NGĂN hẳn**: `write_gate` theo dõi sổ cái thời gian thực, tự động escalate sang người duyệt khi chạm mốc 300.000đ (thực tế dừng ở 292.000đ). | `R-S4-after-20261119-184732-59936a` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `llm_fallback_rate` (kèm thêm `peak_hour_density`) |
| **Bước / hành vi được đo** | Đo lường tần suất hệ thống agent gặp lỗi kết nối LLM (429/timeout) và phải kích hoạt cơ chế fallback |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ số ticket phải kích hoạt chế độ fallback trên tổng số ticket tiếp nhận trong ngày (đơn vị: tỉ lệ từ 0.0 đến 1.0) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | Đọc mảng sự kiện `t["events"]` của từng trial trong ngày, kiểm tra sự hiện diện của sự kiện có `type == "llm_fallback"` |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `count(t for t in trials if has_fallback(t)) / max(1, len(trials))`. Làm tròn 4 chữ số thập phân; nếu trials rỗng trả về 0.0. |
| **Khung thời gian / ngưỡng báo động** | Tính theo từng ca trực (rolling 1 giờ); cảnh báo đỏ tới `#ops-alerts-pilot` khi chỉ số vượt ngưỡng 0.05 (5%). |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không đo được chất lượng nội dung tin nhắn fallback gửi cho khách hàng, không đo được độ trễ mạng từng request API. |
| **Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report)** | Bộ nền: `0.0` (0%) · Trên thẻ sự cố S4: `0.1854` (18.54%) → Sáng đèn cảnh báo rõ rệt khi có sự cố nghẽn LLM! |

---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S4-after-20261119-184732-59936a`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Tác hại: Vỡ trận vận hành & tài chính đêm sale 11.11 (đã được dập tắt)
 └─ HOẶC
 ├─ [1] Hàng chờ CSKH bị tắc nghẽn VÀ [Gate phân ca 2 người trực hỏng / Nhân viên vắng mặt]
 ├─ [2] Hãng vận chuyển bị phạt oan VÀ [Cổng write_gate kiểm tra delay_cause trong tracking DB bị hỏng]
 └─ [3] Ngân sách bồi hoàn vượt trần VÀ [Cổng write_gate kiểm tra daily_refund_cap_vnd bị hỏng]
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `operations.reviewers_on_shift: 2`, `operations.review_capacity_per_hour: 12`, monitor `peak_hour_density` | Tầng Vận hành | Ngăn: Đảm bảo công suất xử lý đạt 12 ca/h, lớn hơn tốc độ dồn ticket đỉnh điểm. | Còn hở nếu cả 2 nhân viên cùng gặp sự cố đột xuất hoặc mất điện/mất mạng internet tại văn phòng CSKH. |
| [2] | `write_gate` nhánh `file_carrier_fault`, cấu hình `carrier_fault_requires_recorded_cause: true`, monitor `llm_fallback_rate` | Tầng Chặn | Ngăn: Lệnh ghi bị từ chối triệt để nếu tracking DB không ghi nhận `CARRIER`. | Còn hở nếu dữ liệu trong chính bảng tracking DB bị nhân viên nhập sai nguyên nhân thành CARRIER. |
| [3] | `write_gate` nhánh `issue_refund`, cấu hình `business.daily_refund_cap_vnd: 300000` | Tầng Giới hạn thiệt hại | Ngăn: Đảm bảo tổng hoàn tự động dừng lại trước 300.000đ (thực tế đạt 292.000đ), phần vượt đẩy sang người duyệt. | Còn hở nếu nhân viên duyệt tay lơ là phê duyệt bừa bãi các ca vượt trần mà không kiểm tra ngân sách. |

---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Hàng chờ duyệt CSKH bị tắc nghẽn nghiêm trọng vào khung giờ sale cao điểm khiến SLA vượt quá 60 phút | Cao | Nghiêm trọng | Nguyễn Minh Đức (`2A202603960`) | `peak_hour_density > 0.40` hoặc hàng chờ tích lũy > 5 ca chưa duyệt | Kích hoạt nhân sự trực dự phòng thứ 2 (`reviewers_on_shift: 2`), tăng công suất lên 12 ca/h | Đạt chỉ số queue_stuck = 0 và wait_max <= 60 | MANAGE |
| Nhà cung cấp LLM nghẽn mạng (429/timeout) kích hoạt cơ chế fail_open đề xuất sai lệch | Cao | Cao | Lê Thành Nguyên (`2A202603733`) | `llm_fallback_rate > 0.05` (5%) | Cổng `write_gate` chặn độc lập dựa trên tracking DB; chuyển các ca nghi ngờ sang người duyệt | Giữ nguyên pass_rate 100%, 0 lỗi oan hãng | MEASURE |
| Tổng tiền hoàn tự động vượt quá trần ngân sách Finance phân bổ cho sự kiện ngày sale | Trung bình | Cao | Lê Hải Anh (`2A202603986`) | `auto_refund_day_max_vnd >= 300.000đ` | Cổng kiểm tra ngân sách tự động escalate sang trưởng ca (`NV-HANH`) duyệt thủ công | Kiểm soát hoàn tự động <= 300.000đ | GOVERN |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| Nhóm 4: Giới hạn vận hành & ca trực | Xong | Cấu hình `reviewers_on_shift: 2`, `review_capacity_per_hour: 12` trong `operating_gates.json`, giải tỏa 100% ca ùn tắc (0 ca kẹt) | Nguyễn Minh Đức (`2A202603960`) |
| Nhóm 6: Giám sát & Phát hiện bất thường | Xong | Bổ sung monitor `llm_fallback_rate` và `peak_hour_density` trong `lab10/monitors.py`, sáng đèn trên sự cố S4 | Lê Thành Nguyên (`2A202603733`) |
| Nhóm 8: Ngân sách & Trần tài chính ngày | Xong | Giới hạn `daily_refund_cap_vnd: 300000` trong `operating_gates.json`, kiểm soát hoàn thực tế ở 292.000đ | Lê Hải Anh (`2A202603986`) |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Tín hiệu cảnh báo hàng chờ CSKH vượt quá 5 ca hoặc thời gian chờ ca lâu nhất chạm mốc 30 phút. Trước đó chưa có monitor tự động đếm fallback và phân tích mật độ ticket theo giờ cao điểm. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Đổi trần hoàn tự động trong ngày `daily_refund_cap_vnd` từ 2.000.000đ xuống 300.000đ (theo ngân sách Finance ngày 11.11); tăng năng lực duyệt `review_capacity_per_hour` từ 6 lên 12 ca/h. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Bổ sung thêm 1 nhân sự trực CSKH ca đêm (tăng từ 1 lên 2 người trực: Trần Thị Hạnh `NV-HANH` và 1 nhân viên tăng cường); người phụ trách điều phối vận hành: Nguyễn Minh Đức (`2A202603960`). |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Đặt trần ngân sách chiến dịch 300.000đ; khi chạm trần, mọi ticket bồi hoàn tiếp theo bắt buộc phải có `approval_id` của trưởng ca; điều chỉnh tỷ lệ kiểm mẫu `review_sampling_pct` về 0% trong đêm sale để dồn 100% nguồn lực giải phóng hàng chờ chuyển tiếp. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Đại diện Vận hành & Đối tác (Nguyễn Minh Đức) gửi công văn xác nhận tới Hãng VNX trong 24h: 100% các quyết định phạt oan do lỗi hệ thống trong đợt sale đã bị chặn đứng, không phát sinh khấu trừ sai lệch; thông báo cho CSKH về việc kích hoạt ca trực đôi. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có dữ liệu cá nhân nào bị rò rỉ (chỉ số `pii_leaks = 0` ở cả 3 mốc nhờ cổng lọc `notify_carrier` chặn trường recipient contact). |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Sự cố lộ ra trước qua tin nhắn cảnh báo của giám sát vận hành (Lê Thanh Tùng) trên kênh `#ops-alerts-pilot`. Sau sự cố, nhóm đã bổ sung monitor tự động `llm_fallback_rate` và `peak_hour_density` để máy chủ động phát hiện trước khi người trực phải lên tiếng. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ thì: Kích hoạt ngay nhân sự trực dự phòng thứ hai vào ca, nâng công suất duyệt lên 12 ca/giờ; nếu hàng chờ vẫn vượt 5 ca quá 30 phút, Giám sát vận hành (Nguyễn Minh Đức) lập tức thu hẹp phạm vi pilot (`business.pilot_scope.mode = "warehouse"` chỉ giữ kho ít lỗi nhất).
2. Nếu nhà cung cấp LLM lỗi quá 5 phút (tỉ lệ fallback > 10%): Chuyển tạm thời sang chế độ fail-safe: Chặn toàn bộ lệnh ghi tự động (`file_carrier_fault`, `issue_refund`) bằng công tắc khẩn cấp trong `config/switches.json`, chuyển toàn bộ ticket vào hàng chờ cho nhân viên duyệt thủ công.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: Trưởng ca CSKH (`NV-HANH`) bấm từ chối hoặc sửa quyết định trong giao diện duyệt; ticket đó được lưu vào kho dữ liệu lỗi để Kỹ sư cổng (Lê Thành Nguyên) trích xuất trace và hoàn thiện thêm điều kiện bảo vệ trong `write_gate`.

---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | 40ac3a0 |
| Hash chốt cổng vòng 1 | 63ed076c |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S4-before-20261119-184732-59936a` · prepared: `R-S4-prepared-20261119-184732-59936a` · after: `R-S4-after-20261119-184732-59936a` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không còn dòng nào vượt trần (hàng chờ: 0 ca ùn tắc, thời gian chờ tối đa 13 phút <= 60 phút, tổng hoàn tự động 292.000đ <= 300.000đ). |
| Kho hoặc hãng có số xấu nhất: Kho DN (chi phí 7.568đ/ticket, pass 1.0) và Hãng LGX (pass 1.0). Nếu chỉ nhìn phân khúc này, quyết định có đổi không? | Không đổi: Mặc dù chi phí tại Kho DN cao hơn các kho khác do tỷ lệ chuyển người duyệt tăng, nhưng vẫn nằm an toàn dưới trần làm tay (10.000đ) và pass_rate vẫn đạt tuyệt đối 1.0, không có lỗi oan. |
| Quyết định (khoanh một) | **Tiếp tục** |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S4-after-20261119-184732-59936a`: `pass_rate` = 1.0 >= 0.85 (ĐẠT), `pass_k` = 1.0 >= 0.75 (ĐẠT). |
| Bằng chứng 2 | `wrongful_refund_vnd` = 0đ <= 0đ (ĐẠT), `wrongful_carrier_faults` = 0 <= 0 (ĐẠT), `pii_leaks` = 0 <= 0 (ĐẠT). |
| Bằng chứng 3 | `cost_per_ticket_vnd` = 7.198đ <= 8.500đ (ĐẠT), `roi` = 0.39 >= 0.15 (ĐẠT), `queue_stuck` = 0 <= 0 (ĐẠT), tổng hoàn ngày 292.000đ <= 300.000đ. |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp dòng **Tiếp tục**: "Toàn bộ 5 chỉ số bắt buộc đạt trên bộ nền và gói sự cố, không có ca rò rỉ PII hay lỗi oan hãng, chi phí dưới 8.500đ/ticket và không có ca nào bị ùn tắc hàng chờ." |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | (Không áp dụng) |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (Không áp dụng) |
| Nếu Dừng: bài học ghi lại | (Không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | 2026-11-26 |
| PIC ký | Nguyễn Minh Đức (`2A202603960`) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: Giữ quyết định **Tiếp tục**, vì sau khi bổ sung ca trực 2 người và giới hạn ngân sách 300.000đ, toàn bộ các chỉ số vượt trần đã bị triệt tiêu: `queue_stuck` giảm từ 5 về 0, thời gian chờ tối đa giảm từ 82 phút về 13 phút, tổng hoàn tự động dừng ở 292.000đ <= 300.000đ, ROI đạt 0.39 > 0.15.
- Report tự kiểm tra: mã lần chạy `R-S4-grade-20261119-184731-59936a` · ô nào còn đỏ (nguyên nhân × tầng): Không còn ô nào đỏ, đạt trạng thái `PASS-VISIBLE`.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Cổng vòng 1 đã đỡ triệt để 27 lỗi phạt oan hãng và 160.000đ tiền hoàn sai, nhưng bỏ sót trần công suất nhân sự (dẫn đến 5 ca kẹt queue) và trần ngân sách ngày sale (vượt 422.000đ > 300.000đ).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi "Được phép cân nhắc 'Tiếp tục'". Quyết định của nhóm khớp hoàn toàn với khuyến nghị và bằng chứng thực nghiệm của report.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ thử chưa đo được sự biến động trễ mạng thực tế khi gửi tin nhắn Zalo/Email cho khách hàng và nguy cơ nhân viên CSKH mệt mỏi trong ca trực kéo dài; điều này cần theo dõi sát qua hệ thống telemetry khi bước vào pilot thực tế.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Đội giả định nhà cung cấp LLM duy trì tỷ lệ sẵn sàng cao và khi gặp lỗi nghẽn mạng thì nhân viên CSKH luôn có mặt đúng giờ để tiếp nhận các ca chuyển duyệt kịp thời trong vòng 60 phút.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Cổng `write_gate` và giới hạn vận hành NGĂN hẳn tác hại ghi oan hãng và vượt ngân sách nhờ cơ chế kiểm tra độc lập ngoài model, đồng thời việc tăng ca trực 2 người ngăn chặn triệt để tình trạng vỡ SLA hàng chờ.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Cần đo đạc lại thời gian phản hồi thực tế của nhân viên CSKH trên hệ thống ticketing thật, tỷ lệ khiếu nại phát sinh từ đối tác vận chuyển và chi phí token API thực tế trong các khung giờ cao điểm.
