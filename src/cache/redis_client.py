import redis
import time

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

redis_client.set("framework", "fastapi", ex=30)

for i in range(5):
    print(redis_client.ttl("framework"))
    time.sleep(3)