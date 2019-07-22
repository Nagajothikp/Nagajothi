a1=int(input())
b=list(map(int,input().split()))[:a1]
for i in range(a1):
    if(b.count(b[i])==1):
        print(b[i])