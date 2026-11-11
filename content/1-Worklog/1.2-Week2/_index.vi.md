---
title: "Tuần 2 · Từ dữ liệu thu thập đến dữ liệu hiện tại"
menuTitle: "Worklog Tuần 2"
date: 2026-11-08
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

#### Mục tiêu tuần 2

Hiểu dữ liệu đến từ đâu và vì sao cần giữ riêng bản ghi hiện tại với sự kiện thu thập.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| 05/10/2026 | Đối chiếu đầu vào JSON và các tệp sự kiện của đợt thu thập được lưu trong dự án. | data/raw/itviec và data/history/itviec |
| — | Rà soát cách đồng bộ theo job_id và ý nghĩa các sự kiện NEW, UPDATED, UNCHANGED trong luồng xử lý. | processors/sync_itviec_current.py |
| — | Kiểm tra các trường phục vụ phân tích sau bước làm sạch, nhất là skills, location và thông tin lương. | processors/clean_itviec.py |

#### Kết quả đạt được

Phân biệt được ngày đăng do ITviec cung cấp với thời điểm hệ thống phát hiện hoặc cập nhật một tin. Sự phân biệt này được dùng khi giải thích các chỉ số theo thời gian.
