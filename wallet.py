from ecdsa import SigningKey, VerifyingKey, SECP256k1


class Wallet:
    def __init__(self, private_key: SigningKey = None):
        self.private_key = private_key 

    @property
    def public_key(self):
        return self.private_key.get_verifying_key()

    def get_private_key_str(self) -> str:
        return self.private_key.to_string().hex()
  
    def get_public_key_str(self) -> str:
        return self.public_key.to_string().hex()

    def generate(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)


    def sign(self, msg: str):
        return self.private_key.sign(msg.encode("utf-8"))

# test

wallet = Wallet(SigningKey.generate(SECP256k1))