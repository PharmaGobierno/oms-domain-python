from dataclasses import dataclass

from typing import Dict, Optional

from pharmagob.v1.models.shipment import ShipmentModel

@dataclass(kw_only=True)
class ShipmentStatusPubsubMessage(BasePubsubMessage):
    payload: ShipmentModel
    status: str
    origin: str
    items: Optional[list[dict]] = None
    version: str = "1"

    @classmethod
    def topic(cls) -> str:
        return "shipment-status"

    def get_attributes(self) -> Dict[str, str]:
        default_attributes = super().get_attributes()
        return {**default_attributes, "origin": self.origin, "status": self.status}
