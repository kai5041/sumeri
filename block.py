from transaction import Transaction
from hashlib import sha256


class Block:
    def __init__(
        self,
        height: int,
        transactions: list[Transaction],
        timestamp: int,
        reward: int,
        parent_hash: str,
    ):
        self.height = height
        self.transactions = transactions
        self.timestamp = timestamp
        self.reward = reward
        self.parent_hash = parent_hash

    @property
    def hash(self) -> str:
        return sha256(
            f"{self.parent_hash} {' '.join(tx.hash for tx in self.transactions)}".encode(
                "utf-8"
            )
        ).hexdigest()
