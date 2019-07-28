def pairORSum(arr, n) : 
    ans = 0     # Initialize result 
  
    # Consider all pairs (arr[i], arr[j)  
    # such that i < j 
    for i in range(0, n) : 
          
        for j in range(i + 1, n) : 
              
            ans = ans + (arr[i] ^ arr[j]) 
              
    return ans 
      
  

arr = [ 5, 9, 7, 6 ] 
n = len(arr) 
  
print(pairORSum(arr, n)) 
  
  