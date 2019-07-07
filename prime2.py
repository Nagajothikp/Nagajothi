x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
for i in range(x,y+1):
    if(i>1):
        for n in range(2,i):
            if(i%n)==0:
                break
            else:
                print(i)