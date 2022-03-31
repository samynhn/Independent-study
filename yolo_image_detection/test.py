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
import json
import argparse
from PIL import Image 

# from PIL import Image
#import pycuda.driver as cuda
#import pycuda.autoinit
from demo import *
from demo_darknet2onnx import *
from tool.darknet2onnx import *
from tool.utils import *
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
img1 = Image.open("../sourse/dog.jpg")
jstr1 = im2json(img1)
img1=json2im(jstr1)
img1=255*np.array(img1).astype("uint8")

#img=cv2.imread("/Users/kwochengho/Downloads/new_folder/Independent-study/sourse/dog.jpg")
plot("files/coco.names","/Users/kwochengho/Downloads/new_folder/Independent-study/imageWay/yolov4_1_3_416_416_static.onnx",img1)
#"/Users/kwochengho/Downloads/new_folder/Independent-study/sourse/dog.jpg"