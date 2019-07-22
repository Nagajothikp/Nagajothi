import math
a=int(input("Enter a num:"))
b=int(input("Enter a num:"))
count=0
for i in range(a,b+1):
    s=math.sqrt(i)
    if math.sqrt(i)==int(s):
        count+=1
        print(count)

