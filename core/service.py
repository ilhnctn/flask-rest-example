import os

from typing import Any, cast, Dict, Optional, List

from redis import StrictRedis
from logging import getLogger

logger = getLogger(__name__)

DEFAULT_TTL: int = cast(int, os.environ.get("DEFAULT_TTL", 60 * 60))


class BaseService:
    pass


class CacheService:
    def __init__(self, r_client: StrictRedis) -> None:
        self.client = r_client

    def set_cache(self, key: str, value: Any, ttl: int = DEFAULT_TTL) -> Any:
        return self.client.set(name=key, value=value, px=ttl * 1000)

    def hm_set(self, key: str, data: Dict[Any, Any]) -> Any:
        return self.client.hmset(name=key, mapping=data)

    def hm_get(self, name: str, keys: List[Any]) -> Any:
        return self.client.hmget(name=name, keys=keys)

    def get(self, key: str) -> Optional[Any]:
        return self.client.get(name=key)

    def increment(self, key: str, amount: int) -> Any:
        return self.client.incr(name=key, amount=amount)

    def keys(self, pattern: str = '*') -> Any:
        return self.client.keys(pattern=pattern)
