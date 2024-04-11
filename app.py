# ###flask app for hello world docker

# from flask import Flask 
# import os
# app=Flask(__name__)

# @app.route('/',methods=['GET'])
# def home():
#     return "Hello World"

# if __name__ == "__main__":
#     app.run(debug=True,host="0.0.0.0",port=5000)
     

import time
import redis

from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            # cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello Khushboo!! I have seen {} times.\n'.format(count)