A=int(input("Enter a num:"))
B=[]
for i in range (2,A+1):
    if (A%i)==0:
        B.append(i)
        A=A//i
c=sorted(B)
print(*c)