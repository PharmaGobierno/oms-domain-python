from dataclasses import dataclass
from typing import Optional

from ._base import UpdatableModel, uuid_by_params
from oms.models.minified.items import ItemMin
from oms.models.minified.users import UserMin
from oms.models.submodels.remission_destinations import RemissionDestination
from oms.models.enums.remission_events import RemissionEvents


@dataclass(kw_only=True)
class RemissionsModel(UpdatableModel):
    __entity_name__ = "remissions"

    tracking_id: str
    order_id: str
    last_author: UserMin
    current_event: RemissionEvents
    current_event_timestamp: int
    original_amount: Optional[int] = None
    item: Optional[ItemMin] = None
    lote: Optional[str] = None
    destination: Optional[RemissionDestination] = None
    last_load: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()
        self._id = uuid_by_params(self.tracking_id)