Number=int(input("Enter a number:"))
count=0
while (Number > 0):
        Number = Number //10
        count = count + 1
print("\n number of digits in given number=%d" %count)