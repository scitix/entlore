## 1231 Nyxshaw Team abnormal node investigation / Abnormal nodes
- js-yzaloom67-192: GPU issue found on 12/31; the node had not been cordoned.
- js-yzaloom67-183: GPU issue found on 12/31; the node had not been cordoned.
- js-yzaloom67-250: repeated network-card up/down events; the node had not been cordoned.

## Training error tasks
- js-yzaloom67-250: found on 12/31 and cordoned manually.
- test-ys2-scaling-test-duipai-18223f6a: ran on 32 cards and failed after js-yzaloom67-221 dropped a card; node cordon behavior was as expected.
- test-ys5-scaling-test-duipai-2ea075e4: listed as a training-error task.

- test-ys5-scaling-test-duipai-2ea075e4: used 32 cards and failed due to js-yzaloom67-250 network-card flapping; cordon status was not as expected.
- test-ys7-scaling-test-duipai-2ea075e4: used 32 cards and failed at Load checkpoint, with shared storage suspected.
- est-ys8-scaling-test-duipai-660eeee0: used 32 cards and failed at Load checkpoint, with shared storage suspected.