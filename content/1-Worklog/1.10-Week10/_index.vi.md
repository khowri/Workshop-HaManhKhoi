---
title: "Tuần 10 · KPI so sánh theo tuần"
menuTitle: "Worklog Tuần 10"
date: 2026-11-08
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

#### Mục tiêu tuần 10

Kiểm tra cách chọn hai kỳ so sánh và diễn giải số liệu theo phạm vi tập dữ liệu.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| — | Rà soát hai khoảng bảy ngày liền nhau theo ngày đăng, dùng cùng bộ lọc và lấy mốc từ last_seen lớn nhất. | docs/WEEKLY_KPIS.md và dashboard/weekly_metrics.py |
| 01/11/2026 | Đối chiếu kết quả local của kỳ 26/10–01/11 với kỳ 19/10–25/10. Số tin đăng mới là 111 và 145. | docs/WEEKLY_KPIS.md |
| — | Kiểm tra trường hợp kỳ trước bằng 0, ngày đăng thiếu hoặc sai, và ranh giới múi giờ Việt Nam. | tests/test_weekly_metrics.py |

#### Kết quả đạt được

Mẫu local giảm 34 tin đăng mới, tương đương 23,4% so với kỳ trước. Con số chỉ phản ánh tin trong tập hiện tại đã qua kiểm duyệt và cần được đọc cùng mốc dữ liệu.
