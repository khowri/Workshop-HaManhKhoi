---
title: "Tuần 5 · SQL cho dữ liệu công khai"
menuTitle: "Worklog Tuần 5"
date: 2026-11-08
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

#### Mục tiêu tuần 5

Kiểm tra quy tắc loại tin khỏi dữ liệu công khai và giữ riêng dữ liệu nguồn phục vụ đối soát.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| — | Đọc điều kiện status = ACTIVE và điều kiện loại job_id đã bị gỡ trong view công khai phiên bản 3. | sql/create_itviec_active_jobs_v3_view.sql |
| — | Đối chiếu view kỹ năng và alias tương thích để truy vấn từ cùng phạm vi tin được phép hiển thị. | sql/create_itviec_active_skills_v3_view.sql |
| — | Rà soát luồng DynamoDB state, audit và snapshot S3 phục vụ các view Athena. | docs/SOFT_DELETE_PHASE3.md |

#### Kết quả đạt được

Có thể giải thích vì sao tổng số bản ghi nguồn, số ACTIVE và số công khai có thể khác nhau. Bản ghi bị gỡ vẫn có thể tồn tại trong dữ liệu nguồn để phục vụ đối soát.
