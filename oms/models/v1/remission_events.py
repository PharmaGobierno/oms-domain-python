from dataclasses import dataclass
from typing import Optional, List

from ._base import UpdatableModel, uuid_by_params
from oms.models.minified.users import UserMin
from oms.models.submodels.remission_evidences import RemissionEvidence
from oms.models.submodels.remission_event_notes import RemissionEventNote
from oms.models.enums.remission_events import RemissionEvents


@dataclass(kw_only=True)
class RemissionEventsModel(UpdatableModel):
    __entity_name__ = "remission-events"

    remission_id: str
    tracking_id: str
    event: RemissionEvents
    event_timestamp: int
    author: UserMin
    evidences: List[RemissionEvidence]
    load_id: Optional[str] = None
    loaded_amount: Optional[int] = None
    delivered_amount: Optional[int] = None
    metadata: Optional[dict] = None
    event_note: Optional[RemissionEventNote] = None
    


    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id, self.event, self.event_timestamp)