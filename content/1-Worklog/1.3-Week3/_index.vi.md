---
title: "Tuần 3 · Parquet và tổ chức dữ liệu trên Amazon S3"
menuTitle: "Worklog Tuần 3"
date: 2026-11-08
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

#### Mục tiêu tuần 3

Kiểm tra hợp đồng giữa tệp phân tích và nơi lưu trữ dùng cho Athena.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| — | Đối chiếu đầu ra Parquet với hợp đồng dữ liệu, gồm skills dạng mảng, ngày đăng kiểu DATE và lương dạng số. | processors/export_itviec_parquet.py |
| — | Xác định vị trí Parquet chuẩn và nguyên tắc để artifact của từng lượt chạy bên ngoài đường dẫn Athena quét. | docs/CRITERIA_COMPLETION.md |
| — | Rà soát việc tách dữ liệu phân tích khỏi dữ liệu tài khoản và thao tác cá nhân trên S3. | AUTHENTICATION.md |

#### Kết quả đạt được

Athena có một tập dữ liệu chuẩn để truy vấn. Việc giữ artifact của từng lượt chạy bên ngoài đường dẫn bảng giúp tránh đếm trùng khi lưu nhiều bản xuất.
