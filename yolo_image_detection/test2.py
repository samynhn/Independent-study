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

from demo import *
from demo_darknet2onnx import *
from tool.darknet2onnx import *
from tool.utils import *

NUMBER_OF_PROCESSES = 8
NUMBER_OF_THREADS = 8
NUMBER_OF_JOBS = NUMBER_OF_PROCESSES*NUMBER_OF_THREADS

img1 = Image.open("../sourse/test1.jpg")
img2 = Image.open("../sourse/test3.jpg")

img1_arr=cv2.cvtColor(np.array(img1),cv2.COLOR_RGB2BGR)
img2_arr=cv2.cvtColor(np.array(img2),cv2.COLOR_RGB2BGR)


def detect(img_array):
    t_pool =ThreadPool(NUMBER_OF_THREADS)
    t_pool_outputs = t_pool.map(plot, (img_array)) 
    t_pool.close()
    t_pool.join()

time_arr = []

# NUMBER_OF_PROCESSES = 8
# NUMBER_OF_THREADS = 8
# NUMBER_OF_JOBS = 8
################################
if __name__ == '__main__':

    for i in range(64):
        index = i+1
        if(64%(index)==0):
            NUMBER_OF_PROCESSES = int(index)
            NUMBER_OF_THREADS = int(64/index)
            if(NUMBER_OF_PROCESSES<9):
                print(NUMBER_OF_PROCESSES)
                print(NUMBER_OF_THREADS)

                img_array = []
                input_array = []
                for i in range(NUMBER_OF_THREADS):
                    img_array.append(img1_arr)
                
                for i in range(NUMBER_OF_PROCESSES):
                    input_array.append(img_array)
                
                m_pool = Pool(NUMBER_OF_PROCESSES)
                start = time.time()
                t_pool_outputs = m_pool.map(detect, (input_array)) 
                m_pool.close()
                m_pool.join()
                end = time.time()
                time_arr.append(end-start)
                print("## 1.Cost : ", end-start, "second")

    print(time_arr)
################################

    # start1 = time.time()
    # for i in range(NUMBER_OF_JOBS):
    #     plot(img1_arr)
    
    # end1 = time.time()
    # print("## 2.Cost : ", end1-start1, "second")

