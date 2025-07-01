from abc import abstractmethod
from typing import List, Optional, Tuple

from ._base import BaseRepositoryInterface


class RemissionsRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def search_by_tracking(
        self,
        search_str: str,
        *,
        page: int,
        limit: int,
        created_at_gt: Optional[int] = None,
        created_at_lt: Optional[int] = None,
        tenants: Optional[List[str]] = None,
        events: Optional[List[str]] = None,
    ) -> Tuple[int, List[dict]]:
        raise NotImplementedError
