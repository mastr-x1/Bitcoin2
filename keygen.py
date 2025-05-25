from cryptography.hazmat.primitives.asymmetric import ed25519
import base64

def generate_wallet():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    address = base64.b64encode(public_key.public_bytes_raw()).decode()
    return private_key, public_key, address