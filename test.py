import multiprocessing as mp
import torch

def check_gpu_detail():
    print('If GPU available : ',torch.cuda.is_available()) # true check GPU if available
    print('The num of GPU : ', torch.cuda.device_count()) # num of GPU
    print('The current GPU index : ', torch.cuda.current_device())# the current GPU index
    for index in range(torch.cuda.device_count()):
        print('GPU name : ',torch.cuda.get_device_name(index)) # print GPU name
check_gpu_detail()