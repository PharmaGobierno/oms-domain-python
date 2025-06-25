from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class RemissionEvidence:
    value: str
    version: Literal["1.0.0"] = "1.0.0"
    type: Optional[str] = None
    validation_timestamp: Optional[int] = None
    validation_status: Optional[str] = None  # TODO: Define enum
