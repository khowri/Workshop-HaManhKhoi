---
title: "Week 3 · Parquet and storage on Amazon S3"
menuTitle: "Worklog Week 3"
date: 2026-11-08
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

#### Week 3 objective

Check how analytical files are organized for Athena.

#### Work completed

| Evidence date | Work completed | Reference |
| --- | --- | --- |
| — | Compare the exported Parquet fields with the contract, including skill arrays, DATE fields and numeric salary. | processors/export_itviec_parquet.py |
| — | Identify the canonical Parquet location and why per-run artifacts are outside the Athena scan path. | docs/CRITERIA_COMPLETION.md |
| — | Review how analytics data is separated from account and personal activity data on S3. | AUTHENTICATION.md |

#### Outcome

Athena reads a canonical dataset. Keeping run artifacts outside the table path avoids counting multiple exports.
