import socket
import pickle
import json
import base64
import cv2
import numpy as np
from PIL import Image

# cap = cv2.VideoCapture('./sourse/test.mp4')

# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter('./outputVideo/output.avi',fourcc, 20.0, (416,416))

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

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         opencv_image = cv2.resize(frame, (416, 416))
#         out.write(opencv_image)

#         cv2.imshow('frame',opencv_image)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
      
# cap.release()
# out.release()
# cv2.destroyAllWindows()
img1 = Image.open("../sourse/test1.jpg")
jstr1 = im2json(img1)
img = json2im(jstr1)
img.show()