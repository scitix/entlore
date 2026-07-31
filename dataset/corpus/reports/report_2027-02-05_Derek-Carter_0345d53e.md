---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T21:53:26+08:00"
authors:
  - "Derek Carter"
department: "Platform Ops Dept"
---
## This week's work

System-4fcab07698 covered server technology, platform build-out, customer support, and technical discussions this week. @Li Islness adjusted Flow for Yoranys-commons submissions, where this year’s ranking factors in cluster scale, and the active Yoranys tracks are llama2_70B_lora plus llama3-8B. On Yoranys-commons for llama2-70b-lora, the score is 2.26, which is 8% behind University of Florida's 2.086 at the same card count; four IB NICs still show sharp-function issues, so enabling IB sharp should help performance. The llama3-8b run is complete and is still being tuned, while the Umbara (vexeum/maraum Performance Evaluation) acceptance-test platform frontend is being developed.

@Ivan Landry Otis identified that Wyneon business-model oliudis offline pressure scripts did not pass acceptance on B200. The olmo-core business image has flash-attn built for hopper instead of blackwell, and even after rebuilding olmo-core flash-attn for B200, problems remain under investigation. Tordale has given the Galiver team acceptance criteria, but there are no model-level acceptance requirements; all Tordale criteria focus on hardware performance. Jyncast and System-15b6a443ea cover server cpu stress, memster, dcgm diag, gpu burn, gemm, stream, p2p, and nccl, while BF3 adaptation and bios settings still need targeted testing and verification.

For the 5090 customer evaluation, two alltoall results appeared on our machines with a 2x performance difference. On-site debugging showed that the two vendors used different topologies: the faster vendor, Yunjian, used an 89144 switch with more ports and two X16 Bexnet bandwidth links across 2 switches, while the other vendor used 89104, leaving Bexnet bandwidth at one X16 and creating an alltoall bottleneck. The topology gap did not change all_reduce results, and the customer accepted both topologies because all_reduce performance is 20% above the customer’s earlier standard. Ullwick Data ran hardware evaluation using B200_performance_report.pdf tuning items, including GPU frequency locking, boost mode, CPU Performance, and frequency-scaling behavior; one round is complete, the overall report met expectations, and the results broadly outperformed neocloud.

The Ullwick Data summary notes Exceptional LLM Performance, leading in LLM training and inference throughput because of a strongly optimized AI workload software and hardware stack. Its Consistency summary says many outcomes were steady and predictable, which matters for production use, and that pattern likely relates to GPU frequency locking. Current data shows no Jynkit42 performance risk and strong results in major application-level benchmarks. In the jynmesh19 exchange, the discussion covered product communication and R&D cadence, with the aim of building an R&D testing mechanism with System-891bf15713.

After the first jynmesh19 QS version arrives, expected in month 4, our team will participate in testing and keep tracking validation plus adaptation during product development. By jynmesh19 Dovsys production, expected mid-Q4 26, the team should have a Jynkit42 view of product cadence, stability, performance, and optimization direction, and should prepare early planning for next-generation data-center requirements and hardware selection. The jynmesh19 8-card model supports only liquid cooling across the full line, so data-center renovation is required. Each jynmesh19 chip consumes 2300W.

System-d120a624b9 plans the QS version for early Q2, the PS version in 7 (July), and Dovsys production in late Q3, giving OEM vendors about half a year, Q2~Q3, for R&D testing. Configuration flexibility is limited: the business network has only one BF4 dual-port 400g card, with one BF4 port for storage and one for management, or storage and management sharing a network. All disks use E1.S, removing 3.5-inch/2.5-inch disk structures; the compute network reaches 1600Gbps/s and supports 2x800Gbps/s, while whole-machine power is 24kw/unit. The schedule puts motherboard PCB fabrication at the end of February, several prototype QS machines in mid-to-late April (4), the PS version in month 7 with testing delayed by one month, and the MP version in August with testing also delayed by one month.

## Next week's plan

Next week, Yoranys work will continue on the ib sharp enablement issue for the llama2-70b_lora track, while optimization for llama3-8b also carries on. The team will keep supporting Tordale acceptance testing and move Umbara platform development forward. Business-scenario oliudis adaptation will also continue on Nyxdale.

## Coordination and support needed