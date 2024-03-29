def longestAlternatingSubarray(a, n): 
      
    # Length of longest alternating  
    longest = 1
    cnt = 1
  
    # Iterate in the array 
    i = 1
    while i < n:  
  
        # Check for alternate  
        if (a[i] * a[i - 1] < 0): 
            cnt = cnt + 1
            longest = max(longest, cnt)  
          
        else: 
            cnt = 1
        i = i + 1
      
    return longest  
  
# Driver Code 
a = [ -5, -1, -1, 2, -2, -3 ] 
n = len(a) 
  
print(longestAlternatingSubarray(a, n)) 
  