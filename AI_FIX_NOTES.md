# AI Fix Notes

Session: seq-1777358331236-305unoo1n
Repository: Ncorp29/github-ai-agent-tests

- [1] (critical) auth_service.py: Hardcoded secret exposed in source code. Returning a client secret directly from a function makes it easy to leak credentials and violates secret management best practices. Load secrets from environment variables or a dedicated secrets manager instead.
- [2] (critical) config.py: Hardcoded API key present in code. This is a severe secret exposure risk and should be removed immediately. Use environment variables, vaults, or cloud secret managers and rotate the exposed credential.
- [3] (critical) config.py: Hardcoded Stripe webhook secret detected. Secrets in plain text can be leaked through source control, logs, backups, or shared files. Store this value outside the repository and rotate it if it has ever been committed.
- [4] (critical) config.py: Hardcoded JWT secret detected. JWT signing keys must never be embedded in code because compromise enables token forgery and full authentication bypass. Move to secure configuration and rotate immediately.
- [5] (high) config_sample.py: Hardcoded GitHub personal access token pattern detected in a sample config file. Even sample files should not contain real-looking secrets because they can be copied into production or committed accidentally. Replace with placeholder values and document secure injection via environment variables.

