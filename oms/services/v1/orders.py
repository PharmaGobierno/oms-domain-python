from oms.models.v1.orders import OrdersModel
from oms.repository_interfaces.v1.orders import (
    OrderRepositoryInterface,
)

from ._base import BaseService


class OrdersService(
    BaseService[OrdersModel, OrderRepositoryInterface]
):
    __model__ = OrdersModel
