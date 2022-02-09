import socket 
import threading
import pickle
import json
import base64
import numpy as np    # we're going to use numpy to process input and output data
import cv2
import time
HEADER = 64
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def im2json(im):
    imdata = pickle.dumps(im)
    # print(type(imdata))
    # print(len(imdata))
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('utf-8')})
    return jstr

def json2im(jstr):
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    # print(len(jstr))
    # print(len(imdata))
    im = pickle.loads(imdata)
    return im
    

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    # print("e")
    # time.sleep(1)
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # first connection msg must be header
        # time.sleep(0.001)
        if msg_length: #avoid msg haven't been catched or no content in it
            time.sleep(0.0001)# ensure video being loaded already
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)# after first msg is header, others msg are messager
            if msg == DISCONNECT_MESSAGE: #close connection
                connected = False
                conn.send("Finish".encode(FORMAT))
            else:
                pil_img = json2im(msg)
                # pil_img.show()
                numpy_image=np.array(pil_img)
                opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
                cv2.imshow('output', opencv_image)
                cv2.waitKey(1)
                
            # print(f"[{addr}] {msg}")
            conn.send("Msg received by server2".encode(FORMAT))
    cv2.destroyAllWindows()
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