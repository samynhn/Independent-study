import socket
import pickle
import json
import base64
import time
import cv2
import numpy as np
from PIL import Image
HEADER = 64
PORT = 5050
PORT2 = 5060#to server2
PORT3 = 5070
PORT4 = 5080

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
ADDR2 = (SERVER, PORT2)#to server2
ADDR3 = (SERVER, PORT3)
ADDR4 = (SERVER, PORT4)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#to server2
client2.connect(ADDR2)#to server2

# client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client3.connect(ADDR3)

# client4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client4.connect(ADDR4)


def send(msg, remainder):
    if(remainder==0):
        message = msg.encode(FORMAT) # convert string to bytes
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length)) # make length == 64 bytes 
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))
    elif(remainder==1):
        message = msg.encode(FORMAT) # convert string to bytes
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length)) # make length == 64 bytes 
        client2.send(send_length)
        client2.send(message)
        print(client2.recv(2048).decode(FORMAT))
    # elif(remainder==2):
    #     message = msg.encode(FORMAT) # convert string to bytes
    #     msg_length = len(message)
    #     send_length = str(msg_length).encode(FORMAT)
    #     send_length += b' ' * (HEADER - len(send_length)) # make length == 64 bytes 
    #     client3.send(send_length)
    #     client3.send(message)
    #     print(client3.recv(2048).decode(FORMAT))
    # elif(remainder==3):
    #     message = msg.encode(FORMAT) # convert string to bytes
    #     msg_length = len(message)
    #     send_length = str(msg_length).encode(FORMAT)
    #     send_length += b' ' * (HEADER - len(send_length)) # make length == 64 bytes 
    #     client4.send(send_length)
    #     client4.send(message)
    #     print(client4.recv(2048).decode(FORMAT))

def im2json(im):
    imdata = pickle.dumps(im)
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('utf-8')})
    return jstr

def json2im(jstr):
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im
def transfer(frame, remainder):
    opencv_image = cv2.resize(frame, (416, 416))
    color_coverted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(color_coverted)
    jstr = im2json(pil_image)
    send(jstr,remainder)

cap = cv2.VideoCapture('../sourse/test.mp4')
count = 1
single_transfer_time = [0,0]
start = time.time()
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret is True:
    count += 1
    #video to the model1
    if(count%2==0):
        transfer(frame, 0) #0.015s
    #video to the model1
    elif(count%2==1):   
        transfer(frame, 1)
    
    # elif(count%4==2):      
    #     transfer(frame, 2)

    # elif(count%4==3):      
    #     transfer(frame, 3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else: # when ret == False(when video is over) , we must make it jump off the while loop manually.
    
    break

end = time.time()
print("Total Time : ",end- start)

cap.release()
cv2.destroyAllWindows()
send(DISCONNECT_MESSAGE,0)
send(DISCONNECT_MESSAGE,1)
# send(DISCONNECT_MESSAGE,2)
# send(DISCONNECT_MESSAGE,3)



# 