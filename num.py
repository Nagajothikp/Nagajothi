print ("Enter the number:")
try:
   x=int(input())
   if x>0:
      print("The given number is positive")
   elif x<0:
      print("The given number is negative") 
   else:
      print("The given number is zero")
except:
    print("Invalid input")