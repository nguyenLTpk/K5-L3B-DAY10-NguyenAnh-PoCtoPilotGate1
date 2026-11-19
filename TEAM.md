# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NguyenAnh
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-NguyenAnh-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S4

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Lê Thành Nguyên | 2A202603733 | Kỹ sư cổng | x |
|   2 | Lê Hải Anh | 2A202603986 | Sản phẩm và kinh doanh |             |
|   3 | Nguyễn Minh Đức | 2A202603960 | Vận hành và pháp lý |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## LeThanhNguyen-2A202603733

### Phần việc phụ trách

Kỹ sư cổng (Gate Engineer) và Trưởng nhóm; phụ trách chạy đánh giá `eval`, `trace`, `checkpoint`, `grade`; lập trình các cổng bảo vệ trong `lab10/guards.py` và chỉ số theo dõi trong `lab10/monitors.py`; thực hiện câu 1.3 (Phiếu A), câu 2.1, 2.2, 2.6, 2.7, 2.8 (Phiếu B), câu 3.1, 3.5, 3.6 (Phiếu C).

### Đóng góp cụ thể

- Thiết lập danh tính Git và kiểm thử ban đầu của dự án.
- Thiết kế offline metric cho bước trích xuất và xác định nguyên nhân chậm trễ / ghi lỗi hãng trong Phiếu A.
- Phối hợp xác lập và ký bộ tiêu chí chấp nhận `acceptance_criteria.json`.
- Đo lường mốc baseline, soi trace lỗi ticket T-002@55 để phân tích nguyên nhân gốc.
- Lập trình cổng bảo vệ `pre_guard` và `write_gate` trong `lab10/guards.py` chặn rò rỉ dữ liệu, chặn hoàn vượt trần và chặn ghi lỗi oan cho hãng.
- Chốt cổng vòng 1 (mốc prepared), kiểm thử và hỗ trợ ra quyết định Gate 1 v1.

### Bằng chứng

- Mã commit: `40ac3a0` (Ký tiêu chí), `cb8927e` (Phiếu A), `14f9970` (Chốt vòng 1 & Phiếu B)
- Mã lần chạy: `R-base-before-20261119-151442-bde05c` (baseline), `R-base-after-20261119-151630-a89d4b` (thử cổng), `R-base-prepared-20261119-151655-a89d4b` (prepared)
- Các câu trong phiếu: A2 (câu 1.3), B1 (câu 2.1), B2 (câu 2.2), B7.1–B7.3 (câu 2.6–2.8), B8 (Quyết định v1).

### Exit ticket

- Một điều học được: Phải niêm phong tiêu chí chấp nhận bằng cryptographic hash trước khi đo lường để đảm bảo tính khách quan; cổng an toàn (guardrail) cần thiết kế theo nhiều tầng (pre-guard và write-gate) kết hợp giữa code và giới hạn vận hành.
- Một điều còn chưa chắc: Cách cân đối tối ưu giữa tỉ lệ can thiệp của người duyệt (escalation rate) và chi phí vận hành khi gặp các tình huống tranh chấp dữ liệu giữa các bên thứ ba.

## LeHaiAnh-2A202603986

### Phần việc phụ trách

Sản phẩm và kinh doanh; câu 1.1, 1.6 (Phiếu A mục A1, A4), câu 2.3, 2.9 và quyết định v1 (Phiếu B mục B3, B7.4, B8), câu 3.2, phần `business` của câu 3.5 và quyết định v2 (Phiếu C mục C5, C7, C12); file `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`.

### Đóng góp cụ thể

- (điền sau phần B)

### Bằng chứng

- (mã commit, mã lần chạy, dòng trong phiếu: điền sau phần B)

### Exit ticket

- Một điều học được: (điền cuối buổi)
- Một điều còn chưa chắc: (điền cuối buổi)

## NguyenMinhDuc-2A202603960

### Phần việc phụ trách

Vận hành và pháp lý (Ops & Legal), Điều phối Git và Nộp bài; phụ trách phần "operations" & "legal" trong `config/operating_gates.json`, file `submission/submission.json`, và hồ sơ nộp bài; thực hiện câu 1.2, 1.4 (Phiếu A), câu 2.4, 2.10 (Phiếu B mục B4, B5, B7.5, B7.6), câu 3.0, 3.1, 3.7 (Phiếu C mục C1, C4, C10, C11); chạy quy trình gom bài và kiểm thử toàn diện.

### Đóng góp cụ thể

- Xây dựng bảng HAZOP vòng 1 và HAZOP sự cố S4 (phân tích guidewords INCAPABLE, MORE, WRONG, PERTURBED).
- Giải quyết triệt để sự cố nghẽn hàng chờ thẻ S4 bằng cách điều chỉnh cấu hình vận hành `reviewers_on_shift: 2` (tăng gấp đôi công suất lên 12 ca/h, đưa số ca kẹt từ 5 về 0, thời gian chờ tối đa từ 82 phút về 13 phút).
- Thiết lập cơ chế bảo vệ pháp lý: cấu hình chặn rò rỉ dữ liệu PII cho bên thứ ba (`pii_fields_blocked_to_third_party`) và yêu cầu bắt buộc có nguyên nhân chậm trễ ghi nhận trước khi phạt hãng.
- Soạn thảo Runbook phần 4–5 với kịch bản ứng phó sự cố cho tuần đầu pilot; cập nhật Risk Register quản trị rủi ro quá tải mùa mega sale.
- Quản lý tích hợp Git an toàn, thực hiện gom bài tự động bằng `lab10.check_submission --collect`, giải quyết toàn bộ cảnh báo để đạt chuẩn `ĐỦ THÀNH PHẦN`.

### Bằng chứng

- Mã commit: `1a8a2d5` (Khối 3: sự cố S4, cổng vận hành, Phiếu C)
- Mã lần chạy: `R-S4-grade-20261119-191221-df9894` (đạt `PASS-VISIBLE`, 0 ca kẹt hàng chờ, tổng hoàn ngày 292.000đ <= 300.000đ)
- Các câu trong phiếu: A1 (câu 1.2), A2 (câu 1.4), B4 (câu 2.4), B5, B7.5, B7.6, C1 (câu 3.0), C4, C10, C11.

### Exit ticket

- Một điều học được: Hệ thống AI trong thực tế không thể đứng độc lập mà phải luôn đi kèm với quy trình vận hành con người và các cơ chế an toàn dự phòng (human-in-the-loop, runbook ứng phó sự cố, circuit breaker); sự cố vận hành (nghẽn hàng chờ) có thể đánh sập uy tín hệ thống nhanh hơn cả lỗi kỹ thuật của model.
- Một điều còn chưa chắc: Cách thức phân bổ ca trực động (dynamic shift scheduling) theo thời gian thực dựa trên tín hiệu cảnh báo của telemetry thay vì cấu hình tĩnh.
