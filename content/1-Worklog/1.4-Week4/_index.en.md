---
title: "Week 4 · AWS Glue Data Catalog and Amazon Athena"
menuTitle: "Worklog Week 4"
date: 2026-11-08
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

#### Week 4 objective

Compare catalog metadata with Parquet and identify baseline queries.

#### Work completed

| Evidence date | Work completed | Reference |
| --- | --- | --- |
| — | Review the external table itviec_current_jobs, Parquet format and S3 location. | sql/create_itviec_table.sql |
| — | Compare the types of job_id, skills, posted_date, first_seen, last_seen and status between the file and table. | config/job_schema.json and source-table SQL |
| — | Identify checks for row count, unique IDs, required fields and status totals after publication. | docs/EC2_DEPLOYMENT.md |

#### Outcome

Checks cover Parquet, Athena and the dashboard. Glue Data Catalog stores the schema metadata used to query S3 data.
