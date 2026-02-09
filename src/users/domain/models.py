from dataclasses import dataclass
from typing import Any

@dataclass
class User:
    id: int | None
    email: str
    is_active: bool = True

    @classmethod
    def from_primitives(cls, data: dict[str, Any]) -> "User":
        return cls(
            id=data.get("id"),
            email=data["email"],
            is_active=data.get("is_active", True)
        )

    def to_primitives(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
        }
