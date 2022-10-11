# list1 = [[1,2,3,4], [5,6,6,6]]
# list2 = [[7,7,7,7,7,7,7], [5,6,6,6]]

# a = [1]
# b =  [1]
# # a.append(list1)
# # a.append(list2) 
# # #[1, [[1, 2, 3, 4], [5, 6, 6, 6]], [[7, 7, 7, 7, 7, 7, 7], [5, 6, 6, 6]]]

# # b.extend(list1)
# # b.extend(list2)
# # #[1, [1, 2, 3, 4], [5, 6, 6, 6], [7, 7, 7, 7, 7, 7, 7], [5, 6, 6, 6]]

# # print(len(a)) #3
# # print(len(b)) #5
# a.append(6%1)

# print(a)



#####################################################

from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing as mp
import time

def func(array):
    time.sleep(1)
    print("fuck")
if __name__ == '__main__':
    p_list = []
    p1 = mp.Process(target=func, args=[2])
    # p_list.append(p1)

    p2 = mp.Process(target=func, args=[2])
    # p_list.append(p2)

    p3 = mp.Process(target=func, args=[2])
    # p_list.append(p3)

    p4 = mp.Process(target=func, args=[2])
    # p_list.append(p4)
    start2 = time.time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()


    # for p in p_list:
    #     p.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end2 = time.time()
    print("## 3.Cost : ", end2-start2, "second")

