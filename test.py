import multiprocessing as mp
import torch
import json
import base64

def check_gpu_detail():
    print('If GPU available : ',torch.cuda.is_available()) # true check GPU if available
    print('The num of GPU : ', torch.cuda.device_count()) # num of GPU
    print('The current GPU index : ', torch.cuda.current_device())# the current GPU index
    for index in range(torch.cuda.device_count()):
        print('GPU name : ',torch.cuda.get_device_name(index)) # print GPU name
# check_gpu_detail()

def check_type_length():
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "192.168.1.26"
    ADDR = (SERVER, PORT)

    msg = "hello world"
    message = msg.encode(FORMAT) # convert string to bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # convert string to bytes
    send_length += b' ' * (HEADER - len(send_length))
    print(len(send_length))

# check_type_length()


import pickle
import json
import base64

# data = {}
# with open('test.jpg', mode='rb') as file:
#     img = file.read()
# data['img'] = base64.encodebytes(img).decode('utf-8')
def im2json(im):
    imdata = pickle.dumps(im)
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('utf-8')})
    return jstr

def json2im(jstr):
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im


from PIL import Image
img = Image.open("test.jpg")
jstr = im2json(img)
result_img = json2im(jstr)
result_img.show()
############# method 2 #############
# import cv2
# img = cv2.imread('test.jpg')
# jstr = im2json(img)
# result_img = json2im(jstr)
# cv2.imshow('test.jpg', result_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
############# method 3 #############
# import matplotlib.pyplot as plt
# img = plt.imread('test.jpg')
# jstr = im2json(img)
# result_img = json2im(jstr)
# plt.imshow(result_img)
