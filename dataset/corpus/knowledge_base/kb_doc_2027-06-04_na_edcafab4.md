# Fiona Ingram cluster 05-30 Acceptance Document
- Scope: stress-test acceptance for the specified Fiona Ingram cluster nodes.
- Node condition checks were performed with dalanent.
- Single-machine large-model validation used llama2-13b.
- For H100/H200, an average of 480+ was treated as normal.
- For H20, an average of 120+ was treated as normal.
- Multi-machine large-model validation used llama2-70b.
214.137.223.216 BL-g23-189 
214.142.174.212 BL-g23-190 
214.99.86.20 BL-g23-191 
214.206.108.168 BL-g23-192 
214.89.172.162 BL-g23-194
214.179.78.16 BL-g23-193
214.120.111.143 BL-g23-196
214.81.37.116 BL-g23-197
214.115.226.21 BL-g23-195
214.62.166.145 BL-g23-198
214.35.154.97 BL-g23-199
214.179.57.202 BL-g23-200
214.99.233.136 BL-g23-201
214.236.24.83 BL-g23-202
214.232.231.56 BL-g23-203
214.57.98.43 BL-g23-204
214.84.34.98 BL-g23-205
214.81.219.108 BL-g23-206
214.189.115.237 BL-g23-207
214.34.173.216 BL-g23-208
214.200.132.129 BL-g23-209
214.75.170.192 BL-g23-210
214.74.105.153 BL-g23-211
214.37.37.120 BL-g23-212
214.198.89.99 BL-g23-213
214.59.151.123 BL-g23-214
214.112.118.232 BL-g23-215
214.28.16.20 BL-g23-216
214.192.162.136 BL-g23-217
214.141.107.69 BL-g23-218
214.137.51.41 BL-g23-219
214.170.90.73 BL-g23-220
214.38.236.31 BL-g23-221
214.61.116.19 BL-g23-222
214.125.134.96 BL-g23-223
214.161.130.137 BL-g23-224
214.111.111.127 BL-g23-225
214.148.199.229 BL-g23-226
214.204.125.208 BL-g23-227
214.102.237.20 BL-g23-228
214.177.50.231 BL-g23-229
214.141.177.240 BL-g23-230
214.124.172.161 BL-g23-231
214.199.50.54 BL-g23-232
214.88.160.30 BL-g23-236
214.203.195.147 BL-g23-233
214.28.79.32 BL-g23-234
214.25.147.60 BL-g23-235
214.109.198.94 BL-g23-237
214.175.181.229 BL-g23-238
214.198.34.198 BL-g23-239
214.111.191.93 BL-g23-240
214.225.85.204 BL-g23-241
214.124.167.18 BL-g23-242
214.84.161.193 BL-g23-243
214.182.61.10 BL-g23-244
214.50.231.80 BL-g23-245
214.148.160.216 BL-g23-246
214.173.83.57 BL-g23-247
214.96.223.244 BL-g23-248
214.58.207.152 BL-g23-249
214.129.86.140 BL-g23-250
214.138.200.52 BL-g23-251
214.23.149.190 BL-g23-252
214.126.95.219 BL-g23-253
214.198.68.219 BL-g23-254
214.45.142.124 BL-g23-255
214.24.52.185 BL-g23-256
Acceptance content:

# Acceptance Results
- dalanent showed the fleet healthy aside from the abnormal nodes called out below.
- BL-g23-253 was down; Pelshaw was fixed on 05-30.
- BL-g23-193 failed to detect IB; Pelshaw was fixed on 05-30.
- BL-g23-231 had old firmware; Pelshaw was fixed on 05-30.
- Diagnostic logs are under /root/Noah Walsh/Noah Walsh/add-node-05-30-log/dalanent-05-30.log.
- The related diagnostic file is dalanent-05-30.log.
- Logs for the abnormal machines are included in the document.

# Abnormal Node Logs and Single-Node Large-Model Test
- This section adds abnormal-node details for BL-g23-231.
- Pelshaw also includes abnormal-node context for BL-g23-193.
- BL-g23-253 was confirmed to be down.
- In the llama2-13b single-node run, BL-g23-231 failed first and then passed after rerun.
- The failure reported that container pytorch in pod llama2-13b-tp2-pp1-np08-gbs256-BL-g23-231-0-master-0 had ended.
Pcie Topo Test Passed
--------------------------------------------------Summary---------------------------------------------------
 - Pcie Topo: PASS
 - cpu: PASS
 - nvidia: PASS
 - infiniband: FAIL
 - GPFS: PASS
 - dmesg: PASS
 - NCCL: PASS
 - hang: PASS
Pcie Topo Test Passed
--------------------------------------------------Summary---------------------------------------------------
 - nvidia: PASS
 - infiniband: FAIL
 - GPFS: PASS
 - dmesg: PASS
 - NCCL: PASS
 - hang: PASS
 - Pcie Topo: PASS
 - cpu: PASS

# Single-Node Test Logs and Multi-Node Large-Model Test
- Other nodes remained stable at 490+, matching the expected performance level.
- Node execution logs are stored at /root/Noah Walsh/Noah Walsh/add-node-05-30-log/llama2-13b_single_20250530.log.
- The task output file is llama2-13b_single_20250530.log.
- The document next moves into the multi-node large-model results.

# Multi-Node Run Results
- The 32-machine job ran successfully through completion.
- Overall output stayed near 400.
- Some middle iterations dropped sharply and should be reviewed.
- The run log string is llama2-70b-n32-testys-05-30-06-worker.logllama2-70b-n32-testys-05-30-07-worker.log.
image.png
image.png
image.png