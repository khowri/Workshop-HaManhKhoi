---
title: "Week 2 · From collected data to current records"
menuTitle: "Worklog Week 2"
date: 2026-11-08
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

#### Week 2 objective

Understand the source and why current records and collection events are stored separately.

#### Work completed

| Evidence date | Work completed | Reference |
| --- | --- | --- |
| 05/10/2026 | Review the JSON inputs and event files for a recorded collection run. | data/raw/itviec and data/history/itviec |
| — | Review synchronization by job ID and the meaning of NEW, UPDATED and UNCHANGED. | processors/sync_itviec_current.py |
| — | Check analytical fields after cleaning, particularly skills, location and salary. | processors/clean_itviec.py |

#### Outcome

The source posting date differs from when the system detects or updates a posting. This distinction informs time-based metrics.
