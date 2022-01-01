import multiprocessing as mp
import torch

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

check_type_length()