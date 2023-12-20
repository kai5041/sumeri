from hashlib import sha256


class Transaction:
    def __init__(
        self,
        sender_public_key: str,
        sender_public_address: str,
        receiver_public_address: str,
        amount: int,
        timestamp: int,
        id: int,
    ):
        self.sender_public_key = sender_public_key
        self.sender_public_address = sender_public_address
        self.receiver_public_address = receiver_public_address
        self.amount = amount
        self.timestamp = timestamp
        self.id = id

    @property
    def header(self) -> str:
        return f"{self.sender_public_key} {self.sender_public_address} {self.receiver_public_address} {self.amount} {self.timestamp} {self.id}"

    @property
    def hash(self) -> str:
        return sha256(self.header.encode('utf-8')).hexdigest()


Tx = Transaction
