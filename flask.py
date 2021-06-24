# pip install python-socketio
# This should be running in ec2 or instance
# It wont work in lamda because it uses websockets

import eventlet
import socketio
import json
import base64
import cv2
import numpy as np
import time

# altchars=b'+/'

sio = socketio.Server(cors_allowed_origins='*')
# app = socketio.WSGIApp(sio , static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def image(sid, data):
    try:
        start = time.time()
        print("enetered")
        d = data["data"]
        print("len of d" , len(d))
        img_b64decode = base64.b64decode(d.split(',')[1])
        img_array = np.frombuffer(img_b64decode,np.uint8)
        print("img_array" , img_array.shape)
        img=cv2.imdecode(img_array,flags = 1)
        cv2.imwrite("pic.jpg" , img)
        writer.write(img)
        print("img shape" , img.shape)
        # d = json.dumps({'data': data})
        # sio.emit('image1', d)
        print("time taken for frame" , time.time()-start)
    except Exception as e:
        print(e)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    writer = cv2.VideoWriter("video.avi" , cv2.VideoWriter_fourcc(*"MJPG") , 20 , (360 , 270))
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 80)), app)
    writer.release()
