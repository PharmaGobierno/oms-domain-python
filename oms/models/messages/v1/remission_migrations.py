
from dataclasses import dataclass
from typing import Dict

from oms.models.v1.remissions import RemissionsModel

from ._enums import ResmissionMigrationOrigins
from .base_publisher import BasePubsubMessage


@dataclass(kw_only=True)
class RemissionMigrationsPubsubMessage(BasePubsubMessage):
    payload: RemissionsModel
    origin: ResmissionMigrationOrigins
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "remission-migrations"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {**default_attributes, "origin": self.origin}
