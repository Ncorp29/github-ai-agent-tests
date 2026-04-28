# ❗ Sensitive data exposure test case

import os

API_KEY = os.getenv("API_KEY", "")
STRIPE_SECRET = os.getenv("STRIPE_SECRET", "")
JWT_SECRET = os.getenv("JWT_SECRET", "")

# TODO: AI fix suggestion (o6thow71): Review and improve: Hardcoded Stripe webhook secret in source code. This is highly sensitive and should be rotated immediately if real. Load from secure configuration instead of committing it to the repository.