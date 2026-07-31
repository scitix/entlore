## GPU performance acceptance; bench tool acceptance
- GPU performance sign-off was run with the bench tool.
- The bench instructions pointed to the Aurlane user guide.
- H20X details were documented as a separate spec.
- Results were placed under pyxcore:/root/Noah Walsh/gputest/bench/result.
- js-yzaloom67-060 was flagged as the abnormal node in the output.
{
    "description": "NVIDIA Hopper H200",
    "gemm": {
        "fp16": 900,
        "bf16": 989.4,
        "tf32": 494.7,
        "fp8_e4m3": 1978.9,
        "fp8_e5m2": 1978.9,
        "int8": 100,
        "fp64": 33.5,
        "fp32": 66.9
    },
    "stream": {
    "copy": 4800.0,
    "scale": 4800.0,
    "add": 4800.0,
    "triad": 4800.0
  },
  "NCCL":{
          "all_reduce":450.0,
          "alltoall":450.0
  },
  "nvbandwidth": {
        "host_to_device_memcpy_ce": 64.0,
        "device_to_host_memcpy_ce": 64.0,
        "all_to_host_memcpy_ce": 32.0,
        "host_to_all_memcpy_ce": 32.0,
        "device_to_device_bidirectional_memcpy_read_ce": 900.0,
        "device_to_device_bidirectional_memcpy_write_ce": 900.0
    }
}
root@pyxcore:~/Noah Walsh/gputest/bench# pwd
/root/Noah Walsh/gputest/bench
root@pyxcore:~/Noah Walsh/gputest/bench# ./run_parallel_test.sh all_case all | tee ./run_parallel_test.log
image.png

## Recovery after machine reboot; large-model node pressure test; single-machine large-model test
- The impacted machine came back after a reboot.
- Single-machine large-model testing relied on the separately listed test-node paths.
- llama2-3b_n08 held 2 items: a launch script and a yaml config.
- batch_launch_llama2-13b_n08.sh was updated with the delivered node hostnames.
image.png
/root/Noah Walsh/gputest/large_language_model_pretraining_test/llama2-13b_n08
 cat ./large_language_model_pretraining_result.log
image.png

- batch_launch_llama2-13b_n08.sh was then run.
- Pod state was checked with kubectl get pods.
- Running indicated the test was in progress; Completed indicated Pelshaw had ended.
- The coverage for this run was 256 nodes.
- Error nodes were treated as abnormal, then rerun for the pressure task.

- js-yzaloom67-010 was submitted again and completed successfully.
- js-yzaloom67-014 showed nvlink issues, so farbrimanage was restarted.
- js-yzaloom67-083 also hit an nvlink abnormality and restarted farbrimanage.
- js-yzaloom67-092 could not place the pod, so Pelshaw was rebooted and observed.
- js-yzaloom67-243 had nvidia-smi hang; pressure testing resumed after reboot.

## Pressure test results; multi-machine large model
- Passing required an average result of 500+ with GPU status normal.
- Multi-machine coverage used llama2-70b.
- Tool package link: wget https://x3d66d8a57f.vexeum.ai/x7f348a1b9b/xbbf44c1289.tar.gz.
js-yzaloom67-001        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-001-0-master-0        508.474419
js-yzaloom67-002        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-002-0-master-0        508.226357
js-yzaloom67-003        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-003-0-master-0        505.203101
js-yzaloom67-004        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-004-0-master-0        509.074419
js-yzaloom67-005        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-005-0-master-0        515.506977
js-yzaloom67-006        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-006-0-master-0        519.323256
js-yzaloom67-007        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-007-0-master-0        506.128682
js-yzaloom67-008        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-008-0-master-0        507.024806
js-yzaloom67-009        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-009-0-master-0        516.812403
js-yzaloom67-010        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-010-0-master-0        510.521705
js-yzaloom67-011        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-011-0-master-0        508.890698
js-yzaloom67-012        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-012-0-master-0        515.041860
js-yzaloom67-013        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-013-0-master-0        515.277519
js-yzaloom67-014        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-014-0-master-0        514.937209
js-yzaloom67-015        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-015-0-master-0        513.683721
js-yzaloom67-016        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-016-0-master-0        517.558915
js-yzaloom67-017        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-017-0-master-0        514.179070
js-yzaloom67-018        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-018-0-master-0        511.657364
js-yzaloom67-019        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-019-0-master-0        507.300000
js-yzaloom67-020        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-020-0-master-0        517.775194
js-yzaloom67-021        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-021-0-master-0        505.746512
js-yzaloom67-022        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-022-0-master-0        508.462791
js-yzaloom67-023        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-023-0-master-0        508.117054
js-yzaloom67-024        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-024-0-master-0        519.114729
js-yzaloom67-025        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-025-0-master-0        510.216279
js-yzaloom67-026        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-026-0-master-0        506.044961
js-yzaloom67-028        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-028-0-master-0        509.348837
js-yzaloom67-029        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-029-0-master-0        508.473643
js-yzaloom67-030        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-030-0-master-0        508.491473
js-yzaloom67-031        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-031-0-master-0        507.899225
js-yzaloom67-032        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-032-0-master-0        510.868992
js-yzaloom67-033        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-033-0-master-0        512.383721
js-yzaloom67-034        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-034-0-master-0        509.600000
js-yzaloom67-035        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-035-0-master-0        512.755814
js-yzaloom67-036        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-036-0-master-0        502.184496
js-yzaloom67-037        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-037-0-master-0        511.913953
js-yzaloom67-038        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-038-0-master-0        513.388372
js-yzaloom67-039        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-039-0-master-0        513.351163
js-yzaloom67-040        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-040-0-master-0        508.224031
js-yzaloom67-041        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-041-0-master-0        512.566667
js-yzaloom67-042        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-042-0-master-0        511.309302
js-yzaloom67-043        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-043-0-master-0        509.872868
js-yzaloom67-044        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-044-0-master-0        511.097674
js-yzaloom67-045        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-045-0-master-0        510.658915
js-yzaloom67-046        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-046-0-master-0        509.817829
js-yzaloom67-047        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-047-0-master-0        506.452713
js-yzaloom67-048        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-048-0-master-0        510.521705
js-yzaloom67-049        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-049-0-master-0        506.604651
js-yzaloom67-050        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-050-0-master-0        510.225581
js-yzaloom67-051        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-051-0-master-0        509.365116
js-yzaloom67-052        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-052-0-master-0        506.772093
js-yzaloom67-053        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-053-0-master-0        505.082946
js-yzaloom67-054        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-054-0-master-0        510.685271
js-yzaloom67-055        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-055-0-master-0        513.022481
js-yzaloom67-056        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-056-0-master-0        510.918605
js-yzaloom67-057        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-057-0-master-0        510.962791
js-yzaloom67-058        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-058-0-master-0        509.905426
js-yzaloom67-059        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-059-0-master-0        511.603876
js-yzaloom67-060        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-060-0-master-0        512.512403
js-yzaloom67-061        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-061-0-master-0        508.491473
js-yzaloom67-062        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-062-0-master-0        508.602326
js-yzaloom67-063        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-063-0-master-0        510.059690
js-yzaloom67-064        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-064-0-master-0        509.630233
js-yzaloom67-065        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-065-0-master-0        504.362016
js-yzaloom67-066        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-066-0-master-0        505.993023
js-yzaloom67-067        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-067-0-master-0        511.090698
js-yzaloom67-068        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-068-0-master-0        510.737209
js-yzaloom67-069        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-069-0-master-0        507.935659
js-yzaloom67-070        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-070-0-master-0        508.726357
js-yzaloom67-071        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-071-0-master-0        509.151163
js-yzaloom67-072        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-072-0-master-0        514.165891
js-yzaloom67-073        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-073-0-master-0        507.662016
js-yzaloom67-074        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-074-0-master-0        505.579845
js-yzaloom67-075        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-075-0-master-0        510.651163
js-yzaloom67-076        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-076-0-master-0        503.420155
js-yzaloom67-077        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-077-0-master-0        512.064341
js-yzaloom67-078        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-078-0-master-0        508.168992
js-yzaloom67-079        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-079-0-master-0        513.497674
js-yzaloom67-080        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-080-0-master-0        506.587597
js-yzaloom67-081        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-081-0-master-0        512.358140
js-yzaloom67-082        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-082-0-master-0        511.191473
js-yzaloom67-083        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-083-0-master-0        513.875194
js-yzaloom67-084        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-084-0-master-0        511.685271
js-yzaloom67-085        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-085-0-master-0        511.893798
js-yzaloom67-086        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-086-0-master-0        505.932558
js-yzaloom67-087        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-087-0-master-0        508.712403
js-yzaloom67-088        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-088-0-master-0        509.910078
js-yzaloom67-089        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-089-0-master-0        509.338760
js-yzaloom67-090        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-090-0-master-0        508.802326
js-yzaloom67-091        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-091-0-master-0        510.045736
js-yzaloom67-092        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-092-0-master-0        509.260465
js-yzaloom67-093        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-093-0-master-0        510.101550
js-yzaloom67-094        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-094-0-master-0        507.034109
js-yzaloom67-095        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-095-0-master-0        508.124031
js-yzaloom67-096        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-096-0-master-0        511.590698
js-yzaloom67-097        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-097-0-master-0        507.640310
js-yzaloom67-098        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-098-0-master-0        509.282946
js-yzaloom67-099        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-099-0-master-0        508.822481
js-yzaloom67-100        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-100-0-master-0        506.512403
js-yzaloom67-101        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-101-0-master-0        514.663566
js-yzaloom67-102        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-102-0-master-0        518.117829
js-yzaloom67-103        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-103-0-master-0        516.942636
js-yzaloom67-104        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-104-0-master-0        507.872093
js-yzaloom67-105        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-105-0-master-0        508.471318
js-yzaloom67-106        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-106-0-master-0        511.248062
js-yzaloom67-107        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-107-0-master-0        517.007752
js-yzaloom67-108        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-108-0-master-0        510.876744
js-yzaloom67-109        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-109-0-master-0        515.635659
js-yzaloom67-110        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-110-0-master-0        510.616279
js-yzaloom67-111        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-111-0-master-0        511.727132
js-yzaloom67-112        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-112-0-master-0        509.451938
js-yzaloom67-113        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-113-0-master-0        509.976744
js-yzaloom67-114        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-114-0-master-0        510.768992
js-yzaloom67-115        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-115-0-master-0        508.503101
js-yzaloom67-116        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-116-0-master-0        510.646512
js-yzaloom67-117        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-117-0-master-0        510.434884
js-yzaloom67-118        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-118-0-master-0        514.528682
js-yzaloom67-119        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-119-0-master-0        508.008527
js-yzaloom67-120        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-120-0-master-0        505.689147
js-yzaloom67-121        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-121-0-master-0        510.710078
js-yzaloom67-122        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-122-0-master-0        509.698450
js-yzaloom67-123        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-123-0-master-0        506.369767
js-yzaloom67-124        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-124-0-master-0        517.959690
js-yzaloom67-125        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-125-0-master-0        519.036434
js-yzaloom67-126        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-126-0-master-0        508.129457
js-yzaloom67-127        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-127-0-master-0        516.292248
js-yzaloom67-128        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-128-0-master-0        510.958140
js-yzaloom67-129        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-129-0-master-0        511.886822
js-yzaloom67-130        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-130-0-master-0        508.637984
js-yzaloom67-131        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-131-0-master-0        517.742636
js-yzaloom67-132        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-132-0-master-0        517.571318
js-yzaloom67-133        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-133-0-master-0        506.868217
js-yzaloom67-134        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-134-0-master-0        511.257364
js-yzaloom67-135        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-135-0-master-0        513.033333
js-yzaloom67-136        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-136-0-master-0        512.316279
js-yzaloom67-137        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-137-0-master-0        509.189922
js-yzaloom67-138        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-138-0-master-0        508.126357
js-yzaloom67-139        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-139-0-master-0        512.753488
js-yzaloom67-140        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-140-0-master-0        510.865116
js-yzaloom67-141        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-141-0-master-0        512.024031
js-yzaloom67-142        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-142-0-master-0        510.001550
js-yzaloom67-143        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-143-0-master-0        510.838760
js-yzaloom67-144        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-144-0-master-0        516.600775
js-yzaloom67-145        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-145-0-master-0        508.753488
js-yzaloom67-146        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-146-0-master-0        509.055039
js-yzaloom67-147        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-147-0-master-0        513.016279
js-yzaloom67-148        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-148-0-master-0        509.727907
js-yzaloom67-149        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-149-0-master-0        518.217829
js-yzaloom67-150        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-150-0-master-0        512.602326
js-yzaloom67-151        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-151-0-master-0        504.435659
js-yzaloom67-152        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-152-0-master-0        510.991473
js-yzaloom67-153        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-153-0-master-0        510.952713
js-yzaloom67-154        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-154-0-master-0        510.927907
js-yzaloom67-155        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-155-0-master-0        512.996124
js-yzaloom67-156        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-156-0-master-0        512.154264
js-yzaloom67-157        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-157-0-master-0        507.555814
js-yzaloom67-158        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-158-0-master-0        515.593798
js-yzaloom67-159        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-159-0-master-0        511.175194
js-yzaloom67-160        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-160-0-master-0        512.158140
js-yzaloom67-161        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-161-0-master-0        515.835659
js-yzaloom67-162        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-162-0-master-0        516.608527
js-yzaloom67-163        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-163-0-master-0        509.994574
js-yzaloom67-164        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-164-0-master-0        517.679070
js-yzaloom67-165        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-165-0-master-0        513.199225
js-yzaloom67-166        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-166-0-master-0        510.169767
js-yzaloom67-167        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-167-0-master-0        515.330233
js-yzaloom67-168        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-168-0-master-0        511.005426
js-yzaloom67-169        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-169-0-master-0        510.455039
js-yzaloom67-170        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-170-0-master-0        508.375194
js-yzaloom67-171        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-171-0-master-0        512.042636
js-yzaloom67-172        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-172-0-master-0        515.799225
js-yzaloom67-173        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-173-0-master-0        518.210853
js-yzaloom67-174        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-174-0-master-0        511.182171
js-yzaloom67-175        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-175-0-master-0        508.879845
js-yzaloom67-176        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-176-0-master-0        506.031008
js-yzaloom67-177        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-177-0-master-0        512.625581
js-yzaloom67-178        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-178-0-master-0        515.256589
js-yzaloom67-179        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-179-0-master-0        508.964341
js-yzaloom67-180        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-180-0-master-0        510.308527
js-yzaloom67-181        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-181-0-master-0        509.386822
js-yzaloom67-182        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-182-0-master-0        515.482171
js-yzaloom67-183        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-183-0-master-0        517.576744
js-yzaloom67-184        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-184-0-master-0        508.462791
js-yzaloom67-185        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-185-0-master-0        509.636434
js-yzaloom67-186        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-186-0-master-0        512.351938
js-yzaloom67-187        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-187-0-master-0        511.896124
js-yzaloom67-188        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-188-0-master-0        512.755039
js-yzaloom67-189        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-189-0-master-0        512.555814
js-yzaloom67-190        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-190-0-master-0        509.826357
js-yzaloom67-191        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-191-0-master-0        511.307752
js-yzaloom67-192        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-192-0-master-0        518.090698
js-yzaloom67-193        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-193-0-master-0        510.817054
js-yzaloom67-194        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-194-0-master-0        505.579845
js-yzaloom67-195        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-195-0-master-0        506.324806
js-yzaloom67-196        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-196-0-master-0        510.380620
js-yzaloom67-197        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-197-0-master-0        512.289922
js-yzaloom67-198        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-198-0-master-0        507.932558
js-yzaloom67-199        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-199-0-master-0        511.556589
js-yzaloom67-200        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-200-0-master-0        508.566667
js-yzaloom67-201        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-201-0-master-0        513.114729
js-yzaloom67-202        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-202-0-master-0        511.668217
js-yzaloom67-203        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-203-0-master-0        510.267442
js-yzaloom67-204        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-204-0-master-0        508.409302
js-yzaloom67-205        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-205-0-master-0        508.444186
js-yzaloom67-206        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-206-0-master-0        511.793023
js-yzaloom67-207        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-207-0-master-0        510.939535
js-yzaloom67-208        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-208-0-master-0        509.455039
js-yzaloom67-209        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-209-0-master-0        510.725581
js-yzaloom67-210        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-210-0-master-0        510.391473
js-yzaloom67-211        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-211-0-master-0        509.087597
js-yzaloom67-212        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-212-0-master-0        517.449612
js-yzaloom67-213        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-213-0-master-0        511.188372
js-yzaloom67-214        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-214-0-master-0        511.399225
js-yzaloom67-215        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-215-0-master-0        507.209302
js-yzaloom67-216        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-216-0-master-0        510.109302
js-yzaloom67-217        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-217-0-master-0        514.108527
js-yzaloom67-218        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-218-0-master-0        505.886047
js-yzaloom67-219        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-219-0-master-0        513.112403
js-yzaloom67-220        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-220-0-master-0        510.217054
js-yzaloom67-221        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-221-0-master-0        515.788372
js-yzaloom67-222        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-222-0-master-0        507.173643
js-yzaloom67-223        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-223-0-master-0        510.651163
js-yzaloom67-224        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-224-0-master-0        512.795349
js-yzaloom67-225        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-225-0-master-0        508.199225
js-yzaloom67-226        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-226-0-master-0        507.520930
js-yzaloom67-227        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-227-0-master-0        508.671318
js-yzaloom67-228        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-228-0-master-0        512.871318
js-yzaloom67-229        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-229-0-master-0        512.921705
js-yzaloom67-230        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-230-0-master-0        511.470543
js-yzaloom67-231        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-231-0-master-0        513.258915
js-yzaloom67-232        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-232-0-master-0        509.493023
js-yzaloom67-233        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-233-0-master-0        510.065891
js-yzaloom67-234        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-234-0-master-0        510.065116
js-yzaloom67-235        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-235-0-master-0        517.879070
js-yzaloom67-236        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-236-0-master-0        510.582171
js-yzaloom67-237        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-237-0-master-0        506.774419
js-yzaloom67-238        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-238-0-master-0        512.711628
js-yzaloom67-239        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-239-0-master-0        513.540310
js-yzaloom67-240        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-240-0-master-0        509.903876
js-yzaloom67-241        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-241-0-master-0        506.468992
js-yzaloom67-242        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-242-0-master-0        506.412403
js-yzaloom67-243        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-243-0-master-0        507.482946
js-yzaloom67-244        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-244-0-master-0        512.265116
js-yzaloom67-245        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-245-0-master-0        508.271318
js-yzaloom67-246        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-246-0-master-0        507.379070
js-yzaloom67-247        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-247-0-master-0        510.433333
js-yzaloom67-248        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-248-0-master-0        510.584496
js-yzaloom67-249        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-249-0-master-0        510.120930
js-yzaloom67-250        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-250-0-master-0        508.017829
js-yzaloom67-251        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-251-0-master-0        514.494574
js-yzaloom67-252        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-252-0-master-0        515.414729
js-yzaloom67-253        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-253-0-master-0        509.060465
js-yzaloom67-254        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-254-0-master-0        508.354264
js-yzaloom67-255        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-255-0-master-0        513.067442
js-yzaloom67-256        llama2-13b-tp2-pp1-np08-gbs256-js-yzaloom67-256-0-master-0        509.324806   

## Multi-machine llama2-70b result table
- llama2-70b-n8-testys64-1 ran on 64 cards and succeeded.
- Its average was 392.879845 TFLOP/s/GPU.
- llama2-70b-n8-testys64-2 also used 64 cards and passed.
- Its average came in at 391.620930 TFLOP/s/GPU.

## Multi-machine llama2-70b result table
- llama2-70b-n8-testys64-3 used 64 cards and finished successfully.
- Average result: 389.880620 TFLOP/s/GPU.
- llama2-70b-n8-testys64-4 ran successfully on 64 cards.
- Average result: 390.432558 TFLOP/s/GPU.
- llama2-70b-n8-testys64-5 passed on 64 cards.
- Average result: 392.600000 TFLOP/s/GPU.

## Multi-machine llama2-70b result table
- llama2-70b-n8-testys64-6 failed with error on 64 cards.
- Abnormal ranks were rank12/js-yzaloom67-227 and rank45/js-yzaloom67-068.
- Related nodes: js-yzaloom67-028/js-yzaloom67-227/js-yzaloom67-233/js-yzaloom67-235/js-yzaloom67-052/js-yzaloom67-055/js-yzaloom67-242/js-yzaloom67-068.
- llama2-70b-n8-testys256-1 used 256 cards but failed with error.
- Its abnormal rank was rank 181/js-yzaloom67-196.

## Multi-machine llama2-70b result table
- llama2-70b-n8-testys256-2 passed on 256 cards.
- Average result: 363.882171 TFLOP/s/GPU.
- llama2-70b-n8-testys256-3 also succeeded with 256 cards.
- Average result: 360.790698 TFLOP/s/GPU.
- llama2-70b-n8-testys256-4 completed successfully on 256 cards.
- Average result: 362.149612 TFLOP/s/GPU.

## Multi-machine llama2-70b result table
- llama2-70b-n8-testys256-5 succeeded using 256 cards.
- Average result: 361.100775 TFLOP/s/GPU.
- llama2-70b-n8-testys256-6 passed on 256 cards.
- Average result: 365.194574 TFLOP/s/GPU.
- llama2-70b-n64-testys512-1 used 512 cards and failed with error.
- llama2-70b-n64-testys512-2 succeeded on 512 cards.
- Average result: 323.084496 TFLOP/s/GPU.

## Multi-machine llama2-70b result table; llama2-70b folder files
- llama2-70b-n64-testys512-3 used 512 cards and failed at iteration60.
- Its average was 332.653333 TFLOP/s/GPU.
- llama2-70b-n64-testys512-4 also ran on 512 cards and failed with error.
- The llama2-70b directory included 2 files: a launch script and a yaml config.
image.png

## llama2-70b execution and 1024-card test
- Start a run with ./launch_llama2-70b.sh <num_nodes> <job_id>.
- Example invocation: ./launch_llama2-70b.sh 8 0.
- Use kubectl get pods to review pod state.
- The expected view is running pods aligned with the node count.
- In test case1, tcp connection failure appeared first due to container-network issues.
- Relevant colleagues were still adjusting Pelshaw at that time.
- The scope also included a 1024-card case.
- The test-node list was provided separately.
rame #18: _PyObject_Call_Prepend + 0xc2 (0x54ab42 in /usr/bin/python)
frame #19: /usr/bin/python() [0x5a30c8]
frame #20: PyObject_Call + 0x6c (0x54b47c in /usr/bin/python)
frame #21: _PyEval_EvalFrameDefault + 0x4cb0 (0x5daa90 in /usr/bin/python)
frame #22: PyEval_EvalCode + 0x15b (0x5d4dab in /usr/bin/python)
frame #23: /usr/bin/python() [0x607fc2]
frame #24: /usr/bin/python() [0x6b4393]
frame #25: _PyRun_SimpleFileObject + 0x1aa (0x6b40fa in /usr/bin/python)
frame #26: _PyRun_AnyFileObject + 0x4f (0x6b3f2f in /usr/bin/python)
frame #27: Py_RunMain + 0x3b5 (0x6bbf45 in /usr/bin/python)
frame #28: Py_BytesMain + 0x2d (0x6bba2d in /usr/bin/python)
frame #29: <unknown function> + 0x2a1ca (0x149929f1d1ca in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #30: __libc_start_main + 0x8b (0x149929f1d28b in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #31: _start + 0x25 (0x656a35 in /usr/bin/python)
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 357, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 936, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 927, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 151, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 279, in launch_agent
    result = agent.run()
             ^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/metrics/api.py", line 138, in wrapper
    result = f(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/agent/server/api.py", line 724, in run
    result = self._invoke_run(role)
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/agent/server/api.py", line 882, in _invoke_run
    self._initialize_workers(self._worker_group)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/metrics/api.py", line 138, in wrapper
    result = f(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/agent/server/api.py", line 692, in _initialize_workers
    self._rendezvous(worker_group)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/metrics/api.py", line 138, in wrapper
    result = f(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/agent/server/api.py", line 507, in _rendezvous
    rdzv_info = spec.rdzv_handler.next_rendezvous()
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/rendezvous/static_tcp_rendezvous.py", line 67, in next_rendezvous
    self._store = TCPStore(  # type: ignore[call-arg]
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
torch.distributed.DistNetworkError: The client socket has failed to connect to any network address of (llama2-70b-n2-testys-master-0, 23456). The client socket has failed to connect to 172-16-100-89.llama2-70b-n2-testys-master-0.default.svc.cluster.local:23456 (errno: 113 - No route to host).
root@pyxcore:~/Noah Walsh/ibtest/Fenoys#
s-yzaloom67-238
js-yzaloom67-025
js-yzaloom67-253
js-yzaloom67-157
js-yzaloom67-254
js-yzaloom67-019
js-yzaloom67-018
js-yzaloom67-221
js-yzaloom67-016
js-yzaloom67-022
js-yzaloom67-124
js-yzaloom67-194
js-yzaloom67-094
js-yzaloom67-239
js-yzaloom67-119
js-yzaloom67-140
js-yzaloom67-081
js-yzaloom67-123
js-yzaloom67-098
js-yzaloom67-208
js-yzaloom67-076
js-yzaloom67-039
js-yzaloom67-077
js-yzaloom67-118
js-yzaloom67-114
js-yzaloom67-092
js-yzaloom67-071
js-yzaloom67-075
js-yzaloom67-093
js-yzaloom67-078
js-yzaloom67-220
js-yzaloom67-091
js-yzaloom67-113
js-yzaloom67-255
js-yzaloom67-127
js-yzaloom67-256
js-yzaloom67-023
js-yzaloom67-064
js-yzaloom67-006
js-yzaloom67-034
js-yzaloom67-120
js-yzaloom67-074
js-yzaloom67-200
js-yzaloom67-105
js-yzaloom67-203
js-yzaloom67-186
js-yzaloom67-229
js-yzaloom67-173
js-yzaloom67-212
js-yzaloom67-236
js-yzaloom67-223
js-yzaloom67-096
js-yzaloom67-227
js-yzaloom67-131
js-yzaloom67-164
js-yzaloom67-103
js-yzaloom67-248
js-yzaloom67-233
js-yzaloom67-215
js-yzaloom67-178
js-yzaloom67-246
js-yzaloom67-138
js-yzaloom67-080
js-yzaloom67-192
js-yzaloom67-102
js-yzaloom67-228
js-yzaloom67-196
js-yzaloom67-169
js-yzaloom67-250
js-yzaloom67-171
js-yzaloom67-159
js-yzaloom67-181
js-yzaloom67-142
js-yzaloom67-049
js-yzaloom67-133
js-yzaloom67-166
js-yzaloom67-235
js-yzaloom67-161
js-yzaloom67-170
js-yzaloom67-160
js-yzaloom67-193
js-yzaloom67-205
js-yzaloom67-195
js-yzaloom67-110
js-yzaloom67-082
js-yzaloom67-226
js-yzaloom67-191
js-yzaloom67-175
js-yzaloom67-213
js-yzaloom67-247
js-yzaloom67-189
js-yzaloom67-108
js-yzaloom67-218
js-yzaloom67-182
js-yzaloom67-172
js-yzaloom67-112
js-yzaloom67-137
js-yzaloom67-104
js-yzaloom67-210
js-yzaloom67-177
js-yzaloom67-143
js-yzaloom67-144
js-yzaloom67-109
js-yzaloom67-188
js-yzaloom67-232
js-yzaloom67-249
js-yzaloom67-099
js-yzaloom67-206
js-yzaloom67-158
js-yzaloom67-149
js-yzaloom67-214
js-yzaloom67-107
js-yzaloom67-240
js-yzaloom67-245
js-yzaloom67-187
js-yzaloom67-217
js-yzaloom67-136
js-yzaloom67-043
js-yzaloom67-209
js-yzaloom67-106
js-yzaloom67-224
js-yzaloom67-185
js-yzaloom67-234
js-yzaloom67-125
js-yzaloom67-033
js-yzaloom67-225
js-yzaloom67-032
js-yzaloom67-017