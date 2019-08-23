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
max = 0
for i in string:
    if string.count(i) > max:
        max = string.count(i)
print(max)

```

3)
