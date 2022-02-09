import socket
import pickle
import json
import base64
import cv2
import numpy as np
from PIL import Image
import struct
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)



def send(msg):
    message = msg.encode(FORMAT) # convert string to bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # make length == 64 bytes 
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def im2json(im):
    imdata = pickle.dumps(im)
    print(type(imdata))
    print(len(imdata))
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('utf-8')})
    return jstr

def json2im(jstr):
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im

cap = cv2.VideoCapture('test.mp4')
count = 1
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret is True:
    count += 1
    if(count%100==0):
        opencv_image = cv2.resize(frame, (416, 416))
        a = pickle.dumps(opencv_image)
        message = struct.pack("Q",len(a))+a
        frame1 = pickle.loads(a)
        print(len(a))
        print(len(message))
        cv2.imshow("RECEIVING VIDEO",frame1)
        # cv2.imshow('output', opencv_image)
        cv2.waitKey(100)      
      
    else:      
      continue
  
    if cv2.waitKey(11) & 0xFF == ord('q'):
      break
  else: # when ret == False(when video is over) , we must make it jump off the while loop manually.
    break

# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture('test.mp4')
# count = 1
# while(cap.isOpened()):
#   ret, frame = cap.read()
#   if ret is True:
#     count += 1
#     if(count%2==0):
#         opencv_image = cv2.resize(frame, (416, 416))
#         color_coverted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
#         pil_image=Image.fromarray(color_coverted)
#         jstr = im2json(pil_image)
#         pil_img = json2im(jstr)
#         numpy_image=np.array(pil_img)
#         opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
#         cv2.imshow('output', opencv_image)
#         cv2.waitKey(1)      
      
#     else:      
#       continue
  
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#       break
#   else: # when ret == False(when video is over) , we must make it jump off the while loop manually.
#     break

# cap.release()