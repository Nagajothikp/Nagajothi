def round( n ): 
    a = (n // 10) * 10
    b = a + 10
      
    return (b if n - a > b - n else a)  
n = int(input("Enter a value"))
print(round(n)) 