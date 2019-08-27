
import threading

import time




def read1():
    print("reading a file")
    fp = open("test_log",'r')
    content = fp.read()
    print(content)
    fp.close()    



def write1():
    print("im trying to write smething")
    fp1 = open("test_log","a+")
    fp1.write("we are anonymous")
    fp1.close()


    

t1= threading.Thread(target = read1,name="read1")
t2= threading.Thread(target = read1,name="read2")
t3= threading.Thread(target = write1,name="write1")


t1.start()
t2.start()
t3.start()


