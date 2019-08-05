user_number = input ("Enter your number")
try:
   val = int(user_number)
   if(val > 0):
       print("yes ")
   else:
       print("no")
except ValueError:
   print("invalid")