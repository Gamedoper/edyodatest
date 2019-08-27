#import pdb 
import logging
import sys


# list of numbers and key exists == true
# list of num and keys does not exits == fasle
# list in empty return ==>false
# if key is is none =>false


logging.basicConfig(level= logging.ERROR,filename= "/home/ubuntu/python-dev-program/test_log",format="%(asctime)s-%(levelname)s-%(message)s")
def linear_search(n,x):
    logging.debug("sUCC ENTERED HE FUNCTION")
    element = []

    for i in range(1,n):
        element.append(i)
        flag = 0
    
    
    for i in element:
        if(i==x):
            print("number is found" + str(i))
            flag =1

        if(flag==0):
            print("number not found")

print(sys.argv)

#pdb.set_trace()
linear_search(1000,50)
logging.error("sUCC COMPLETED HE FUNCTION")



