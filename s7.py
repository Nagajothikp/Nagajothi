s="Hi jo"
g=s[0::2]
n=s[1::2]
print(g,n,end="")
temp=g
g=n
n=temp
print("\n",g,n)