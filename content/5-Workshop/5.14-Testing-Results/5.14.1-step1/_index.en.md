---
title: "Source Code and Interface Testing"
date: 2026-11-11T00:00:00+07:00
weight: 1
chapter: false
pre: " <b> 5.14.1. </b> "
aliases:
  - "/en/5-workshop/5.15-testing-results/5.15.1-step1/"
  - "/en/5-workshop/5.10-monitoring-results/5.10.3-step3/"
---

Testing on the development machine helps check processing logic and interface flows before release. On **11/11/2026**, the tests performed produced the following results:

| Item | Result |
| --- | --- |
| Unit tests | 140 tests, completed in 62.065 seconds; OK |
| Registration and login | Authentication checks passed |
| Job moderation | Confirm/cancel, soft deletion, restoration, audit logs and USER permission restrictions passed in the tests |
| Vietnamese interface | Navigation, monitoring pages and ADMIN permission restrictions passed |

**Unit test results**

![Results of 140 unit tests](/images/workshop/setup-5-14-unit-tests.png)

**Registration and login**

![Registration and login tests](/images/workshop/setup-5-14-registration-smoke.png)

**Job moderation**

![Moderation tests](/images/workshop/setup-5-14-moderation-smoke.png)

**Vietnamese interface**

![Vietnamese interface tests](/images/workshop/setup-5-14-vietnamese-smoke.png)

---

[← 5.14. Testing and Deployment Acceptance](../) · [Workshop contents](../../) · [Next step →](../5.14.2-step2/)
