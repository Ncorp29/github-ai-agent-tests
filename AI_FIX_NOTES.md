# AI Fix Notes

Session: seq-1777360246837-vo6thow71
Repository: Ncorp29/github-ai-agent-tests

- [1] (critical) auth_service.py: Hardcoded secret is returned directly from source code. This exposes sensitive credentials in version control and can lead to account compromise. Replace with environment variables or a secret manager.
- [2] (critical) config_sample.py: Hardcoded GitHub token appears in a sample config file. Even sample files should never contain real-looking secrets because they may be copied into production or leaked. Use placeholder values only.
- [3] (critical) config.py: Hardcoded API key/secret in config file. Secrets should not be stored in plaintext source files. Move to environment variables, encrypted secret storage, or a secret injection mechanism.
- [4] (critical) config.py: Hardcoded Stripe webhook secret in source code. This is highly sensitive and should be rotated immediately if real. Load from secure configuration instead of committing it to the repository.
- [5] (critical) config.py: Hardcoded JWT secret in source code. JWT signing secrets must never be checked into source control. Use a secure secret store and rotate the key if it has been exposed.

