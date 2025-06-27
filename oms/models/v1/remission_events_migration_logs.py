from dataclasses import dataclass

from ._base import BaseModel, uuid_by_params
from ._enums import ResmissionMigrationOrigins


@dataclass(kw_only=True)
class RemissionEventsMigrationLogsModel(BaseModel):
    __entity_name__ = "remission-events-mirgration-logs"

    payload: dict
    tracking_id: str
    origin: ResmissionMigrationOrigins
    origin_timestamp: int

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.origin_timestamp, self.origin.value)
