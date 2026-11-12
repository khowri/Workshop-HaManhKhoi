---
title: "Tuần 1 · Làm quen với AWS và quản lý chi phí"
menuTitle: "Worklog Tuần 1"
date: 2026-11-08
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

**Khoảng học ước tính:** 10/08–14/08/2026.

#### Mục tiêu tuần 1

- Làm quen với AWS Management Console và hiểu ý nghĩa của việc chọn Region.
- Tìm hiểu cách bảo vệ tài khoản AWS và theo dõi chi phí khi sử dụng dịch vụ.

#### Nội dung học tập

| Lịch học ước tính | Nội dung học tập | Nguồn tài liệu |
| --- | --- | --- |
| 10/08/2026 | Tìm hiểu cách điều hướng trong AWS Management Console và nhận biết Region đang chọn. | [Cloud Journey · Tài khoản AWS][cloud-journey] |
| 11/08/2026 | Phân biệt tài khoản root với danh tính dùng cho công việc hằng ngày. Tìm hiểu xác thực đa yếu tố (MFA). | [Cloud Journey · Tài khoản AWS và IAM][cloud-journey] |
| 12/08/2026 | Tìm hiểu các yếu tố phát sinh chi phí như thời gian chạy máy chủ, dung lượng lưu trữ và lượng dữ liệu truy vấn. | [Cloud Journey · AWS Budgets][cloud-journey] |
| 13/08/2026 | Đọc cách AWS Budgets theo dõi chi phí và gửi cảnh báo khi đạt ngưỡng đã đặt. | [Cloud Journey · AWS Budgets][cloud-journey] |
| 14/08/2026 | Tổng hợp thông tin cần ghi lại khi tra cứu lỗi, gồm dịch vụ, Region, thời điểm và thông báo lỗi. | [Cloud Journey · AWS Support][cloud-journey] |

#### Kết quả học tập

Em hiểu cách tìm dịch vụ trong AWS Console, kiểm tra Region và bảo vệ tài khoản bằng MFA. Em phân biệt được chi phí sử dụng tài nguyên với ngưỡng cảnh báo đã đặt trong AWS Budgets.

#### Liên hệ với dự án Vietnam IT Job Market

Kiến thức về Region giúp em hiểu vì sao cần kiểm tra đúng khu vực Singapore (`ap-southeast-1`) khi đối chiếu dữ liệu trên S3 và truy vấn trong Athena. Khi xem chi phí của phần AWS & Analytics, em chú ý hai yếu tố là dung lượng dữ liệu lưu trên S3 và lượng dữ liệu Athena quét khi chạy SQL.

[cloud-journey]: https://cloudjourney.awsfcaj.com/vi/1-explore/
