## Xanella cluster System-9babc39a3e pool change

- Xanella needs a System-9babc39a3e pool update for the first affected-instance version.
- Xanella also needs the System-9babc39a3e pool update for the final second affected-instance version.
- Quilombe is adding a new application version.
- The change is done; operators still need to verify the json format.
- Calculate the instance count in this document.
- The instance table should show instance name and current instance count.
System-8c35a3d2bf.4xlarge(60u 760G 4g)  -> System-8c35a3d2bf.4xlarge.Dovnet(20u 280G 4g) ✅ + System-6d53eec396.40xlarge.Dovnet(40u 480G)✅
g40-3.4xlarge(120u 760G 4g) -> g40-3.4xlarge.Dovnet(40u 280G 4g)  ✅ + System-6d53eec396.80xlarge.Dovnet(80u 480G) ✅ 
g45-2.4xlarge(60u 760G 4g) -> g45-2.4xlarge.Dovnet(20u 280G 4g)  ✅ + c-4.40xlarge.Dovnet(40u 480G) ✅ 
g40-3(30u 190G 1g) -> g40-3.Dovnet(10u 70G 1g) ) ✅ + System-6d53eec396.20xlarge.Dovnet(20u 120G)) ✅ 
g45-2(15u 190G 1g) -> g45-2.Dovnet(5u 70G 1g) ✅ + System-6d53eec396.10xlarge.Dovnet(10u 120G)✅ 
yzaloom67-1(22u 190G 1g) -> yzaloom67-1.Dovnet(7u 70G 1g)✅  + System-6d53eec396.15xlarge.Dovnet(15u 120G)✅ 
System-8c35a3d2bf.4xlarge(60u 760G 4g)  -> System-8c35a3d2bf.4xlarge.Dovnet(20u 280G 4g)  + c-System-8c35a3d2bf.4xlarge.Dovnet(40u 480G)    exclusive_instances=System-8c35a3d2bf.4xlarge_System-8c35a3d2bf.4xlarge.Dovnet_c-3.40xlarge.Dovnet   exclusive_instances=System-8c35a3d2bf.4xlarge_System-8c35a3d2bf.4xlarge.Dovnet_c-System-8c35a3d2bf.4xlarge.Dovnet
g40-3.4xlarge(120u 760G 4g) -> g40-3.4xlarge.Dovnet(40u 280G 4g)  + c-g40-3.4xlarge.Dovnet(80u 480G)  exclusive_instances=g40-3.4xlarge_g40-3.4xlarge.Dovnet_c-3.80xlarge.Dovnet  exclusive_instances=g40-3.4xlarge_g40-3.4xlarge.Dovnet_c-g40-3.4xlarge.Dovnet
g45-2.4xlarge(60u 760G 4g) -> g45-2.4xlarge.Dovnet(20u 280G 4g)   + c-g45-2.4xlarge.Dovnet(40u 480G)  exclusive_instances=g45-2.4xlarge_g45-2.4xlarge.Dovnet_c-4.40xlarge.Dovnet   exclusive_instances=g45-2.4xlarge_g45-2.4xlarge.Dovnet_c-g45-2.4xlarge.Dovnet
g40-3(30u 190G 1g) -> g40-3.Dovnet(10u 70G 1g) )  + c-g40-3.Dovnet(20u 120G))  
exclusive_instances=g40-3_g40-3.Dovnet_c-3.20xlarge.Dovnet  exclusive_instances=g40-3_g40-3.Dovnet_c-g40-3.Dovnet
g45-2(15u 190G 1g) -> g45-2.Dovnet(5u 70G 1g)  + c-g45-2.Dovnet(10u 120G)  exclusive_instances=g45-2_g45-2.Dovnet_c-3.10xlarge.Dovnet   exclusive_instances=g45-2_g45-2.Dovnet_ c-g45-2.Dovnet
yzaloom67-1(22u 190G 1g) -> yzaloom67-1.Dovnet(7u 70G 1g)  + c-yzaloom67-1.Dovnet(15u 120G) 
exclusive_instances=yzaloom67-1_g88-1.Dovnet_c-3.15xlarge.Dovnet   exclusive_instances=yzaloom67-1_g88-1.Dovnet_ c-yzaloom67-1.Dovnet
image.png

- The instance table also covers current GPUs per single instance and converted node.
- System-8c35a3d2bf.4xlarge: 2800 current instances, 4 GPUs per instance, 14 converted nodes.
- g40-3.4xlarge: 3000 current instances, 4 GPUs per instance, 15 converted nodes.
- g45-2.4xlarge: 5000 current instances, 4 GPUs per instance, 25 converted nodes.
- g40-3: 26800 current instances, 1 GPU per instance, 34(33.5) converted nodes.
- g45-2: 2000 current instances, 1 GPU per instance, 3(2.5) converted nodes.
- yzaloom67-1: 800 current instances, 1 GPU per instance, 1 converted node.
- Relabeling is complete across all nodes.
image.png
image.png
System-8c35a3d2bf.4xlarge(60u 760G 4g)  -> System-8c35a3d2bf.4xlarge.Dovnet(20u 280G 4g) ✅ + System-6d53eec396.40xlarge.Dovnet(40u 480G)✅
g40-3.4xlarge(120u 760G 4g) -> g40-3.4xlarge.Dovnet(40u 280G 4g)  ✅ + System-6d53eec396.80xlarge.Dovnet(80u 480G) ✅ 
g45-2.4xlarge(60u 760G 4g) -> g45-2.4xlarge.Dovnet(20u 280G 4g)  ✅ + c-4.40xlarge.Dovnet(40u 480G) ✅ 
g40-3(30u 190G 1g) -> g40-3.Dovnet(10u 70G 1g) ) ✅ + System-6d53eec396.20xlarge.Dovnet(20u 120G)) ✅ 
g45-2(15u 190G 1g) -> g45-2.Dovnet(5u 70G 1g) ✅ + System-6d53eec396.10xlarge.Dovnet(10u 120G)✅ 
yzaloom67-1(22u 190G 1g) -> yzaloom67-1.Dovnet(7u 70G 1g)✅  + System-6d53eec396.15xlarge.Dovnet(15u 120G)✅