#!flask/bin/python
from flask import Flask, request
import redis
import os

app = Flask(__name__)

# Get Redis connection details from environment variables
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_DB = int(os.environ.get("REDIS_DB", 0))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

COUNTER_KEY = "counter"

def get_counter():
    value = r.get(COUNTER_KEY)
    return int(value) if value else 0

def increment_counter():
    return r.incr(COUNTER_KEY)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        new_value = increment_counter()
        return f"Hmm, Plus 1 please. Counter is now: {new_value}"
    else:
        return f"Our counter is: {get_counter()} "

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
