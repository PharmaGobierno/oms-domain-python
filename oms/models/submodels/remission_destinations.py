from dataclasses import dataclass
from typing import Optional, Literal

@dataclass
class RemissionDestination:
    id: str
    version: Literal["1.0.0"] = "1.0.0"
    name: Optional[str] = None
    company: Optional[str] = None
