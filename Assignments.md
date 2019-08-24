# Welcome to My Homework!


**Assignment 1st** 

1) to find no of denominations in currency
```
    def no_notes(a):
            notes = [2000,500, 200, 100, 50, 20, 10]
            count = 0
            for i in range(6):
                q = notes[i]
                count += int(a / q)
                a = int(a % q)
            if a > 0:
                count = -1
            return count
        print(no_notes(1000))

```
2)  fetch most occurred string

```
string = "aaabbbcccccc"


#string="aaaaaaabbbbcccdddd"

set1 = set(s)

count = 0
char =' '

for i in set1:
    if count < string.count(i):
        count = string.count(i)
        char = i
print(char)

```

6) 
```
#problem 6

dict =  {'2':('a','b','c'),'3':('d','e','f'),'4':('g','h','i'),'5':('j','k','l'),
                '6':('m','n','o'),'7':('p','q','r','s'),'8':('t','u','v'),'9':('w','x','y','z')}

number = "9999335533"
temp = number[0]
count= 0
list =[]
for i in range(len(number)):
    if temp == number[i]:
        count+=1
    else:
        list.append(dict[temp][count-1])
        temp = number[i]
        count=1
    if i == (len(number)-1):
         list.append(dict[temp][count-1])
        
        
for i in list:
    print(i,end="")



```

3)
