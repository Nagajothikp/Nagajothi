

Number = int(input(" Enter any Number: "))
product=1

while(Number != 0):
    product = product*(Number %10)
    Number = Number //10

print("\n product of the digits of Given Number =",product)