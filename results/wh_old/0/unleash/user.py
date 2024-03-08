from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    username: str
    online_status: bool