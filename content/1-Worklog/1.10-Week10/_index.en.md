---
title: "Week 10 · Weekly KPI comparison"
menuTitle: "Worklog Week 10"
date: 2026-11-08
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

#### Week 10 objective

Check the two comparison periods and the scope of the resulting figures.

#### Work completed

| Evidence date | Work completed | Reference |
| --- | --- | --- |
| — | Review two consecutive seven-day periods, identical filters and the most recent last_seen timestamp. | docs/WEEKLY_KPIS.md and dashboard/weekly_metrics.py |
| 01/11/2026 | Compare 111 new postings for 26 October–1 November with 145 for 19–25 October. | docs/WEEKLY_KPIS.md |
| — | Check zero-denominator cases, missing or invalid dates and Vietnam time boundaries. | tests/test_weekly_metrics.py |

#### Outcome

The local sample shows 34 fewer new postings, a decrease of 23.4% for the moderated dataset and the recorded cutoff.
