from oms.models.v1.remissions import RemissionsModel
from oms.repository_interfaces.v1.remissions import \
    RemissionRepositoryInterface

from ._base import BaseService


class RemissionEventsService(
    BaseService[RemissionsModel, RemissionRepositoryInterface]
):
    __model__ = RemissionsModel
