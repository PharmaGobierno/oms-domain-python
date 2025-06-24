from dataclasses import asdict, dataclass
from time import time
from typing import Any, Dict, Optional

@dataclass
class BasePubsubMessage:
    payload: Any
    origin_timestamp: int
    author: min_models.UserMin
    version: str
    published_at: int = round(time() * 1000)
    context: Optional[dict] = None

    def dict(self):
        return asdict(self)

    @classmethod
    def topic(cls) -> str:
        raise NotImplementedError

    def get_attributes(self) -> Dict[str, str]:
        return {"topic": self.topic(), "version": self.version}
