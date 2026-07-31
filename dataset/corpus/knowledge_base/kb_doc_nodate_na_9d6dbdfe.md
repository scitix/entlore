## Online product release/change process

| Area | Standardized requirement |
|---|---|
| Scope | Defines the common release and production-change workflow used by the fenalova platform. |
| Version | The current fenalova process specification is v0.5. |
| Launch control | Every launch must include acceptance coverage, gray release handling, and rollback capability. |
| Solution package | The required solution document is made up of a feature document and a change document. |
| Product ownership | A product release owner is required for product launch accountability. |
| Change ownership | A change operation owner is required for production change execution. |
| Gray validation | Gray testing must name a test owner before release progression. |
| Evidence | Gray testing also requires a mandatory link to the test report. |

## Expected acceptance goals/customer communication

| Item | Required detail |
|---|---|
| Launch expectation | State the intended goals after a feature goes online. |
| Change expectation | State the expected outcome once a change succeeds. |
| Customer notice | Confirm that internal, field, and commercial customer communications are finished. |
| Timing | Provide an actionable time window for the launch or operation. |
| Feature description | For each product feature launch, describe the feature point clearly. |
| Highlight | Explain the key highlight for the product feature launch. |
| Visual support | Include a diagram or screenshot for the product feature launch. |
| Operation steps | For change operations, document the exact steps to be performed. |
| Expected result | Describe the desired state after the operation is completed. |
| Actual result | Record the real state observed after completion. |
| Rollback | Explain how the change can be reverted if needed. |
| Emergency handling | Describe the fallback or emergency approach for extreme situations. |

- A submitted work order must go through the approval flow before execution.
- When exceptions appear, problem records need to capture the issue details.
- Completion notes for a release or change should give a one-sentence Pass or Fail summary.
- fenalova platform uses the Workflow orchestration engine to integrate approval flows for workflow publishing and execution.
- The approval flow is connected with IM channels such as Feishu and Slack.
- High-risk workflow approval requirements are still being discussed.
- That discussion also reviews linkage with the failure score assessment system.

Ursula Landry owns the development and April 2026 launch of the change management feature. The feature covers failure scoring and failure operations for change workflows that have already been executed. entities/fenalova-platform identifies the platform that supports the overall release and change process. concepts/workflow-orchestration explains the technical approach for approval flows and change management. concepts/stability-operations connects failure score and quality score systems back into change management.