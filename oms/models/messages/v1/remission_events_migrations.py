from dataclasses import dataclass
from typing import Dict

from ._enums import ResmissionMigrationOrigins
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionEventMigrationsPubsubMessage(BasePubsubMessage):
    payload: dict
    tracking_id: str
    remission_id: str
    migration_log_id: str
    event: str
    origin: ResmissionMigrationOrigins
    origin_id: str
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "oms-remission-event-migrations"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {
            **default_attributes,
            "origin": self.origin.value,
            "origin_id": self.origin_id,
        }
