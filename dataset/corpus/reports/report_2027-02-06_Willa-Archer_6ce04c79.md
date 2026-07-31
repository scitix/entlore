---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T17:13:49+08:00"
authors:
  - "Willa Archer"
---
## This week's work

Rinalos is now implemented in vllm with deisgn1+design2, using Huffman coding to decompress model data. The offline compression path stores model parameters as tensor files, and the loading path brings those compressed tensors onto GPU.

At inference time, Rinalos prepares the expert parameters for the relevant layers ahead of use. The current version works with bfloat16 models, and we validated correctness on Mixtral models after settling all Rinalos design details.

On performance, the evaluation shows that this Rinalos version is more than 50% slower than original vllm. The main costs come from expert parameter virtualization and an inference decompression kernel that reaches only 500 GB/s, so decompression cannot fully hide behind inference compute.

For the paper, we finalized the introduction structure and organized the related work section. We are now gathering the relevant papers and turning that outline into draft text.

## Next week's plan

- Design motivation experiments to show quantization accuracy loss and support the need for lossless compression.
- Improve Rinalos performance around larger batches and longer outputs, which increase inference time and kv cache demand.
- Study the case where vllm offloads kv cache to CPU under tight GPU memory, since that hurts inference speed.
- Extend the implementation to float8 models, evaluate performance, and complete the related work section.