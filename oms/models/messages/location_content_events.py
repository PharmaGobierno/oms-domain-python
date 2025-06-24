
from dataclasses import dataclass
from typing import Dict
from pharmagob.v1.models.location_content import LocationContentModel

@dataclass(kw_only=True)
class LocationContentEventsPubsubMessage(BasePubsubMessage):
    payload: LocationContentModel
    event: str
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "location-content-events"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {**default_attributes, "event": self.event}