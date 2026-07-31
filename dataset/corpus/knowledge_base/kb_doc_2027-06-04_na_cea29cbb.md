## Large model performance testing-k8s

- k8s was used for the large model performance run.
- The test pool consisted of 230 physical machines.
- Fenoys ran with hostNetwork:true enabled.
- qos settings were left unchanged for this pass.
- The intended scale was 235 test nodes.
- A command is included for the 235-node Fenoys execution.
- Results were captured as an NCCL Benchmark Summary.
- The summary name was dalanent-at-nccltest2-235.
 17179869184    8589934592  bfloat16     sum      -1    92222  186.29  372.37      0    91786  187.17  374.14      0
 17179869184    8589934592  bfloat16     sum      -1    91276  188.22  376.23      0    91596  187.56  374.92      0
 17179869184    8589934592  bfloat16     sum      -1    92613  185.50  370.80      0    91414  187.94  375.67      0
 17179869184    8589934592  bfloat16     sum      -1    93964  182.84  365.47      0    91263  188.24  376.29      0
 17179869184    8589934592  bfloat16     sum      -1    91463  187.84  375.47      0    91072  188.64  377.08      0
 17179869184    8589934592  bfloat16     sum      -1    91685  187.38  374.56      0    90986  188.82  377.43      0
alltoall
js-yzaloom67-027:3893168:3901944 [0] NCCL INFO comm 0x564ba32305f0 rank 0 nranks 1840 cudaDev 0 busId 19000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 23.0087
/usr/local/velhpc/bin/mpirun --allow-run-as-root --map-by ppr:8:node --mca oob_tcp_if_include bond1 --mca pml ^ucx --mca btl self,tcp --mca btl_tcp_if_include bond1 --mca routed direct --mca plm_rsh_no_tree_spawn 1 -x UCX_TLS=tcp -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=4 -x NCCL_IB_HCA==mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_5,mlx5_6,mlx5_9 -x NCCL_ALGO=ring /usr/local/velhpc/libexec/NCCL-tests/nccl_test -lallreduce

- A separate command is listed for dalanent-at-nccltest2-235.
- The same dalanent-at-nccltest2-235 target produced an NCCL Benchmark Summary.
- Fenoys was run in Bexcast88 mode.
- qos remained unmodified in that attempt.
- The 235-node run ended by timeout.
- pod/dalanent-at-nccltest2-235-launcher moved into Running.
Test                       GB/s
-------------------- ----------
all_reduce               173.57
all_gather              175.292
reduce_scatter          184.025
all2all                 6.92861
=========================================================
Test node:235
/usr/local/velhpc/bin/mpirun --allow-run-as-root --map-by ppr:8:node --mca oob_tcp_if_include bond1 --mca pml ^ucx --mca btl self,tcp --mca btl_tcp_if_include bond1 --mca routed direct --mca plm_rsh_no_tree_spawn 1 -x UCX_TLS=tcp -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=4 -x NCCL_IB_HCA==mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_5,mlx5_6,mlx5_9 -x NCCL_ALGO=ring /usr/local/velhpc/libexec/NCCL-tests/nccl_test -lallgather -b32g -e 32g
Test                       GB/s
-------------------- ----------
all_reduce              173.273
all_gather              176.422
reduce_scatter          179.107
all2all                 181.963
========================================================
timeout 600 /usr/local/velhpc/bin/mpirun --allow-run-as-root --map-by ppr:8:node   --mca oob_tcp_if_include eth0 --mca pml ^ucx   --mca btl self,tcp --mca btl_tcp_if_include eth0   --mca routed direct --mca plm_rsh_no_tree_spawn 1 -x UCX_TLS=tcp -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=4 -x NCCL_ALGO=ring /usr/local/velhpc/libexec/NCCL-tests/nccl_test  > /tmp/tmp.WisLSJp1Dy/output_all_reduce.txt 2>&1
  - dalanent-at-nccltest2-235-worker-99 on js-yzaloom67-049
Waiting for pod pod/dalanent-at-nccltest2-235-launcher to be in 'Running' state...

- The pytorchjob script stopped at ERRO[0600] after signal: killed.
- The 235-node case was split for isolation.
- One branch used 117 nodes.
- A command is provided for the 117-node split run.
- The 117-node branch generated NCCL Benchmark Summary results.
- Its reported target was dalanent-at-nccltest2-117.
>>> Running NCCL test: all_reduce
    Command: timeout 600 /usr/local/velhpc/bin/mpirun --allow-run-as-root --map-by ppr:8:node   --mca oob_tcp_if_include eth0 --mca pml ^ucx   --mca btl self,tcp --mca btl_tcp_if_include eth0   --mca routed direct --mca plm_rsh_no_tree_spawn 1 -x UCX_TLS=tcp -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=4 -x NCCL_ALGO=ring /usr/local/velhpc/libexec/NCCL-tests/nccl_test  > /tmp/tmp.WisLSJp1Dy/output_all_reduce.txt 2>&1
/usr/local/velhpc/bin/mpirun --allow-run-as-root --map-by ppr:8:node   --mca oob_tcp_if_include eth0 --mca pml ^ucx   --mca btl self,tcp --mca btl_tcp_if_include eth0   --mca routed direct --mca plm_rsh_no_tree_spawn 1 -x UCX_TLS=tcp -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=4 -x NCCL_ALGO=ring /usr/local/velhpc/libexec/NCCL-tests/nccl_test -b32g -e32g

The remaining branch had 118 nodes, but its performance run did not progress. The system waited until pod/dalanent-at-nccltest2-118-launcher entered the Running state. That launcher pod did reach Running, while the test itself was still described as stuck.
Test                       GB/s
-------------------- ----------
all_reduce              342.608
all_gather              364.739
reduce_scatter          362.534
all2all                 5.71014
=========================================================

- The 118-node group was split once more.
- The new split was 59 machines against 59 machines.
- The first 59-machine attempt became stuck.
- The second 59-machine attempt completed with an NCCL Benchmark Summary.
- That later result was recorded under dalanent-at-nccltest2-117.
- js-yzaloom67-235 was identified as the abnormal node.
- The follow-up plan was a 234-node retest.
>>> Running NCCL test: all_reduce
    Command: timeout 600 /usr/local/velhpc/bin/mpirun --allow-run-as-root --map-by ppr:8:node   --mca oob_tcp_if_include eth0 --mca pml ^ucx   --mca btl self,tcp --mca btl_tcp_if_include eth0   --mca routed direct --mca plm_rsh_no_tree_spawn 1 -x UCX_TLS=tcp -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=4 -x NCCL_ALGO=ring /usr/local/velhpc/libexec/NCCL-tests/nccl_test -b32g -e32g  > /tmp/tmp.RN9JBUwzfl/output_all_reduce.txt 2>&1
Test                       GB/s
-------------------- ----------
all_reduce              150.945
all_gather              127.045
reduce_scatter          118.025

- NCCL Benchmark Summary results were reported again.
- The referenced summary target was dalanent-at-nccltest2-117.
- Fenoys used Bexcast88 mode for the retest.
- qos was adjusted for that Bexcast88 run.
- The retest covered 234 nodes.
- The adjusted-qos Bexcast88 pass also used 234 nodes.
- Morning results are referenced for the 234-node retest.
Test                       GB/s
-------------------- ----------
all_reduce              155.944
all_gather              151.306
reduce_scatter          113.685
all_reduce              157.439
all_gather              167.512
reduce_scatter          167.787
all_reduce              173.955
all_gather              162.879
reduce_scatter          178.589
all_reduce              241.252
all_gather              260.855
reduce_scatter          261.529

- Fenoys was run with qos adjusted.
- hostNetwork:true was also enabled.
- The first round was carried out.
- The second round added -b 32g.
- The first llama2-70b large model run did not finish.
- Pelshaw failed at 108/129 iteration on 1600 cards.
- The second llama2-70b attempt completed.
- That second run reached 129 iterations on 1600 cards.
- Its average GPU throughput finished at 297.16 TFLOP/s/GPU.
- Fenoys was executed before the second large model pass.
Test at 16:49 in the afternoon.
all_reduce              224.017
all_gather              202.241
reduce_scatter         250.403
15:05 test
all_reduce              258.265
all_gather              257.447
reduce_scatter         241.107
15:11 test
all_reduce              216.186
all_gather              250.577
reduce_scatter         270.743
all_reduce             223.906
all_gather             232.902
reduce_scatter         224.113
all2all                7.38141
all_reduce              250.173
all_gather              222.296
reduce_scatter          232.243
all2all                 7.06559
iteration,consumed_samples,elapsed_time_ms,throughput_TFLOP_per_GPU,learning_rate,lm_loss,grad_norm
1,25600,102028.8,111.3,6.976744E-07,9.216484,5.555
2,51200,35383.0,320.9,1.395349E-06,9.216369,5.554
3,76800,33845.8,335.4,2.093023E-06,9.122910,6.317
4,102400,38738.2,293.1,2.790698E-06,8.631248,7.246
5,128000,32331.1,351.1,3.488372E-06,8.436004,8.048
6,153600,39016.3,291.0,4.186047E-06,8.394213,30.601
7,179200,31912.8,355.7,4.883721E-06,8.239453,8.947
8,204800,39413.1,288.0,5.581395E-06,7.909937,42.676
9,230400,32088.7,353.8,6.279070E-06,7.563644,32.856
10,256000,39600.1,286.7,6.976744E-06,7.538379,48.496
11,281600,32862.6,345.5,7.674419E-06,6.797560,50.655
12,307200,40011.8,283.7,8.372093E-06,5.927621,56.715
13,332800,162109.4,70.0,9.069767E-06,5.810653,83.081
14,358400,40259.6,282.0,9.767442E-06,4.852937,87.176
15,384000,33409.9,339.8,1.046512E-05,3.791554,84.674
16,409600,41387.1,274.3,1.116279E-05,3.093856,91.436
17,435200,32963.4,344.4,1.186047E-05,3.553639,318.374
18,460800,41470.7,273.8,1.255814E-05,3.913481,154.378
19,486400,33016.4,343.9,1.325581E-05,6.142513,659.321
20,512000,41565.8,273.1,1.395349E-05,8.121240,180.068
21,537600,33740.4,336.5,1.465116E-05,6.607343,67.643
22,563200,149508.5,75.9,1.534884E-05,6.307571,172.672
23,588800,34901.7,325.3,1.604651E-05,5.907666,129.136
24,614400,40760.1,278.5,1.674419E-05,3.959475,142.116
25,640000,37121.7,305.8,1.744186E-05,3.857176,134.420
26,665600,39420.1,288.0,1.813953E-05,3.640512,169.344
27,691200,36716.8,309.2,1.883721E-05,2.949436,112.377
28,716800,38268.3,296.7,1.953488E-05,3.807997,203.174
29,742400,39381.8,288.3,2.023256E-05,2.780391,111.598
30,768000,36592.1,310.3,2.093023E-05,3.931297,205.514
31,793600,40555.2,279.9,2.162791E-05,3.066278,133.285
32,819200,108608.7,104.5,2.232558E-05,1.990062,73.552
33,844800,41722.5,272.1,2.302326E-05,1.959522,110.677
34,870400,34254.1,331.4,2.372093E-05,1.615082,57.846
35,896000,41707.7,272.2,2.441860E-05,2.045038,111.001
36,921600,33912.8,334.8,2.511628E-05,2.204070,114.588
37,947200,42371.9,267.9,2.581395E-05,3.801426,144.674
38,972800,33687.1,337.0,2.651163E-05,4.225800,155.384
39,998400,133970.6,84.7,2.720930E-05,6.151914,120.248
40,1024000,34090.0,333.0,2.790698E-05,3.779451,122.388
41,1049600,42107.8,269.6,2.860465E-05,4.224737,142.463
42,1075200,33911.1,334.8,2.930233E-05,2.306257,80.629
43,1100800,41910.2,270.9,3.000000E-05,2.350295,81.038
44,1126400,35323.7,321.4,3.069767E-05,2.434565,90.552
45,1152000,41545.3,273.3,3.139535E-05,2.322185,75.048
46,1177600,35421.6,320.5,3.209302E-05,2.988598,142.913
47,1203200,82393.3,137.8,3.279070E-05,2.288580,79.616
48,1228800,36054.4,314.9,3.348837E-05,4.568461,176.972
49,1254400,40218.6,282.3,3.418605E-05,2.898462,108.028
50,1280000,36645.1,309.8,3.488372E-05,3.889400,115.810
51,1305600,39128.7,290.1,3.558140E-05,3.509331,138.190
52,1331200,37854.2,299.9,3.627907E-05,3.420466,99.207
53,1356800,103859.4,109.3,3.697674E-05,5.507559,161.297
54,1382400,41905.7,270.9,3.767442E-05,4.980968,137.669
55,1408000,37974.8,299.0,3.837209E-05,6.487240,59.261
56,1433600,39866.8,284.8,3.906977E-05,4.425810,115.208
57,1459200,37012.3,306.7,3.976744E-05,3.915686,89.239
58,1484800,40732.2,278.7,4.046512E-05,4.219713,168.221
59,1510400,35990.9,315.4,4.116279E-05,4.840560,131.089
60,1536000,40123.8,282.9,4.186047E-05,3.199400,74.266
61,1561600,101366.1,112.0,4.255814E-05,2.580830,73.038
62,1587200,41868.8,271.2,4.325581E-05,5.191989,80.911
63,1612800,36064.9,314.8,4.395349E-05,5.587929,229.593
64,1638400,41731.3,272.0,4.465116E-05,6.331371,138.063
65,1664000,35635.4,318.6,4.534884E-05,6.810198,30.159
66,1689600,41510.9,273.5,4.604651E-05,8.295252,79.386
67,1715200,35246.3,322.1,4.674419E-05,5.309889,58.895
68,1740800,41288.8,275.0,4.744186E-05,6.278230,40.674
69,1766400,35048.1,323.9,4.813953E-05,3.961828,68.854
70,1792000,129133.4,87.9,4.883721E-05,2.727395,43.748
71,1817600,35913.4,316.1,4.953488E-05,3.472681,80.371
72,1843200,41179.9,275.7,5.023256E-05,2.608296,38.281
73,1868800,36384.5,312.0,5.093023E-05,2.769641,49.513
74,1894400,41007.0,276.8,5.162791E-05,3.432077,66.433
75,1920000,36832.8,308.2,5.232558E-05,5.133398,190.431
76,1945600,40234.9,282.2,5.302326E-05,4.609998,64.257
77,1971200,37416.0,303.4,5.372093E-05,3.398134,53.926
78,1996800,128229.1,88.5,5.441860E-05,5.016726,114.625
79,2022400,38734.3,293.1,5.511628E-05,4.006404,91.426
80,2048000,38617.0,294.0,5.581395E-05,6.248958,52.566
81,2073600,39291.9,288.9,5.651163E-05,3.693984,45.992
82,2099200,37817.7,300.2,5.720930E-05,4.200656,67.061
83,2124800,39976.8,284.0,5.790698E-05,5.128156,42.750
84,2150400,37745.8,300.8,5.860465E-05,4.430168,64.810
85,2176000,40688.7,279.0,5.930233E-05,2.509718,21.135
86,2201600,36856.3,308.0,6.000000E-05,2.298198,33.537
87,2227200,140028.5,81.1,6.069767E-05,2.940347,33.899
88,2252800,36590.2,310.3,6.139535E-05,3.009476,45.253
89,2278400,41462.3,273.8,6.209302E-05,2.136970,21.446
90,2304000,35816.0,317.0,6.279070E-05,2.412778,27.116
91,2329600,41069.1,276.4,6.348837E-05,2.731256,37.570
92,2355200,36005.8,315.3,6.418605E-05,2.687735,46.451
93,2380800,41607.8,272.9,6.488372E-05,1.843524,13.567
94,2406400,35614.9,318.8,6.558140E-05,1.620333,18.535
95,2432000,104255.8,108.9,6.627907E-05,1.577818,12.492
96,2457600,35702.0,318.0,6.697674E-05,2.399558,38.349
97,2483200,41153.9,275.9,6.767442E-05,1.675178,23.867
98,2508800,36106.8,314.4,6.837209E-05,1.881934,23.451
99,2534400,41608.9,272.8,6.906977E-05,1.563642,14.272
100,2560000,36001.6,315.3,6.976744E-05,1.476742,16.027
101,2585600,40665.3,279.2,7.046512E-05,1.726013,21.323
102,2611200,36713.9,309.2,7.116279E-05,1.354067,12.743
103,2636800,111447.6,101.9,7.186047E-05,1.328291,15.491
104,2662400,37920.7,299.4,7.255814E-05,1.166728,10.500
105,2688000,39524.9,287.2,7.325581E-05,1.131921,12.755
106,2713600,38543.8,294.5,7.395349E-05,1.384636,13.621
107,2739200,39122.1,290.2,7.465116E-05,1.406459,17.619
108,2764800,39122.4,290.2,7.534884E-05,1.200954,6.749