import threading
import logging
import time
import numpy as np


# def compare(name, x, y):
#     startTime = time.time()
#     logging.info("Thread %s: starting", name)
#     if x > y:
#         print(x)
#     else:
#         print(y)
#     logging.info("Thread %s: finished", name)
#     endTime = time.time()
#     totalRunTime = endTime-startTime
#     logging.info("Thread %s took %ld time",name,totalRunTime)

def easyPosFind(arr,results,element):
    values = np.array(arr)
    searchVal = element
    results.append(np.where(values == searchVal)[0])


arr = [1, 2, 3, 4, 5, 1]
n = len(arr)
threads = []
results = []
for i in range(n):
    x = threading.Thread(target = easyPosFind,args = (arr,results,arr[i]))
    threads.append(x)
    x.start()
for i in range(n):
    x.join()
print(results)
# format = "%(asctime)s: %(message)s"
# logging.basicConfig(filename="logfirstThread.log",level=logging.INFO,format=format,datefmt="%H:%M:%S")
# threads = []
# for i in range(10):
#     logging.info("Main    : create and start thread %d.", i)
#     x = threading.Thread(target=compare, args=(i,(i + 1) ** (i + 1), ((i + 1) ** 2)))
#     threads.append(x)
#     x.start()
# for i in range(10):
#     x.join()
