import numpy as np    # we're going to use numpy to process input and output data
import onnxruntime    # to inference ONNX models, we use the ONNX Runtime
import onnx
from onnx import numpy_helper
import urllib.request
import json
import time

import pandas as pd
from imageio import imread
import warnings
warnings.filterwarnings('ignore')
# display images in notebook
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import matplotlib.patches as patches

ssd_onnx_model = r"nanodet.onnx"
tiny_yolov3_onnx_model = r"nanodet.onnx"
img_file = r"test1.jpg"

# Preprocess and normalize the image
def preprocess(img_file, w, h):
    input_shape = (1, 3, w, h)
    img = Image.open(img_file)
    img = img.resize((w, h), Image.BILINEAR)
    # convert the input data into the float32 input
    img_data = np.array(img)
    img_data = np.transpose(img_data, [2, 0, 1])
    img_data = np.expand_dims(img_data, 0)
    mean_vec = np.array([0.485, 0.456, 0.406])
    stddev_vec = np.array([0.229, 0.224, 0.225])
    norm_img_data = np.zeros(img_data.shape).astype('float32')
    for i in range(img_data.shape[1]):
        norm_img_data[:,i,:,:] = (img_data[:,i,:,:]/255 - mean_vec[i]) / stddev_vec[i]
    return norm_img_data.astype('float32'), np.array(img)

#%% SSD模型推理

def infer_ssd(onnx_model:str):
    # Run the model on the backend
    session = onnxruntime.InferenceSession(onnx_model, None)
    
    # get the name of the first input of the model
    input_name = session.get_inputs()[0].name  
    output_name = session.get_outputs()[0].name  
    # print(len(session.get_outputs()))
    print('Input Name:', input_name)
    print('Output Name:', output_name)
    # 符合https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/ssd 模型的輸入要求
    input_data, raw_img = preprocess(img_file, 416, 416)
    print('輸入影象大小：', input_data.shape)
    
    start = time.time()
    raw_result = session.run([], {
   
   input_name: input_data})
    end = time.time()
    print('推理時間：', end-start,'s')
    print(np.shape(raw_result))
    bboxes = np.squeeze(raw_result[0]) # 200x4
    labels = raw_result[3].T # 200x1
    scores = raw_result[2].T # 200x1，結構已經按照得分從高到低的順序排列
    
    
    fig, ax = plt.subplots(1)
    ax.imshow(raw_img)
    
    LEN = np.sum(np.where(scores>0.6,1,0))
    
    for k in range(LEN):
        
        x1 = 416*bboxes[k][0]
        y1 = 416*bboxes[k][1]
        x2 = 416*bboxes[k][2]
        y2 = 416*bboxes[k][3]
        rect = patches.Rectangle((x1,y1),x2-x1,y2-y1,linewidth=1,edgecolor='r',fill=False)
        
        ax.add_patch(rect)
    
    plt.show()

infer_ssd(ssd_onnx_model)
#%% yolov3-tiny模型推理

def infer_tiny_yolov3(onnx_model:str):
    
    # Run the model on the backend
    session = onnxruntime.InferenceSession(onnx_model, None)
    
    # get the name of the first input of the model
    input_name = session.get_inputs()[0].name  
    output_name = session.get_outputs()[0].name  
    # print(len(session.get_outputs()))
    print('Input Name:', input_name)
    print('Output Name:', output_name)
    
    # 符合https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/tiny-yolov3 模型的輸入要求
    input_data, raw_img = preprocess(img_file, 618, 618)
    print('輸入資料大小：', input_data.shape)
    print('輸入資料型別：', input_data.dtype)
    image_size = np.array([raw_img.shape[1], raw_img.shape[0]], dtype=np.float32).reshape(1, 2)
    print('輸入影象大小：', image_size.shape)
    start = time.time()
    raw_result = session.run([], {
   
   input_name: input_data,
                                  'image_shape':image_size})
    end = time.time()
    print('推理時間：', end-start,'s')
    
# infer_tiny_yolov3(tiny_yolov3_onnx_model)