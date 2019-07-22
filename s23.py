a=list(map(int,input("Enter a num:")))
b=list(map(int,input("Enter a num:")))
c=[]
for i in range(len(b)):
    a.append(b[i])
    c.append(max(a))
    print(*c)

