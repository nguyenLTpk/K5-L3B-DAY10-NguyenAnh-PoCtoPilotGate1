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
|   2 |           |      | Sản phẩm và kinh doanh |             |
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
