# pip install python-socketio
# This should be running in ec2 or instance
# It wont work in lamda because it uses websockets

import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio , cors_allowed_origins="*")

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def image(sid, data):
  print(data)
  

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
