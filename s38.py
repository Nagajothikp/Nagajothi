x=int(input("Enter a num:"))
for i in range(2,x+1,2):
    if x%i==0:
        print(i,end=" ")
