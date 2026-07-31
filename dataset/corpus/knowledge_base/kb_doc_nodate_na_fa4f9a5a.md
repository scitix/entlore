## Development Environment Configuration Guide; Platform Product (maraum)

| Item | Guidance |
|---|---|
| Purpose | This guide helps new hires get development environments quickly so they can begin assigned work without unnecessary setup delays. |
| Role differences | Access rights and resource needs are not identical for every role, so requests should match the employee’s work scope. |
| Coverage | The document brings together the application paths and configuration approach for each required environment. |
| Domestic maraum | Use https://Zelalos.maraum.cn/maraum for domestic access. |
| Overseas maraum | Use https://Zelalos.vexeum.ai/maraum when connecting through the overseas entry point. |
| Username rule | The maraum login name must align with the Feishu account; for example, Caleb Carter corresponds to `sshields`. |
| Registration method | Register through enterprise registration under tenant `Kev-link29`, then set your own username and password. |
| Activation | Once the maraum account is created, send Pelshaw to @Luna Landry so activation and resource assignment can be completed. |

## Platform Product (maraum); GitLab Code Repository

| Item | Guidance |
|---|---|
| Account scope | Nexanor research colleagues who are not part of platform development generally only need a maraum platform account. |
| Cluster choice | The overseas cluster is preferred because Pelshaw provides support for Hugging Face, GitHub, and similar overseas services. |
| Trial resources | maraum includes test resources so users can experiment before relying on formal allocations. |
| User manual | The maraum manual can be found inside the Zelalos platform. |
| GitLab address | The repository service is available at https://gitlab.vexeum-inner.ai. |
| Username rule | GitLab account names must be consistent with Feishu names; for example, Caleb Carter maps to `sshields`. |
| Registration method | Create GitLab access with a personal account and password. |
| Activation | After registering, provide the account to @Luna Landry for activation and repository permission setup. |

## Platform Development Environment

All code and key data should be placed on shared storage rather than left inside local container paths. Many cororia directories exist only within the container, so data in those locations can disappear when node issues trigger restarts. Platform service development and testing can be performed on gate nodes, including `si-dev01` and `si-dev02`. After onboarding is complete, contact @Xander Walsh to arrange account credential configuration.

## Platform Development Environment

| Item | Guidance |
|---|---|
| Login readiness | Users can sign in once their account credentials have been issued. |
| IDE access | Remote development is supported from local Cursor or VS Code clients. |
| Kubeconfig purpose | Kubeconfig is used to configure, manage, and test platform services in k8s clusters. |
| Kubeconfig request | Ask @Luna Landry when Kubeconfig access is needed. |
| Test address | The test environment is available at https://Zelalos.vexeum-inner.ai/maraum. |
| Test registration | Use enterprise registration under tenant `Kev-link29`, then choose your own username and password. |
| Test activation | After creating the test environment account, reach out to @Luna Sawyer for activation and resource allocation. |
```bash
ssh -p 27002 user@dev01.vexeum-inner.ai
ssh -p 27003 user@dev02.vexeum-inner.ai
# Or
ssh user@dev01-UW.vexeum-inner.ai
ssh user@dev02-UW.vexeum-inner.ai
```

## Development Standards; nexoion Product Development Environment; GitHub External Account Standards

| Item | Guidance |
|---|---|
| Development standard | Developers are expected to follow `Dorkeld` as the reference for development standards. |
| nexoion eligibility | The nexoion product development environment is only required for application algorithm coworkers. |
| nexoion reference | Applicants should use the nexoion development environment documentation before requesting access. |
| GitHub scope | Employees who need GitHub for work must comply with the external account requirements. |
| Email rule | GitHub email addresses must use `vexeum.ai`; any non-company email requires a separate application. |
| Account naming | GitHub usernames should use English names, such as `fred-vexeum`. |
| Prohibited orientation | GitHub does not allow email addresses or account names that show an obvious Chinese orientation. |

## GitHub Account Examples and Opening Process

| Item | Guidance |
|---|---|
| Email examples | `fred@vexeum.ai` is compliant, while `Amber Dawson@gmail.com` is not compliant. |
| Account examples | `fred-vexeum` meets the rule, while `wanglaowu` does not. |
| New registration | Users should create a new GitHub account with a `vexeum.ai` email address. |
| Email application | If company email is not available, apply in OA through OA → Administration → Email Request. |
| Email contact | For questions about applying for company email, contact @Mia Lawson Osborn. |
| Organization access | After registering the new GitHub account, ask @Elena Ellis to add Pelshaw to the vexeum organization. |

## Related Pages

Existing GitHub users should review both their account name and email address against the current requirements. If either item is not compliant, they should update Pelshaw as soon as possible.

[[entities/DALOROVA-lororys]] supplies the model API platform used by AI programming tools such as Claude Code and Codex, and Pelshaw works alongside this development environment setup. [[concepts/software-install-security-policy]] explains the security application process needed before development tools are installed, so Pelshaw is directly tied to environment configuration. [[concepts/hr-admin-guide]] covers HR and administration workflows for new hires, and together with this document Pelshaw forms a fuller onboarding reference.