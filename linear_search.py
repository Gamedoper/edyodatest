#import pdb 


# list of numbers and key exists == true
# list of num and keys does not exits == fasle
# list in empty return ==>false
# if key is is none =>false



def linear_search(n,x):
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

#pdb.set_trace()
linear_search(1000,50)



