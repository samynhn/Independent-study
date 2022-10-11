from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing
from multiprocessing.dummy import freeze_support
import time
import queue
import numpy as np
import os
from functools import partial
NUM_OF_PROCESS = 4
zero_array = [-1]*45

def func(num, remainder):
    time.sleep(1)
    zero_array[1] = 0
    remainder = num % 8
    
    print(remainder)
    return num #remember use return


if __name__ == '__main__':
    print("num of cpus : ", os.cpu_count())
    start = time.time()

    # array = [-1,-1,-1,-1]
    # q = multiprocessing.Queue(4)
    count = 0
    remainder = []
    result = []
    input = []
    pool = Pool(8)
    for num in range(32):
                remainder.append(count%8)
                input.append(num)
                count += 1
                 #let input = [0,1,2,3,4,5,6,7] len=8
                if(len(input)==8):
                    # partial_func = partial(func, input) #partial func only for para is a value not 8 array
                    pool_outputs = pool.starmap(func, zip(input, remainder)) #input = [0,1,2,3,4,5,6,7] and parallel exe 8 input data
                    input.clear() #input = [] and redo the loop
                    remainder.clear()
                    result.extend(pool_outputs) # get 8 output to result array
                
                
                # func(num)
            # pool = multiprocessing.Pool(NUM_OF_PROCESS, func, (q,))
    print(result)
    pool.close()
    pool.join()
    end = time.time()
    
    print("the procedure time cost : ",end-start," seconds")