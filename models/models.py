from dataclasses import dataclass, field
from datetime import datetime
from bson import ObjectId
from typing import List, Dict

@dataclass

class Conversation :
    id: ObjectId = field(default_factory=ObjectId, init=False)
    user_id: str = field(default_factory=str)
    messages: List[Dict] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if not isinstance(self.id, ObjectId):
            self.id = ObjectId(self.id) if self.id else ObjectId()
        self.created_at = datetime.utcnow() if not self.created_at else self.created_at

