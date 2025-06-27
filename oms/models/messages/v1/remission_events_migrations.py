from dataclasses import dataclass
from typing import Dict

from ._enums import ResmissionMigrationOrigins
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionEventMigrationsPubsubMessage(BasePubsubMessage):
    payload: dict
    tracking_id: str
    event: str
    origin: ResmissionMigrationOrigins
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "remission-event-migrations"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {**default_attributes, "origin": self.origin.value, "event": self.event}
