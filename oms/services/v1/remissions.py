from oms.models.v1.remissions import RemissionsModel
from oms.repository_interfaces.v1.remissions import RemissionsRepositoryInterface

from ._base import BaseService


class RemissionsService(BaseService[RemissionsModel, RemissionsRepositoryInterface]):
    __model__ = RemissionsModel
