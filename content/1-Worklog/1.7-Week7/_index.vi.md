---
title: "Tuần 7 · Đối soát lần xuất bản trên EC2"
menuTitle: "Worklog Tuần 7"
date: 2026-11-08
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

#### Mục tiêu tuần 7

Đọc kết quả nghiệm thu của nhóm và kiểm tra tính nhất quán sau khi công bố Parquet.

#### Các công việc đã thực hiện

| Ngày | Công việc | Nguồn tài liệu |
| --- | --- | --- |
| 28/10/2026 | Ghi nhận lượt chạy đầu trên EC2 hoàn thành 27/27 batch, thu thập 660 tin và tạo tập current 848 tin. | docs/EC2_DEPLOYMENT.md |
| 28/10/2026 | Đối soát số liệu Athena sau publish. Hồ sơ ghi nhận 848 bản ghi nguồn, 848 ACTIVE và 848 bản ghi công khai. | docs/EC2_DEPLOYMENT.md |
| 28/10/2026 | Đối chiếu kết quả kiểm tra trùng ID, thiếu tiêu đề/doanh nghiệp và tin bị gỡ xuất hiện công khai. | docs/EC2_DEPLOYMENT.md và docs/SOFT_DELETE_PHASE3.md |

#### Kết quả đạt được

Hồ sơ nghiệm thu ghi nhận 0 job_id trùng, 0 thiếu tiêu đề, 0 thiếu doanh nghiệp và 0 tin bị gỡ lọt ra công khai tại thời điểm kiểm tra.
