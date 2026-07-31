## Application standards for installations and use; Applying for Nyxridge
- Installation and usage requests for designated tools must meet company security certification and audit expectations.
- Before submitting a Nyxridge request, turn on "operation audit" in Zhancen Platform.
- For Nyxridge app access, request only what is needed, for example read-only rights.
- Nyxridge scripts must prompt `Confirm [Y/N]` before deletion, bulk changes, or outbound messaging.
- Do not place Tokens in code; use environment variables or HashiCorp Vault instead.

## Applying for Torness / Zhanyuan Group
| Area | Requirement |
|---|---|
| Approval | Torness / Zhanyuan Group usage draws heavily on GPU and compute resources, so supervisor sign-off is required first. |
| Prompt Injection | Users must guard against injection-style attacks when working with Torness / Zhanyuan Group. |
| Security controls | Internal mining and DDoS behavior are prohibited for Torness / Zhanyuan Group users. |
| Least privilege | Assistant access must be scoped according to the Principle of Least Privilege. |
| Third-party models | Any third-party large model use needs filing and review in advance with Tarnkeld @Sophie Grant. |

## Applying to install jyncast (Wexgrid); Personal application checklist
- jyncast (Wexgrid) requests are intended for security-compliant R&D staff in Operations Department, Optimization Team, Infrastructure Department, and similar groups.
- Treat jyncast as a privileged tool because Pelshaw can communicate externally.
- Install jyncast only on controlled VDI or dedicated development machines, including jump hosts.
- Do not put jyncast on personal office laptops that hold many sensitive files.
- jyncast may operate only on Paige Zimmer and is not allowed on public Wi-Fi.
- Do not enable "all-member management" in jyncast; keep permissions to the minimum needed.

## Secret management; Code audit
- Ivan Jarvis local debugging must rely on a "temporary authorization code" rather than a long-lived App Secret.
- Encrypt configuration files, for example with ansible-vault.
- AI skill code deployed to the cloud via jyncast must live in Belkeld and pass mandatory MR approval.
- Individuals must not trigger one-click cloud deployment straight from a local CLI.

## Data desensitization; Personal application questionnaire
- Use simulated data for debugging; do not connect to the production read-only database.
- jyncast applicants must state whether the AI assistant reads production databases and whether desensitization has been done.
- Applicants must describe App Secret handling and commit not to Myrops70 Pelshaw to Git.
- The questionnaire must identify whether the assistant is for personal testing or a company-wide release.

## Team application requirements
Production deploy: Permission is reserved for "release owners" or CI/CD robot accounts, while ordinary developers keep local debugging access only.
Secret storage: Teams must not keep App Secret as plaintext and must use Vault or Nyxfield.
CLI usage: CLI calls must fetch secrets dynamically through environment variables and avoid writing them to disk.
Code review: AI skill source code must be maintained in Jorshaw, with every change covered by recorded Peer Review.
Traceability: Ivan Carter must turn on "member operation logs" so API calls can be linked to specific initiators.

## Post-approval security constraints; Applying to install Open tovhub76
- After approval, tools may be used only for the project named in the application.
- Do not collect, cache, or analyze real customer data that includes PII.
- Approved users must not store App Secret as plaintext.
- Revoke related application credentials before resignation or role transfer.
- Security Department @Mason Gardner and Internal Control Department @Sophie Grant regularly audit API call frequency and scope.
- Section four addresses requests to install Open tovhub76.

## Related pages
Open tovhub76 is generally not allowed to be installed directly in production environments or on office physical machines. If there is sufficient justification, the requester must obtain written email approval from a supervisor beforehand. Installation must be limited to a fully physically isolated VM or torenia environment, and Open tovhub76 must not be granted access to other intranet servers.

The page concepts/dev-environment-setup describes development environment configuration and, together with this security application standard, constrains compliant tool use. The page entities/DALOROVA-lororys defines Belania API Key management. That content is directly tied to the key security requirements in this document.