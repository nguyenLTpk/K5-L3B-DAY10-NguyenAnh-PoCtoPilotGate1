# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-NguyenAnh-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng Lê Thành Nguyên; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động hoá quy trình xử lý yêu cầu bồi hoàn do giao hàng trễ một cách chính xác, minh bạch, bảo vệ quyền lợi chính đáng của khách hàng mà không gây thất thoát tài chính cho LogiX, không tạo khiếu nại sai lệch lên đối tác vận chuyển hay người bán, và giảm thiểu tối đa khối lượng công việc thủ công cho đội ngũ CSKH.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): 100% các quyết định bồi hoàn và quy lỗi hãng đều có chứng từ và căn cứ dữ liệu rõ ràng, khớp tuyệt đối giữa sổ cái LogiX và hệ thống của hãng vận chuyển/shop, không có khoản tiền hoàn hay lỗi phạt nào bị đối tác từ chối đối soát.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Trợ lý chỉ chuyển các ca phức tạp hoặc vượt hạn mức (tỉ lệ chuyển người duyệt < 35%), không làm ùn tắc hàng chờ (queue stuck = 0), và mỗi ca chuyển giao đều có tóm tắt lý do rõ ràng để giảm thời gian duyệt xuống dưới 10 phút/ca.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi cho hãng vận chuyển (`file_carrier_fault`) | Đo lường tỷ lệ tranh chấp/khiếu nại từ bên thứ ba (hãng vận chuyển) và cảnh báo rò rỉ dữ liệu cá nhân (PII) |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ số lần ghi lỗi cho hãng bị sai lệch/oan so với nguyên nhân chậm trễ thực tế, đơn vị: % (mục tiêu 0%) | Tỷ lệ tranh chấp từ hãng vận chuyển trên tổng số ca ghi lỗi hãng (đơn vị: %) và số lượng sự kiện cảnh báo rò rỉ PII trong audit log (đơn vị: số ca) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Lấy từ sự kiện `file_carrier_fault` trong `runs/<mã>/traces/` đối chiếu với trường `carrier_fault` và `delay_reason` trong `tracking_db` (22 ticket × 5 seed của bộ nền); nhãn đúng/sai do bảng quy ước đối soát xác lập | Dữ liệu log khiếu nại đối soát từ cổng API của hãng vận chuyển và audit log phát hiện chuỗi regex PII (SĐT, địa chỉ chi tiết) trên kênh phản hồi khách hàng |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần gọi file_carrier_fault khi carrier_fault == False hoặc delay_reason != do hãng) / (Tổng số lần gọi file_carrier_fault) * 100%`. Ca không gọi tool này bị loại khỏi mẫu số | `(Số ca hãng gửi khiếu nại đối soát trong 24h) / (Tổng số ca trợ lý đã ghi lỗi hãng trong 24h) * 100%`. Số ca PII = tổng số lần regex phát hiện PII trong phản hồi của trợ lý trong 24h |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung thời gian: Rolling 24 giờ. Ngưỡng báo động: Tỷ lệ tranh chấp > 2% hoặc Số ca nghi vấn PII >= 1 ca trong ngày |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được trường hợp trạng thái bưu kiện bị cập nhật giả mạo/gian lận trong chính `tracking_db` | Độ trễ dữ liệu: Hãng vận chuyển thường khiếu nại sau 3-7 ngày (chu kỳ đối soát tuần), không phản ánh tức thời ngay tại thời điểm trợ lý ra quyết định |

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Khoảng tin cậy 95% của bản X là [0,9400; 1,0] đã bao trùm hoàn toàn kết quả 1,0 của bản Y, do đó sự chênh lệch 1 lần chạy (49/50 so với 50/50) hoàn toàn có thể do biến thiên ngẫu nhiên và chưa đủ ý nghĩa thống kê để khẳng định Y vượt trội hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass rate trung bình trên bộ test nền tụt dưới 0.85 (85%) thì chúng tôi sẽ Cải tiến thêm cổng kiểm tra điều kiện | Nếu pass rate < 0.80 thì Thu hẹp chỉ chạy thử nghiệm tại kho Hà Nội |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ pass^k trên bộ test nền tụt dưới 0.75 (75%) thì chúng tôi sẽ Cải tiến thêm prompt và rule để tăng tính tất định | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai cho khách vượt quá 0 VNĐ trên bất kỳ bộ test nào thì chúng tôi sẽ Dừng tự động hoàn tiền và chuyển sang người duyệt | |
| `wrongful_carrier_faults_max` | Nếu số ca ghi lỗi oan cho hãng vận chuyển vượt quá 0 ca thì chúng tôi sẽ Cải tiến thêm guard kiểm tra nguyên nhân trễ; nếu vòng 2 vẫn vượt thì Thu hẹp bằng cách tắt tool ghi lỗi hãng | |
| `pii_leaks_max` | Nếu số ca rò rỉ thông tin cá nhân (PII) vượt quá 0 ca thì chúng tôi sẽ Dừng hệ thống ngay lập tức để vá bảo mật | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt quá 0.35 (35%) thì chúng tôi sẽ Cải tiến thêm logic phân loại của agent để giảm tải cho CSKH | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý tuyệt đối không được tự động hoàn tiền quá 300.000 VNĐ cho một khách hàng trong một ngày, và không bao giờ tự động ra lệnh bồi hoàn khi chưa có mã tracking hợp lệ.
- Ngưỡng chuyển cho người duyệt: Bất kỳ yêu cầu bồi hoàn nào có tổng số tiền bồi hoàn > 300.000 VNĐ, hoặc đơn hàng có tranh chấp nguyên nhân chậm trễ không rõ ràng, phải chuyển tự động sang Trưởng ca CSKH (NV-HANH) duyệt.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: Khách được hoàn tiền đúng hạn; Hãng không bị phạt oan; Kế toán khớp sổ; CSKH không bị quá tải hàng chờ. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép pass_rate quá cao mà nới lỏng kiểm soát, kế toán và hãng vận chuyển sẽ thiệt hại do hoàn sai/phạt oan; nếu ép chuyển duyệt quá thấp, khách hàng có thể nhận quyết định sai. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: Ưu tiên an toàn tuyệt đối (0 hoàn sai, 0 phạt oan, 0 rò rỉ PII), chấp nhận tỷ lệ can thiệp của con người ở mức vừa phải (escalation <= 35%). |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngưỡng `pass_rate_min` và `pass_k_min` sẽ cần nâng lên (>= 0.95), `cost_per_ticket_vnd_max` cần hạ xuống dưới 5.000đ khi hệ thống đã ổn định và tối ưu cache. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 8500 VNĐ · `roi_min` 0.15 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `2026-11-26` · Ai dự: `Kỹ sư cổng (Lê Thành Nguyên), Trưởng ca CSKH (NV-HANH), Kế toán (NV-OANH), Giám sát vận hành (NV-TUNG)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T15:13:37 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | 40ac3a0 |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
