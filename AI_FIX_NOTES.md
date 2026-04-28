# AI Fix Notes

Session: seq-1777358659861-ihxi31h8t
Repository: Ncorp29/github-ai-agent-tests

- [1] (critical) auth_service.py: Hardcoded secret returned from get_token(). Storing credentials in source code is a critical secret-management issue and may expose sensitive authentication material in logs, source control, or client-side usage.
- [2] (critical) config_sample.py: Hardcoded GitHub token-like credential detected (GITHUB_TOKEN). Example/config files should never contain real secrets or secret-looking values, even in samples, because they are commonly copied into production.
- [3] (critical) config.py: Hardcoded API key detected (API_KEY). Secrets must be loaded from environment variables or a secrets manager rather than committed to source control.
- [4] (critical) config.py: Hardcoded Stripe webhook secret detected (STRIPE_SECRET). Webhook and signing secrets are highly sensitive and should not be stored in code.
- [5] (critical) config.py: Hardcoded JWT secret detected (JWT_SECRET). Weak or committed JWT signing secrets can allow token forgery and full authentication compromise.

