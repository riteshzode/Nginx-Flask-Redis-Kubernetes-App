from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def hello():
    count = r.incr("counter")
    return f"Hello, you have visited {count} times."

if __name__ == "__main__":
    app.run(host='0.0.0.0')