import os
from typing import cast
from redis import StrictRedis


def get_redis_client() -> StrictRedis:
    redis_host: str = cast(str, os.environ.get("REDIS_HOST", "localhost"))
    redis_port: int = cast(int, os.environ.get("REDIS_PORT", 6379))
    primary_db: int = cast(int, os.environ.get("REDIS_DB_INDEX", 0))

    return StrictRedis(host=redis_host, port=redis_port, db=primary_db)