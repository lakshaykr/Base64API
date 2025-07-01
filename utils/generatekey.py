import secrets
import string

def generate_api_key(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
