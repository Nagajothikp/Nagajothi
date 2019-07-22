x=int(input("ENter a num:"))
y=int(input("ENter a num:"))
for i in range(1,min(x,y)+1):
    if ((x%i==0) and (y%i==0)):
        x=i
        print(x)
