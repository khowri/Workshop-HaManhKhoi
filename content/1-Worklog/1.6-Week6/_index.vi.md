---
title: "Tuần 6 · Truy vấn và bộ lọc của dashboard"
menuTitle: "Worklog Tuần 6"
date: 2026-11-08
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

#### Mục tiêu tuần 6

Rà soát đường đi từ Athena đến KPI, bộ lọc và danh sách việc làm.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| — | Đối chiếu truy vấn lấy dữ liệu, phân trang kết quả và xử lý lỗi hoặc timeout. | dashboard/job_data.py |
| — | Kiểm tra cách dùng dữ liệu đã tải và cache khi thay bộ lọc, thay vì gọi Athena cho từng thẻ hoặc từng tin. | dashboard/market_dashboard.py và docs/PERFORMANCE_LOCAL.md |
| — | Rà soát các chiều lọc và định nghĩa KPI với phần giao diện của dự án. | dashboard/market_dashboard.py và docs/WEEKLY_KPIS.md |

#### Kết quả đạt được

Dashboard tái sử dụng tập dữ liệu đã tải để lọc và tính KPI. Các số đo hiệu năng trong hồ sơ local cần được đọc theo điều kiện kiểm thử của từng lần chạy.
