import os
from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)
redis_client = Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)


@app.get("/health")
def health():
    return jsonify(status="ok", service="songs-api")


@app.post("/api/play")
def play():
    redis_client.rpush("song_queue", "next_song")
    return jsonify(message="Song queued")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
