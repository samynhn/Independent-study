import onnx
 
 
# Preprocessing: load the ONNX model
model_path = 'nanodet.onnx'
onnx_model = onnx.load(model_path)
 # Check the model
def checkModel(model):
    try:
        onnx.checker.check_model(model)
    except onnx.checker.ValidationError as e:
        print('The model is invalid: %s' % e)
    else:
        print('The model is valid!')

# checkModel(onnx_model)

import json
import numpy as np # we're going to use numpy to process input and output data
import onnxruntime # to inference ONNX models, we use the ONNX Runtime
import time
from PIL import Image

def load_labels(path):
    with open(path) as f:
        data = json.load(f)
    return np.asarray(data)


def preprocess(input_data):
    # convert the input data into the float32 input
    img_data = input_data.astype('float32')

    #normalize
    mean_vec = np.array([0.485, 0.456, 0.406])
    stddev_vec = np.array([0.229, 0.224, 0.225])
    norm_img_data = np.zeros(img_data.shape).astype('float32')
    for i in range(img_data.shape[0]):
        norm_img_data[i,:,:] = (img_data[i,:,:]/255 - mean_vec[i]) / stddev_vec[i]
        
    #add batch channel
    norm_img_data = norm_img_data.reshape(1, 3, 416, 416).astype('float32')
    return norm_img_data

def softmax(x):
    x = x.reshape(-1)
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def postprocess(result):
    return softmax(np.array(result)).tolist()

import cv2
# # Load the raw image
img = Image.open("test1.jpg")
img = img.resize((416, 416), Image.BILINEAR)
image_data = np.array(img).transpose(2, 0, 1) # (416,416,3) to (3,416,416)
# print(image_data.dtype)
# print(input_data.dtype)
input_data = preprocess(image_data)
# print(input_data.dtype)
# print(np.shape(input_data))

# # Run the model on the backend
session = onnxruntime.InferenceSession('nanodet.onnx', None)

# get the name of the first input of the model
input_name = session.get_inputs()[0].name  
print('Input Name:', input_name)

# Inference
start = time.time()
raw_result = session.run([], {input_name: input_data})
end = time.time()
res = postprocess(raw_result)

inference_time = np.round((end - start) * 1000, 2)
idx = np.argmax(res)

print('========================================')
print('Final top prediction is: %d'% idx)
print('========================================')

print('========================================')
print('Inference time: ' + str(inference_time) + " ms")
print('========================================')
