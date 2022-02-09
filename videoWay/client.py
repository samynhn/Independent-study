import socket
import pickle
import json
import base64
import cv2
import numpy as np
from PIL import Image
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

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

# img1 = Image.open("test1.jpg")
# jstr1 = im2json(img1)
# img2 = Image.open("test2.jpg")
# jstr2 = im2json(img2)
# img3 = Image.open("test3.jpg")
# jstr3 = im2json(img3)
# img4 = Image.open("test4.jpg")
# jstr4 = im2json(img4)
# img5 = Image.open("test5.jpg")
# jstr5 = im2json(img5)
# # result_img = json2im(jstr)

# input()
# send(jstr1)
# input()
# send(jstr2)
# input()
# send(jstr3)
# input()
# send(jstr4)
# input()
# send(jstr5)
# input()

cap = cv2.VideoCapture('../sourse/test.mp4')
count = 1

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret is True:
    count += 1
    if(count%7==0):
      opencv_image = cv2.resize(frame, (416, 416))
      color_coverted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
      pil_image=Image.fromarray(color_coverted)
      jstr = im2json(pil_image)
      send(jstr)
      
      
    else:      
      continue
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else: # when ret == False(when video is over) , we must make it jump off the while loop manually.
    break

cap.release()
cv2.destroyAllWindows()
send(DISCONNECT_MESSAGE)