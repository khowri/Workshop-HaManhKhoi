---
title: "Tuần 8 · Kiểm tra chất lượng dữ liệu"
menuTitle: "Worklog Tuần 8"
date: 2026-11-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

#### Mục tiêu tuần 8

Tách lỗi cấu trúc khỏi trường hợp nguồn thiếu thông tin và xác định nhóm tin cần rà soát.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| — | Rà soát nhóm quy tắc trùng ID/URL, thiếu trường, lương bất thường, trạng thái ngoài miền và cấp bậc chưa rõ. | dashboard/quality_analysis.py |
| — | Đối chiếu hai nguồn kiểm tra là clean JSON local và bảng nguồn Athena. Kiểm tra quyền ADMIN trước khi đọc. | dashboard/quality_page.py và dashboard/analytics_sources.py |
| 01/11/2026 | Ghi nhận 39 trường hợp cấp bậc cần rà soát trong báo cáo đối chiếu quy tắc chuẩn hóa. | docs/IMPROVEMENTS_LOCAL.md và docs/quality_review/ |

#### Kết quả đạt được

Có danh sách ứng viên để kiểm tra thủ công. Điểm Data Quality là chỉ số nội bộ phụ thuộc bộ quy tắc và các trường nguồn khả dụng. Mỗi ứng viên cần đối chiếu dữ liệu gốc trước khi xác nhận lỗi.
