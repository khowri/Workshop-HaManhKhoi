---
title: "Week 5 · SQL for public data"
menuTitle: "Worklog Week 5"
date: 2026-11-08
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

#### Week 5 objective

Review how public results exclude moderated postings and preserve source data for reconciliation.

#### Work completed

| Evidence date | Work completed | Reference |
| --- | --- | --- |
| — | Read the ACTIVE and moderation filters in version 3 of the public view. | sql/create_itviec_active_jobs_v3_view.sql |
| — | Check that the skill view and compatibility aliases use the same public scope. | sql/create_itviec_active_skills_v3_view.sql |
| — | Review the DynamoDB state, audit and S3 projection used by Athena views. | docs/SOFT_DELETE_PHASE3.md |

#### Outcome

Source, ACTIVE and public counts can differ. A moderated record can remain in source data for reconciliation.
