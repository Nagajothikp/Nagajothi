num=int(input("Enter the number:"))
temp=num
rev=0
while temp!=0:
    rev=(rev*10)+(temp % 10)
    temp=temp//10
if num==rev:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
