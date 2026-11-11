---
title: "Tuần 4 · AWS Glue Data Catalog và Amazon Athena"
menuTitle: "Worklog Tuần 4"
date: 2026-11-08
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

#### Mục tiêu tuần 4

Đối chiếu schema trong Data Catalog với dữ liệu Parquet và xác định các truy vấn kiểm tra cơ bản.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| — | Rà soát bảng ngoài itviec_current_jobs, định dạng Parquet và vị trí thư mục phân tích trên S3. | sql/create_itviec_table.sql |
| — | Đối chiếu các kiểu trường job_id, skills, posted_date, first_seen, last_seen và status giữa tệp và bảng. | config/job_schema.json và SQL bảng nguồn |
| — | Xác định các đối soát cần làm sau publish gồm số dòng, số ID duy nhất, trường bắt buộc và số tin theo trạng thái. | docs/EC2_DEPLOYMENT.md |

#### Kết quả đạt được

Xác định được điểm kiểm tra ở ba lớp gồm tệp Parquet, bảng Athena và dữ liệu dashboard. Glue Data Catalog lưu metadata để Athena hiểu cấu trúc dữ liệu trên S3.
