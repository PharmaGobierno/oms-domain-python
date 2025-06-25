from oms.models.v1.remission_events import RemissionEventsModel
from oms.repository_interfaces.v1.remission_events import \
    RemissionEventRepositoryInterface

from ._base import BaseService


class RemissionEventsService(
    BaseService[RemissionEventsModel, RemissionEventRepositoryInterface]
):
    __model__ = RemissionEventsModel
