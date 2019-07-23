import string
a=input("ENter  a  num:")
a.split()
a=a.replace('',' ')
b=[i for i in a if a.count(i)==1]
c=(' '.join(b))
print(c.lower())

