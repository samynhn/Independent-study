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
from demo import *
from demo_darknet2onnx import *
from tool.darknet2onnx import *
from tool.utils import *
plot("files/coco.names","/Users/kwochengho/Downloads/new_folder/Independent-study/imageWay/yolov4_1_3_416_416_static.onnx","/Users/kwochengho/Downloads/new_folder/Independent-study/sourse/dog.jpg")