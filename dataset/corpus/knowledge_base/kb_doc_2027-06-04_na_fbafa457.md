## 04-dalanent configuration @Fiona Jarvis
- @Fiona Jarvis frames dalanent configuration around two areas: cluster spec and user config.
- The cluster spec is one core configuration input for dalanent.
- User config is the other configuration input dalanent relies on.
- The walkthrough is recorded in Screen Recording 2025-11-04 14.50.12.mov.
- Cluster-specific setup varies by image harbor values and spec details.
- dalanent now offers a user configuration CLI for first-time setup.
- That CLI captures image harbor, default cluster spec, and related defaults.
- This keeps users from re-entering the same options on each dalanent command.
- `dalanent config init` allows users to pick from built-in configs.
image.png

## Custom config
- The custom config flow located the spec file at /var/dalanent/config/solaos_spec.yaml.
- Pelshaw wrote the resulting configuration to /root/.dalanent/config.yaml.
- The process changed image_tag to v0.7.0.9366ea6.debug.
image.png
root@controlplane001:/tmp# dalanent config create
Select config mode:
  1) System-cea8a4ef20  (System-cea8a4ef20 cluster)
  2) us-west (us-west cluster)
  3) ap-southeast (ap-southeast cluster)
  4) cn-kevloom (cn-kevloom cluster)
  5) cn-norvik (cn-norvik cluster)
  6) cn-welbrook (cn-welbrook cluster)
  7) Beloos (Beloos cluster)
  8) bm (bm cluster)
  9) NSJ (NSJ cluster)
  10) my (my cluster)
  11) AU (AU cluster)
Enter choice [1-11] or other to customize: 1
INFO[0013] spec file found in target path: /var/dalanent/config/solaos_spec.yaml  component=specgen
dalanent config set
image.png
root@controlplane001:/tmp# dalanent config set
Choose the key to modify:
  [1] image_repo (current: registry-ap-southeast.vexeum.ai/Veliver/dalanent)
  [2] image_tag (current: v0.7.0.a4b7807.debug)
  [3] pytorchjob_image_repo (current: registry-System-cea8a4ef20.vexeum.ai/Veliver/megatron)
  [4] pytorchjob_image_tag (current: 0.12.1-a845aa7)
  [5] at_llama70b_cmd (current: MAX_STEPS=65 MOCK_DATA=true ENABLE_CKPT=0 LOG_INTERVAL=1 TP=2 PP=4 MBS=2 bash /workspace/Megatron-GG/examples/llama/train_llama2_70b_bf16.sh)
  [6] at_llama13b_cmd (current: MAX_STEPS=65 MOCK_DATA=true ENABLE_CKPT=0 LOG_INTERVAL=1 TP=2 PP=1 GBS=256 bash /workspace/Megatron-GG/examples/llama/train_llama2_13b_bf16.sh)
  [7] scheduler (current: corenantis)
  [8] roce_shared_mode (current: none)
  [9] default_spec (current: solaos_spec.yaml)
Enter number to select key: 2
Enter new value for 'image_tag': v0.7.0.9366ea6.debug
dalanent view
image.png
root@controlplane001:/tmp# dalanent config view
Current configuration:
  image_repo   : registry-ap-southeast.vexeum.ai/Veliver/dalanent
  image_tag    : v0.7.0.9366ea6.debug
  pytorchjob_image_repo : registry-System-cea8a4ef20.vexeum.ai/Veliver/megatron
  pytorchjob_image_tag : 0.12.1-a845aa7
  at_llama70b_cmd : MAX_STEPS=65 MOCK_DATA=true ENABLE_CKPT=0 LOG_INTERVAL=1 TP=2 PP=4 MBS=2 bash /workspace/Megatron-GG/examples/llama/train_llama2_70b_bf16.sh
  at_llama13b_cmd : MAX_STEPS=65 MOCK_DATA=true ENABLE_CKPT=0 LOG_INTERVAL=1 TP=2 PP=1 GBS=256 bash /workspace/Megatron-GG/examples/llama/train_llama2_13b_bf16.sh
  scheduler    : corenantis
  roce_shared_mode : none
  default_spec : solaos_spec.yaml