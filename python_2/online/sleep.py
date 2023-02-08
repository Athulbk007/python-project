from time import sleep
def task():
    sleep()
    print('this is from another thread')

# task()
from threading import  Thread
thread = Thread(target=task)
thread.start()


def task(sleep,time,message):
    sleep(sleep_time)
    print(message)

thread = Thread(target=task, args=(1.5,'new message from another thread'))
thread.start()
print('waiting for the thread...')
thread.join()


import  time
import threading

def cal_sqre(num):
    print("calculate the square root of the given number")
    for n in num:
        time.sleep(0.3)
        print('square is : ',n * n)
    arr=[4,5,6,7,2]
t1=time.time()
th1 = threading.Thread(target=cal_sqre,args=(arr,))
th2 = threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print('total ')