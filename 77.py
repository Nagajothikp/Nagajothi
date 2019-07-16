n=int(input("Enter a num:"))
Factors=[]
for i in range(1,n+1):
    if n%i==0:
        Factors.append(i)
        print("Factors of {}={}".format(n,Factors))
    