# Authentication config
import os

def get_token():
    client_secret = os.getenv("AZURE_CLIENT_SECRET")
    return client_secret