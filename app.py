# import os
# import redis
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
# r = redis.from_url(os.environ['REDIS_URL'])

@app.route("/")
def hello():
    return 'Hello, World!'

@socketio.on('connect')
def onConnect():
    print('connect', request)
    print('connect', request.sid)
    # r.sadd('conn', request.sid)

@socketio.on('disconnect')
def onDisconnect():
    print('disconnect', request)
    print('disconnect', request.sid)
    # r.srem('conn', request.sid)

@socketio.event
def test():
    send(request.sid)

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print(e)
