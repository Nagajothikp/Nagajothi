x=int(input("how much numbers:"))
total = 0
for n in range(x):
    numbers=float(input("enter numbers:"))
    total += numbers
avg = total/x
print("average of ",x,"numbers is:",avg)
