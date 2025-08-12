from flask import Flask, request
import redis

app = Flask(__name__)

# Connect to Redis service by DNS name (redis) and default port 6379
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        r.incr('counter')  # Increment counter in Redis
        return "Hmm, Plus 1 please test1"
    else:
        count = r.get('counter')
        if count is None:
            count = 0
        else:
            count = int(count)
        return f"Our counter is: {count} test1"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')