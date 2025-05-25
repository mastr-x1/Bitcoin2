from cryptography.hazmat.primitives.asymmetric import ed25519
import base64

class Wallet:
    def __init__(self):
        self.private_key = ed25519.Ed25519PrivateKey.generate()
        self.public_key = self.private_key.public_key()

    def get_address(self):
        return base64.b64encode(self.public_key.public_bytes_raw()).decode()

    def sign_transaction(self, message: bytes):
        signature = self.private_key.sign(message)
        return base64.b64encode(signature).decode()