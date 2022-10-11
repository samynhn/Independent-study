import socket 
import threading
import pickle
import json
import base64
import numpy as np    # we're going to use numpy to process input and output data
import cv2
import time
import sys
import os
import argparse
# from PIL import Image
#import pycuda.driver as cuda
#import pycuda.autoinit
from demo_darknet2onnx import *
from tool.darknet2onnx import *
from tool.utils import *
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

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

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # first connection msg must be header
        if msg_length: #avoid msg haven't been catched or no content in it
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)# after first msg is header, others msg are messager
            if msg == DISCONNECT_MESSAGE: #close connection
                connected = False
                print("connected false")
            else:
                img = json2im(msg)
                #img.show()
                start = time.time()
                plot("files/coco.names","yolov4_1_3_416_416_static.onnx",img)
                end = time.time()
                print("single time: ", end-start," second")
                # print(msg)
            # print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True: # infinite loop
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()