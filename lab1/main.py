from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def hello():
    count = redis_client.incr('hits')
    return f'''
    <html>
        <body style="text-align: center; font-family: Arial; padding: 50px;">
            <h1>Страничка в интернете</h1>
            <h2>Количество посещений: {count}</h2>
            <p>Контейнер ID: {os.environ.get('HOSTNAME', 'Unknown')}</p>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)