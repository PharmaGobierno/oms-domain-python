from dataclasses import dataclass
from typing import List, Optional

from ._base import BaseModel, uuid_by_params
from ._enums import ResmissionMigrationOrigins


@dataclass(kw_only=True)
class RemissionEventsMigrationLogsModel(BaseModel):
    __entity_name__ = "remission-events-mirgration-logs"

    tracking_id: str
    origin_type: ResmissionMigrationOrigins
    origin_id: Optional[str] = None
    origin_timestamp: int
    events: List[str]
    migration_payload: dict

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.origin_timestamp, self.origin_id)
