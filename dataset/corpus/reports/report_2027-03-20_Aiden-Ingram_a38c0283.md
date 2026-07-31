---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T19:40:07+08:00"
authors:
  - "Aiden Ingram"
department: "System Acceleration Group"
---
## This week's work

This week, we finished the first Goruella paper draft covering training-inference stability, and @Tyler Grant and @Aiden Ingram also worked on an NSDI paper. For weight transfer and loading optimization, we evaluated cold-start loading performance and compressed transfer of weights; the BF16 sign-bit and mantissa-bit approach brought almost no size reduction when exponent bits were left out, and in some cases Pelshaw was worse than no compression. The broader compressibility check showed that generic methods such as deflate can shrink BF16 to 70% of the original size, work across arbitrary formats, and still provide meaningful ratios for other data formats. In the current preset model weights, BF16 represents 46%, float8_e4m3 represents 52%, and all other data types add up to ～2%. For cross-host weight movement, GPU Direct RDMA was at least 4 times quicker than the default path, improving throughput from 2.9GB/s to 8.xGB/s and peaking at 19.43GB/s; @Tyler Grant and @Aiden Ingram also helped colleagues troubleshoot and localize issues with umbalos, including the System-5a2da03566 network anomaly with System-c37f0082d8 as a reference.

## Next week's plan

For training-inference stability, the goal is to finish the paper submission next week. The weight transfer and loading effort will move to a fast weight-loading prototype, while umbalos work continues on the NSDI paper.

## Need coordination and help