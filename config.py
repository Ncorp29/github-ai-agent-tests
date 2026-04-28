# ❗ Sensitive data exposure test case

import os

API_KEY = os.getenv("API_KEY")
STRIPE_SECRET = os.getenv("STRIPE_SECRET")
JWT_SECRET = os.environ["JWT_SECRET"]

# TODO: AI fix suggestion (hxi31h8t): Review and improve: Hardcoded Stripe webhook secret detected (STRIPE_SECRET). Webhook and signing secrets are highly sensitive and should not be stored in code.