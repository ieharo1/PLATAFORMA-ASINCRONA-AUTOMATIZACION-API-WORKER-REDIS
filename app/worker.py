import os
import time
from redis import Redis

redis_client = Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

while True:
    song = redis_client.lpop("song_queue")
    if song:
        print(f"[worker] playing: {song}")
    time.sleep(2)
