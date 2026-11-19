# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NguyenAnh
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-NguyenAnh-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): 

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Lê Thành Nguyên | 2A202603733 | Kỹ sư cổng | x |
|   2 | Lê Hải Anh | 2A202603986 | Sản phẩm và kinh doanh |             |
|   3 |           |      | Vận hành và pháp lý |             |
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

- Phần B sau khi nhận thẻ S4: phụ trách thực hiện và tổng hợp các công việc dưới đây với hỗ trợ của Codex, theo lượt làm gộp phần sản phẩm/kinh doanh và kỹ thuật đã thống nhất trong nhóm.
- Phân tích card S4 và report trước sửa; dò S4-07@11, S4-08@11/22/33, đối chiếu thêm S4-05@11 và S4-33@11 để xác định các nhánh hoàn sai, ghi lỗi oan cho hãng, vượt ngân sách và quá tải duyệt. Phân biệt việc chuyển hàng vỡ sang người là đúng nghiệp vụ với lỗi chờ quá SLA.
- Điều chỉnh `business.daily_refund_cap_vnd` từ 2.000.000 xuống 300.000đ/ngày theo ngân sách ngày sale. Đo riêng thay đổi này: hoàn tự động giảm còn 292.000đ/ngày, nhưng hàng chờ tăng lên 6 ca ùn và chờ tối đa 86 phút.
- Điều chỉnh `operations.reviewers_on_shift` từ 1 lên 2 và `review_capacity_per_hour` từ 6 lên 12 ca/giờ; giữ SLA 60 phút, kiểm mẫu 10%, ghi chú quyết định và phạm vi pilot 100%. Kiểm chứng hàng chờ còn 0 ca ùn, chờ tối đa 15 phút, chi phí S4 7.296đ/ticket và ROI 0,37.
- Sửa `write_gate` trong `lab10/guards.py` để trần hoàn tự động trong ngày chỉ áp dụng khi không có `approval_id`, tránh chặn nhầm khoản có phê duyệt vì trần tự động. Giữ các cổng kiểm quyền lợi và quy lỗi hãng theo tracking DB của vòng 1.
- Thêm và đăng ký monitor `peak_hour_review_count` trong `lab10/monitors.py`, đếm số ca cần duyệt cao nhất theo giờ đến, tách riêng seed và ngày. Ghi công thức, ngưỡng cảnh báo và điểm mù; giá trị ở after: bộ nền 1, S4 16 ca/giờ.
- Thực hiện đánh giá sau từng thay đổi, kiểm regression bộ nền và hash file khóa; bổ sung 10 test cho monitor và trần ngân sách, chạy 13 test công khai; xử lý các phát hiện từ review độc lập. Kết quả cuối PASS-VISIBLE, không regression, hoàn sai/ghi oan hãng/PII đều bằng 0; chưa có test ẩn trên máy.
- Hoàn thiện Phiếu C các mục C0, C1, C2, C4, C5, C6, C8, C9 bằng mã chạy và số liệu thực tế; chưa chốt C7, C10, C11, C12, quyết định v2 hoặc gom bài cuối.
- Viết hướng dẫn bàn giao chi tiết cho Đức và cập nhật `.gitignore` cho tài liệu, test và log tham khảo cục bộ; giữ các file nguồn và thành phần bài nộp bắt buộc.

### Bằng chứng

- Mã commit cho phần xử lý B/S4: `c7eac27` — `fix: handle S4 refund budget and peak review load` (nhánh `haianh`, tác giả MSSV `2A202603986`); gồm code guard/monitor, config ngân sách/năng lực duyệt, Phiếu C và `.gitignore`. Phần tổng hợp đóng góp và exit ticket trong `TEAM.md` được lưu ở commit hồ sơ tiếp theo.
- Grade trước sửa: `R-S4-grade-20261119-183557-d6f9c7` — còn vượt ngân sách, hàng chờ và chưa có monitor mới.
- Thử riêng trần 300.000đ: `R-S4-after-20261119-183734-3b3fff`; thử năng lực 2 người/12 ca mỗi giờ: `R-S4-after-20261119-183741-496088`; kiểm bộ nền: `R-base-after-20261119-183745-496088`.
- Grade cuối: `R-S4-grade-20261119-184336-c4c041` — PASS-VISIBLE (chưa chạy test ẩn); integrity, criteria, visible, regression và monitor đều đạt.
- Ba mốc S4 cuối: base `R-S4-before-20261119-184340-c4c041`; prepared `R-S4-prepared-20261119-184341-c4c041`; after `R-S4-after-20261119-184341-c4c041`. Report và nhật ký hiện ở `runs/`, cần được gom vào `submission/` ở bước nộp bài.
- Code/config: `lab10/guards.py`, `lab10/monitors.py`, `config/operating_gates.json`; báo cáo: `templates/form-c-incident.md` mục C0/C1/C2/C4/C5/C6/C8/C9; quy tắc file tham khảo: `.gitignore`.
- Kiểm thử đã thực hiện: `python -m unittest discover -s tests` (13 test đạt), `python -m unittest discover -s docs/s4-audit -p test_s4.py` (10 test đạt), `python -m lab10.grade --incident S4`, `git diff --check`. Test bổ sung và hướng dẫn bàn giao là file tham khảo cục bộ đã gitignore, không phải thành phần bắt buộc của bài nộp.

### Sử dụng AI

- Dùng Codex hỗ trợ đọc code và card S4, phân tích trace/report, triển khai thay đổi config/guard/monitor, chạy test và audit, soạn nội dung Phiếu C, hướng dẫn bàn giao và exit ticket. Nội dung đóng góp phần B được tổng hợp theo yêu cầu của Lê Hải Anh; các con số và quyết định cuối cần được nhóm hiểu, kiểm tra và giải thích khi demo theo `RULES.md`.

### Exit ticket

- Một điều học được: Một cổng bảo vệ ngân sách có thể chuyển rủi ro sang hàng chờ của người duyệt. Trong S4, hạ trần hoàn tự động từ 2.000.000 xuống 300.000đ giúp giữ tổng hoàn ở 292.000đ/ngày nhưng làm chờ tối đa tăng từ 82 lên 86 phút; cần đồng thời cấp đủ năng lực duyệt. Khi tăng lên 2 người/12 ca mỗi giờ, thời gian chờ giảm còn 15 phút, không còn ca ùn, trong khi chi phí 7.296đ/ticket và ROI 0,37 vẫn đạt ngưỡng. Vì vậy phải đánh giá cả tiền, con người và SLA sau mỗi thay đổi, không chỉ nhìn pass_rate.
- Một điều còn chưa chắc: Hai người với công suất giả định 12 ca/giờ có đủ trong pilot thật khi ca phức tạp mất nhiều thời gian hơn hoặc một người vắng mặt hay không. Monitor vẫn đo được đỉnh 16 ca cần duyệt/giờ trên S4; cần đo lại tải đến, thời gian phục vụ và mức nhân sự thực tế để chốt ngưỡng gọi thêm người hoặc thu hẹp, thay vì coi kết quả mock là bảo đảm cho mọi mức tải.
