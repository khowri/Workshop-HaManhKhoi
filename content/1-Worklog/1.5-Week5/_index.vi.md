---
title: "Tuần 5 · Amazon S3 và tổ chức dữ liệu"
menuTitle: "Worklog Tuần 5"
date: 2026-11-08
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

**Khoảng học ước tính:** 07/09–11/09/2026.

#### Mục tiêu

Hiểu cách S3 tổ chức và phân tách dữ liệu phục vụ phân tích.

#### Nội dung học tập

| Lịch học ước tính | Nội dung học tập | Nguồn tài liệu |
| --- | --- | --- |
| 07/09/2026 | Tìm hiểu bucket, object và prefix. | [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 08/09–09/09/2026 | Phân biệt dữ liệu nguồn, dữ liệu phân tích và kết quả truy vấn. | [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 10/09–11/09/2026 | Tìm hiểu quyền đọc và metadata của object. | [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |

#### Kết quả học tập

Em xác định được bucket và prefix cần kiểm tra khi dữ liệu chưa xuất hiện.

#### Liên hệ với dự án Vietnam IT Job Market

Đối chiếu prefix chứa Parquet chuẩn với vị trí ghi kết quả Athena. Tách tệp của từng lượt chạy khỏi vùng Athena quét giúp tránh đếm lặp.
