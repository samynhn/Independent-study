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
from multiprocessing.pool import ThreadPool

from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing as mp

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
img1 = Image.open("../sourse/test1.jpg")
img2 = Image.open("../sourse/test3.jpg")

img1_arr=cv2.cvtColor(np.array(img1),cv2.COLOR_RGB2BGR)
img2_arr=cv2.cvtColor(np.array(img2),cv2.COLOR_RGB2BGR)
# jstr1 = im2json(img1)
# img1=json2im(jstr1)
# img1=255*np.array(img1).astype("uint8")

def func(array):
    time.sleep(1)
    print("good")

def detect(img_array):
    pool =ThreadPool(8)
    pool_outputs = pool.map(plot, (img_array)) 
    pool.close()
################################
if __name__ == '__main__':
    # img_array = []
    # input_array = []

    # img_array.append(img1_arr)
    # img_array.append(img2_arr)
    # img_array.append(img1_arr)
    # img_array.append(img2_arr)
    # img_array.append(img1_arr)
    # img_array.append(img2_arr)
    # img_array.append(img1_arr)
    # img_array.append(img2_arr)

    # input_array.append(img_array)
    # input_array.append(img_array)
    # input_array.append(img_array)
    # input_array.append(img_array)
    # input_array.append(img_array)
    # input_array.append(img_array)
    # input_array.append(img_array)
    # input_array.append(img_array)
    # pool = Pool(8)
    # start = time.time()
    # pool_outputs = pool.map(detect, (input_array)) 
    # end = time.time()
    # print("## 1.Cost : ", end-start, "second")

################################


# if __name__ == '__main__':
#     img_array = []
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
    

#     pool = Pool()
#     start = time.time()
#     pool_outputs = pool.map(plot, (img_array)) 
#     end = time.time()
#     print("## 1.Cost : ", end-start, "second")

################################
    start1 = time.time()
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)

    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)

    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)

    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)

    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)

    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    plot(img1_arr)
    plot(img2_arr)
    end1 = time.time()
    print("## 2.Cost : ", end1-start1, "second")

################################

# if __name__ == '__main__':
    
#     img_array = []
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     img_array.append(img1_arr)
#     img_array.append(img2_arr)
#     # pool =ThreadPool(8)

#     start3 = time.time()
#     # pool_outputs = pool.map(plot, (img_array)) 
#     detect(img_array)
#     end3 = time.time()
#     print("## 4.Cost : ", end3-start3, "second")
################################

