def isDigitPresent(x, d): 
  
    while (x > 0): 
      
        if (x % 10 == d): 
            break
  
        x = x / 10
      
  
    return (x > 0) 
  
  
def printNumbers(n, d): 
  
    for i in range(0, n+1): 
  
        if (i == d or isDigitPresent(i, d)): 
            print(i,end=" ") 
  

n = 47
d = 7
print("The number of values are") 
printNumbers(n, d) 