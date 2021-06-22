# pip install python-socketio
# This should be running in ec2 or instance
# It wont work in lamda because it uses websockets

import eventlet
import socketio
import json

sio = socketio.Server(cors_allowed_origins='*')
# app = socketio.WSGIApp(sio , static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })
flag = True
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def image(sid, data):
    try:
        if flag:
            print(data)
            flag = False
        d = json.dumps({'data': data})
        sio.emit('image1', d)
        
    except Exception as e:
        print(e)
  

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
