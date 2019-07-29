def solution (a, b, n): 
  
    i = 0
    while i * a <= n: 
          
        # check if it is satisfying 
        # the equation 
        if (n - (i * a)) % b == 0: 
            print("x = ",i ,", y = ", 
               int((n - (i * a)) / b)) 
            return 0
        i = i + 1
      
    print("No solution") 
  
# driver program to test the above function 
a = 2
b = 3
n = 7
solution(a, b, n) 
  