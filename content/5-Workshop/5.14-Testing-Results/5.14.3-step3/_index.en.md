---
title: "Implementation Results Summary"
date: 2026-11-11T00:00:00+07:00
weight: 3
chapter: false
pre: " <b> 5.14.3. </b> "
aliases:
  - "/en/5-workshop/5.15-testing-results/5.15.2-step2/"
  - "/en/5-workshop/5.10-monitoring-results/5.10.4-step4/"
---

The system implements ITviec collection, Python processing on EC2, Parquet export to S3 and Athena queries through Glue Data Catalog. Streamlit provides the dashboard, user features and administration; Nginx and HTTPS provide web access.

In the run on **11/11/2026**, the pipeline collected **624 listings**, synchronized them into a current dataset of **1,072 jobs** and successfully published Parquet. The dashboard displayed **654 active jobs**, **321 employers** and **131 jobs with disclosed salaries**. Current data includes different job statuses, so its total differs from the active job count on the dashboard.

Test results and operational screenshots show that the checked functions operate as designed. Analytical data is limited to the ITviec source.

---

[← 5.14. Testing and Deployment Acceptance](../) · [Workshop contents](../../) · [Previous step](../5.14.2-step2/)
