import threading
import time

#read write andoperaions  io operations 

#complexity 


def add(num1,num2):
    print("inside add function")
    time.sleep(5)
    print(num1 + num2)
    




def mul(num1,num2):
    print("inside add function")
    print(num1 * num2)



t1 = threading.Thread(target = add,args=(10,20), name="add_tread")
t2 = threading.Thread(target = mul,args=(5,6),name = "mul_thread")



t1.start()
t1.join()
t2.start()






