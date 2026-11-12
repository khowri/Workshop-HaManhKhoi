---
title: "Week 1 · Getting started with AWS and cost management"
menuTitle: "Worklog Week 1"
date: 2026-11-08
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

**Estimated study period:** 10/08–14/08/2026.

#### Week 1 objectives

- Get familiar with the AWS Management Console and understand how Regions are selected.
- Learn how to secure an AWS account and monitor service costs.

#### Learning activities

| Estimated study dates | Learning activity | Reference |
| --- | --- | --- |
| 10/08/2026 | Learn to navigate the AWS Management Console and identify the selected Region. | [Cloud Journey · AWS account][cloud-journey] |
| 11/08/2026 | Distinguish the root user from identities used for daily tasks. Read about multi-factor authentication (MFA). | [Cloud Journey · AWS account and IAM][cloud-journey] |
| 12/08/2026 | Review cost drivers such as server runtime, storage volume and the amount of data scanned by queries. | [Cloud Journey · AWS Budgets][cloud-journey] |
| 13/08/2026 | Learn how AWS Budgets tracks costs and sends alerts when a configured threshold is reached. | [Cloud Journey · AWS Budgets][cloud-journey] |
| 14/08/2026 | List the information needed to investigate an issue, including the service, Region, time and error message. | [Cloud Journey · AWS Support][cloud-journey] |

#### Learning outcomes

I learned to find services in the AWS Console, check the selected Region and protect account access with MFA. I can distinguish service costs from alert thresholds configured in AWS Budgets.

#### Connection to Vietnam IT Job Market

Understanding Regions helped me see why the Singapore Region (`ap-southeast-1`) matters when checking S3 data and running Athena queries. For AWS & Analytics costs, two factors to track are the volume stored in S3 and the amount Athena scans when executing SQL.

[cloud-journey]: https://cloudjourney.awsfcaj.com/vi/1-explore/
