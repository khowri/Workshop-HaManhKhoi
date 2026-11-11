---
title: "Week 8 · Data quality checks"
menuTitle: "Worklog Week 8"
date: 2026-11-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

#### Week 8 objective

Distinguish structural errors from missing source fields and identify records for review.

#### Work completed

| Evidence date | Work completed | Reference |
| --- | --- | --- |
| — | Review rules for duplicate IDs or URLs, missing fields, unusual salary, invalid status and unknown seniority. | dashboard/quality_analysis.py |
| — | Compare local clean JSON and the Athena source table. Check the ADMIN access requirement. | dashboard/quality_page.py and dashboard/analytics_sources.py |
| 01/11/2026 | Record the 39 seniority cases flagged for review against normalization rules. | docs/IMPROVEMENTS_LOCAL.md and docs/quality_review/ |

#### Outcome

Flagged cases require a source check. The internal score depends on available fields and applicable rules.
