## Incident Description

- Time: 2027-01-15
- Reporter: Xander Grant
- System: Maraum
- Symptom: After inference applications are deleted in the AurwoodOraport environment, the pod is not released
- Impact scope: Failure symptom: pod was not released after the inference application in the AurwoodOraport environment was deleted

## Analysis

- Root cause:

The owner reference of the deployment pods was deleted, so these pods were not managed by the Nora Drake console. The Nora Drake console code has no Bexcast61 to directly modify pods and has never called the k8s pod interface, so the initial suspicion is that some component in the cluster behaved abnormally. Further investigation is needed using the k8s audit logs to identify the component that modified owner reference. @Xander Nolan

```text
Found 194 Pod definitions
  Pod #1 (packing-sft-28200it-worker-8758878cd-dffw2): ownerReferences field is missing ✓
  Pod #2 (packing-sft-28200it-worker-8758878cd-jvhdq): ownerReferences field is missing ✓
  Pod #3 (packing-sft-28200it-worker-8758878cd-srcgd): has ownerReferences (1 total)
  Pod #4 (packing-sft-28200it-worker-8758878cd-wnjqq): has ownerReferences (1 total)
  Pod #5 (qwen3-Tarnholm-64c-bf16-H20X-iter-0010000-worker-f67f4bc89-55mr4): has ownerReferences (1 total)
  Pod #6 (qwen3-Tarnholm-64c-bf16-H20X-iter-0010000-worker-f67f4bc89-r7wlc): has ownerReferences (1 total)
  Pod #7 (qwen3-Tarnholm-64c-bf16-H20X-iter-0010000-worker-f67f4bc89-tk58j): ownerReferences field is missing ✓
  Pod #8 (qwen3-Tarnholm-64c-bf16-H20X-iter-0010000-worker-f67f4bc89-tzwhx): ownerReferences field is missing ✓
  Pod #9 (qwen3-Yorombe-sftpack-0010000-think-worker-74749bb649-hvr4l): has ownerReferences (1 total)
  Pod #10 (qwen3-Yorombe-sftpack-0010000-think-worker-74749bb649-jxltp): ownerReferences field is missing ✓
  Pod #11 (qwen3-Yorombe-sftpack-0010000-think-worker-74749bb649-mzvbt): has ownerReferences (1 total)
  Pod #12 (qwen3-Yorombe-sftpack-0010000-think-worker-74749bb649-r8ckr): ownerReferences field is missing ✓
  Pod #13 (qwen3-psft-10000it-worker-565c54b597-4jq8p): ownerReferences field is missing ✓
  Pod #14 (qwen3-psft-10000it-worker-565c54b597-5qwnp): ownerReferences field is missing ✓
  Pod #15 (qwen3-psft-10000it-worker-565c54b597-fv9dm): has ownerReferences (1 total)
  Pod #16 (qwen3-psft-10000it-worker-565c54b597-r5gzb): has ownerReferences (1 total)
  Pod #17 (qwen3-psft-28200it-worker-6ccd6dcdcc-8gnr8): has ownerReferences (1 total)
  Pod #18 (qwen3-psft-28200it-worker-6ccd6dcdcc-jh8kg): ownerReferences field is missing ✓
  Pod #19 (qwen3-psft-28200it-worker-6ccd6dcdcc-vjbxh): ownerReferences field is missing ✓
  Pod #20 (qwen3-psft-28200it-worker-6ccd6dcdcc-zhlwq): has ownerReferences (1 total)
  Pod #21 (deepseek-r1-fork-1-worker-66588cf49-hmtfg): ownerReferences field is missing ✓
  Pod #22 (deepseek-r1-fork-2-worker-85b5ddc6dd-9zrqj): ownerReferences field is missing ✓
  Pod #23 (deepseek-r1-worker-fdfc6b74c-gxswv): ownerReferences field is missing ✓
  Pod #24 (inference-glm-4-6-fork-1-worker-7fb7c846d-mtrrp): ownerReferences field is missing ✓
  Pod #25 (inference-glm-4-6-worker-54856dd74d-x97w8): ownerReferences field is missing ✓
  Pod #26 (llama-4-maverick-instruct-fork-1-worker-6cd88f88b4-tw8zc): ownerReferences field is missing ✓
  Pod #27 (llama-4-maverick-instruct-fork-3-worker-559c5cf4b5-hhs25): ownerReferences field is missing ✓
  Pod #28 (llama-4-maverick-instruct-worker-f8b69974b-xrzvz): ownerReferences field is missing ✓
  Pod #29 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-bbprt): has ownerReferences (1 total)
  Pod #30 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-bpv2q): has ownerReferences (1 total)
  Pod #31 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-lrgsf): has ownerReferences (1 total)
  Pod #32 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-lt2wg): has ownerReferences (1 total)
  Pod #33 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-q7pqp): has ownerReferences (1 total)
  Pod #34 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-tj8lj): has ownerReferences (1 total)
  Pod #35 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-zpzzr): has ownerReferences (1 total)
  Pod #36 (qwen3-235b-a22b-for-Oliion-worker-86768997d9-zq7rv): has ownerReferences (1 total)
  Pod #37 (qwen3-Yorombe-sft-dpo-rpo-v3-iter-1200-vllm-worker-5fd457565b-lzdkg): has ownerReferences (1 total)
  Pod #38 (qwen25-72b-base-0): has ownerReferences (1 total)
  Pod #39 (qwen25-72b-base-0-1): has ownerReferences (1 total)
  Pod #40 (qwen25-72b-base-1): has ownerReferences (1 total)
  Pod #41 (qwen25-72b-base-1-1): has ownerReferences (1 total)
  Pod #42 (qwen25-72b-base-2): has ownerReferences (1 total)
  Pod #43 (qwen25-72b-base-2-1): has ownerReferences (1 total)
  Pod #44 (qwen25-72b-base-3): has ownerReferences (1 total)
  Pod #45 (qwen25-72b-base-3-1): has ownerReferences (1 total)
  Pod #46 (qwen3-32b-worker-6ff74f8655-hjvl4): ownerReferences field is missing ✓
  Pod #47 (qwen3-32b-worker-6ff74f8655-p4kfj): ownerReferences field is missing ✓
  Pod #48 (qwen3-32b-worker-6ff74f8655-qvq8t): ownerReferences field is missing ✓
  Pod #49 (qwen3-32b-worker-6ff74f8655-r2qhm): ownerReferences field is missing ✓
  Pod #50 (qwen3-32b-worker-f87c69dc6-4768s): has ownerReferences (1 total)
  Pod #51 (qwen3-32b-worker-f87c69dc6-p6l84): has ownerReferences (1 total)
  Pod #52 (qwen3-32b-worker-f87c69dc6-xdx74): has ownerReferences (1 total)
  Pod #53 (qwen3-32b-worker-f87c69dc6-xrp7p): has ownerReferences (1 total)
  Pod #54 (qwen3-30b-base-iter-0010000-fork-worker-766cc59c75-l9nhr): has ownerReferences (1 total)
  Pod #55 (qwen3-30b-base-iter-0010000-worker-68cb77944f-85v54): ownerReferences field is missing ✓
  Pod #56 (qwen3-30b-base-iter-0010000-worker-68cb77944f-gjjqv): ownerReferences field is missing ✓
  Pod #57 (qwen3-30b-base-iter-0026000-fork-worker-8f8bf887d-ss4xl): has ownerReferences (1 total)
  Pod #58 (qwen3-30b-base-rl-1200steps-fork-worker-589d5c897f-krg9s): has ownerReferences (1 total)
  Pod #59 (qwen3-Tarnholm-iter-0028200-rl-worker-5749f64ff5-8lbsw): ownerReferences field is missing ✓
  Pod #60 (qwen3-Tarnholm-iter-0028200-rl-worker-5749f64ff5-zkfjj): ownerReferences field is missing ✓
  Pod #61 (eval-qwen2-5-72b-instruct-worker-77dd88848d-2bgw7): has ownerReferences (1 total)
  Pod #62 (eval-qwen2-5-72b-instruct-worker-77dd88848d-xn9gk): ownerReferences field is missing ✓
  Pod #63 (qweninstruct-worker-5d8754b98c-4df7r): ownerReferences field is missing ✓
  Pod #64 (qweninstruct-worker-5d8754b98c-4t4bq): ownerReferences field is missing ✓
  Pod #65 (qweninstruct-worker-5d8754b98c-4z7mh): ownerReferences field is missing ✓
  Pod #66 (qweninstruct-worker-5d8754b98c-57tst): ownerReferences field is missing ✓
  Pod #67 (qweninstruct-worker-5d8754b98c-cm9dz): ownerReferences field is missing ✓
  Pod #68 (qweninstruct-worker-5d8754b98c-cmvjv): ownerReferences field is missing ✓
  Pod #69 (qweninstruct-worker-5d8754b98c-cwg26): ownerReferences field is missing ✓
  Pod #70 (qweninstruct-worker-5d8754b98c-lrxxf): ownerReferences field is missing ✓
  Pod #71 (qweninstruct-worker-5d8754b98c-pql4k): ownerReferences field is missing ✓
  Pod #72 (qweninstruct-worker-5d8754b98c-qmxvz): ownerReferences field is missing ✓
  Pod #73 (qweninstruct-worker-5d8754b98c-rvvdm): ownerReferences field is missing ✓
  Pod #74 (qweninstruct-worker-5d8754b98c-zfpvb): ownerReferences field is missing ✓
  Pod #75 (deepseek-r1-0): has ownerReferences (1 total)
  Pod #76 (deepseek-r1-0-1): has ownerReferences (1 total)
  Pod #77 (deepseek-r1-1): has ownerReferences (1 total)
  Pod #78 (deepseek-r1-1-1): has ownerReferences (1 total)
  Pod #79 (deepseek-r1-2): has ownerReferences (1 total)
  Pod #80 (deepseek-r1-2-1): has ownerReferences (1 total)
  Pod #81 (deepseek-r1-3): has ownerReferences (1 total)
  Pod #82 (deepseek-r1-3-1): has ownerReferences (1 total)
  Pod #83 (deepseek-v3-1-0-decode-0): has ownerReferences (1 total)
  Pod #84 (deepseek-v3-1-0-decode-0-1): has ownerReferences (1 total)
  Pod #85 (deepseek-v3-1-0-decode-1): has ownerReferences (1 total)
  Pod #86 (deepseek-v3-1-0-decode-1-1): has ownerReferences (1 total)
  Pod #87 (deepseek-v3-1-0-prefill-0): has ownerReferences (1 total)
  Pod #88 (deepseek-v3-1-0-prefill-1): has ownerReferences (1 total)
  Pod #89 (deepseek-v3-1-0-scheduler-6649f4d96f-jtrkl): has ownerReferences (1 total)
  Pod #90 (deepseek-v3-1-terminus-0-decode-0): has ownerReferences (1 total)
  Pod #91 (deepseek-v3-1-terminus-0-decode-0-1): has ownerReferences (1 total)
  Pod #92 (deepseek-v3-1-terminus-0-decode-1): has ownerReferences (1 total)
  Pod #93 (deepseek-v3-1-terminus-0-decode-1-1): has ownerReferences (1 total)
  Pod #94 (deepseek-v3-1-terminus-0-prefill-0): has ownerReferences (1 total)
  Pod #95 (deepseek-v3-1-terminus-0-prefill-1): has ownerReferences (1 total)
  Pod #96 (deepseek-v3-1-terminus-0-scheduler-64c754c6c-82s4d): has ownerReferences (1 total)
  Pod #97 (deepseek-v3-2-0-decode-0): has ownerReferences (1 total)
  Pod #98 (deepseek-v3-2-0-decode-0-1): has ownerReferences (1 total)
  Pod #99 (deepseek-v3-2-0-decode-1): has ownerReferences (1 total)
  Pod #100 (deepseek-v3-2-0-decode-1-1): has ownerReferences (1 total)
  Pod #101 (deepseek-v3-2-0-decode-2): has ownerReferences (1 total)
  Pod #102 (deepseek-v3-2-0-decode-2-1): has ownerReferences (1 total)
  Pod #103 (deepseek-v3-2-0-decode-3): has ownerReferences (1 total)
  Pod #104 (deepseek-v3-2-0-decode-3-1): has ownerReferences (1 total)
  Pod #105 (deepseek-v3-2-0-prefill-0): has ownerReferences (1 total)
  Pod #106 (deepseek-v3-2-0-prefill-1): has ownerReferences (1 total)
  Pod #107 (deepseek-v3-2-0-prefill-2): has ownerReferences (1 total)
  Pod #108 (deepseek-v3-2-0-prefill-3): has ownerReferences (1 total)
  Pod #109 (deepseek-v3-2-0-scheduler-674f74c45b-jb9c9): has ownerReferences (1 total)
  Pod #110 (deepseek-v3-2-0-scheduler-674f74c45b-trfhn): has ownerReferences (1 total)
  Pod #111 (deepseek-v3-2-speciale-sglang056-0-decode-0): has ownerReferences (1 total)
  Pod #112 (deepseek-v3-2-speciale-sglang056-0-decode-0-1): has ownerReferences (1 total)
  Pod #113 (deepseek-v3-2-speciale-sglang056-0-decode-1): has ownerReferences (1 total)
  Pod #114 (deepseek-v3-2-speciale-sglang056-0-decode-1-1): has ownerReferences (1 total)
  Pod #115 (deepseek-v3-2-speciale-sglang056-0-prefill-0): has ownerReferences (1 total)
  Pod #116 (deepseek-v3-2-speciale-sglang056-0-prefill-1): has ownerReferences (1 total)
  Pod #117 (deepseek-v3-2-speciale-sglang056-0-scheduler-5d4f8dcd66-47t7j): has ownerReferences (1 total)
  Pod #118 (glm-4-6-0): has ownerReferences (1 total)
  Pod #119 (glm-4-6-0-1): has ownerReferences (1 total)
  Pod #120 (glm-4-6-1): has ownerReferences (1 total)
  Pod #121 (glm-4-6-1-1): has ownerReferences (1 total)
  Pod #122 (glm-4-6v-worker-5697b5b58c-2276m): has ownerReferences (1 total)
  Pod #123 (glm-4-6v-worker-5697b5b58c-42rgh): ownerReferences field is missing ✓
  Pod #124 (glm-4-6v-worker-5697b5b58c-8ngtx): has ownerReferences (1 total)
  Pod #125 (glm-4-6v-worker-5697b5b58c-qxhzc): ownerReferences field is missing ✓
  Pod #126 (glm-4-7-worker-855b7c5d7b-7nl5t): has ownerReferences (1 total)
  Pod #127 (glm-4-7-worker-855b7c5d7b-ldttj): ownerReferences field is missing ✓
  Pod #128 (glm-4-7-worker-855b7c5d7b-mfx2r): ownerReferences field is missing ✓
  Pod #129 (glm-4-7-worker-855b7c5d7b-t48bv): has ownerReferences (1 total)
  Pod #130 (gpt-Quoreeon-120b-0-decode-0): has ownerReferences (1 total)
  Pod #131 (gpt-Quoreeon-120b-0-decode-1): has ownerReferences (1 total)
  Pod #132 (gpt-Quoreeon-120b-0-prefill-0): has ownerReferences (1 total)
  Pod #133 (gpt-Quoreeon-120b-0-scheduler-ccc89ffd5-pz2nm): has ownerReferences (1 total)
  Pod #134 (kat-dev-72b-exp-worker-d5469f846-4mtzt): has ownerReferences (1 total)
  Pod #135 (kat-dev-72b-exp-worker-d5469f846-f5cq9): has ownerReferences (1 total)
  Pod #136 (kat-dev-72b-exp-worker-d5469f846-fd22h): ownerReferences field is missing ✓
  Pod #137 (kat-dev-72b-exp-worker-d5469f846-g8f4q): ownerReferences field is missing ✓
  Pod #138 (kimi-System-2b9f5c895e-instruct-0-decode-0): has ownerReferences (1 total)
  Pod #139 (kimi-System-2b9f5c895e-instruct-0-decode-0-1): has ownerReferences (1 total)
  Pod #140 (kimi-System-2b9f5c895e-instruct-0-decode-1): has ownerReferences (1 total)
  Pod #141 (kimi-System-2b9f5c895e-instruct-0-decode-1-1): has ownerReferences (1 total)
  Pod #142 (kimi-System-2b9f5c895e-instruct-0-prefill-0): has ownerReferences (1 total)
  Pod #143 (kimi-System-2b9f5c895e-instruct-0-prefill-0-1): has ownerReferences (1 total)
  Pod #144 (kimi-System-2b9f5c895e-instruct-0-prefill-1): has ownerReferences (1 total)
  Pod #145 (kimi-System-2b9f5c895e-instruct-0-prefill-1-1): has ownerReferences (1 total)
  Pod #146 (kimi-System-2b9f5c895e-instruct-0-scheduler-5bbc7f78d-kbb7q): has ownerReferences (1 total)
  Pod #147 (kimi-System-2b9f5c895e-instruct-0-scheduler-5bbc7f78d-xlv2j): has ownerReferences (1 total)
  Pod #148 (kimi-System-2b9f5c895e-thinking-0-decode-0): has ownerReferences (1 total)
  Pod #149 (kimi-System-2b9f5c895e-thinking-0-decode-0-1): has ownerReferences (1 total)
  Pod #150 (kimi-System-2b9f5c895e-thinking-0-decode-1): has ownerReferences (1 total)
  Pod #151 (kimi-System-2b9f5c895e-thinking-0-decode-1-1): has ownerReferences (1 total)
  Pod #152 (kimi-System-2b9f5c895e-thinking-0-prefill-0): has ownerReferences (1 total)
  Pod #153 (kimi-System-2b9f5c895e-thinking-0-prefill-0-1): has ownerReferences (1 total)
  Pod #154 (kimi-System-2b9f5c895e-thinking-0-prefill-1): has ownerReferences (1 total)
  Pod #155 (kimi-System-2b9f5c895e-thinking-0-prefill-1-1): has ownerReferences (1 total)
  Pod #156 (kimi-System-2b9f5c895e-thinking-0-scheduler-6c5df85878-2k9h8): has ownerReferences (1 total)
  Pod #157 (kimi-System-2b9f5c895e-thinking-0-scheduler-6c5df85878-xwdjz): has ownerReferences (1 total)
  Pod #158 (mistral-large-3-675b-instruct-2512-worker-658655f4db-bl74z): has ownerReferences (1 total)
  Pod #159 (mistral-large-3-675b-instruct-2512-worker-658655f4db-m59wm): ownerReferences field is missing ✓
  Pod #160 (mistral-large-3-675b-instruct-2512-worker-658655f4db-s7lzm): ownerReferences field is missing ✓
  Pod #161 (mistral-large-3-675b-instruct-2512-worker-658655f4db-vrcrz): has ownerReferences (1 total)
  Pod #162 (qwen2-5-72b-instruct-0): has ownerReferences (1 total)
  Pod #163 (qwen2-5-72b-instruct-0-1): has ownerReferences (1 total)
  Pod #164 (qwen2-5-72b-instruct-1): has ownerReferences (1 total)
  Pod #165 (qwen2-5-72b-instruct-1-1): has ownerReferences (1 total)
  Pod #166 (qwen2-5-72b-instruct-2): has ownerReferences (1 total)
  Pod #167 (qwen2-5-72b-instruct-2-1): has ownerReferences (1 total)
  Pod #168 (qwen2-5-72b-instruct-3): has ownerReferences (1 total)
  Pod #169 (qwen2-5-72b-instruct-3-1): has ownerReferences (1 total)
  Pod #170 (qwen2-5-math-7b-instruct-worker-58b7c9b8d7-55j46): has ownerReferences (1 total)
  Pod #171 (qwen2-5-math-7b-instruct-worker-58b7c9b8d7-hnqn2): has ownerReferences (1 total)
  Pod #172 (qwen2-5-math-7b-instruct-worker-58b7c9b8d7-mqpsq): has ownerReferences (1 total)
  Pod #173 (qwen2-5-math-7b-instruct-worker-58b7c9b8d7-wdnlk): has ownerReferences (1 total)
  Pod #174 (qwen3-235b-a22b-instruct-2507-0-decode-0): has ownerReferences (1 total)
  Pod #175 (qwen3-235b-a22b-instruct-2507-0-decode-1): has ownerReferences (1 total)
  Pod #176 (qwen3-235b-a22b-instruct-2507-0-prefill-0): has ownerReferences (1 total)
  Pod #177 (qwen3-235b-a22b-instruct-2507-0-scheduler-6d984d8b5b-pvqjt): has ownerReferences (1 total)
  Pod #178 (qwen3-235b-a22b-thinking-2507-decode-0): has ownerReferences (1 total)
  Pod #179 (qwen3-235b-a22b-thinking-2507-decode-1): has ownerReferences (1 total)
  Pod #180 (qwen3-235b-a22b-thinking-2507-prefill-0): has ownerReferences (1 total)
  Pod #181 (qwen3-235b-a22b-thinking-2507-prefill-1): has ownerReferences (1 total)
  Pod #182 (qwen3-235b-a22b-thinking-2507-Junient-7c75dcbbfd-v2c2z): has ownerReferences (1 total)
  Pod #183 (qwen3-32b-worker-85fd7c65d9-4mcht): has ownerReferences (1 total)
  Pod #184 (qwen3-32b-worker-85fd7c65d9-h8gj9): has ownerReferences (1 total)
  Pod #185 (qwen3-Fenhaven-2507-worker-576b5fccbd-7vll4): has ownerReferences (1 total)
  Pod #186 (qwen3-Fenhaven-2507-worker-576b5fccbd-96p46): has ownerReferences (1 total)
  Pod #187 (qwen3-Fenhaven-2507-worker-576b5fccbd-c5pct): has ownerReferences (1 total)
  Pod #188 (qwen3-Fenhaven-2507-worker-576b5fccbd-q7rs9): has ownerReferences (1 total)
  Pod #189 (qwen3-8b-worker-7d5b84d6df-7cxrr): has ownerReferences (1 total)
  Pod #190 (qwen3-8b-worker-7d5b84d6df-fk44p): has ownerReferences (1 total)
  Pod #191 (qwen3-vl-235b-a22b-instruct-worker-5457856578-4pldz): ownerReferences field is missing ✓
  Pod #192 (qwen3-vl-235b-a22b-instruct-worker-5457856578-5svv6): has ownerReferences (1 total)
  Pod #193 (qwen3-vl-235b-a22b-instruct-worker-5457856578-926np): has ownerReferences (1 total)
  Pod #194 (qwen3-vl-235b-a22b-instruct-worker-5457856578-9t27k): ownerReferences field is missing ✓

Found 49 Pod with no ownerReferences
================================================================================
```

## Handling

- Handlers: Xander Grant, Noah Irwin
- Steps:

```text
Use a script to filter pods without owner reference, with cleanup performed by @Ivan Bishop
Continue observing afterward; no more pods without owner reference appeared
The container team continues investigating the root cause based on audit logs @Ivan Bishop
```

## Retrospective

TBD