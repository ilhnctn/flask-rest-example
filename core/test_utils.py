from fakeredis import FakeStrictRedis


def get_fake_redis() -> FakeStrictRedis:
    return FakeStrictRedis(host="localhost", port=6379, db=0)
