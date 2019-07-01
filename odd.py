print ("Enter a number")
try:
    x =int(input()) 
    if x%2 == 0:
        print("The given number is even")
    else:
        print("The given number is odd")
except:
    print("Invalid Input")
