def maxTripletSum(arr, n) : 
  
    # Initialize the answer 
    ans = 0
   
    for i in range(1, (n - 1)) : 
        max1 = 0
        max2 = 0
   
        # find maximum value(less than arr[i]) 
        # from i + 1 to n-1 
        for j in range(0, i) : 
            if (arr[j] < arr[i]) : 
                max1 = max(max1, arr[j]) 
   
        # find maximum value(greater than arr[i]) 
        # from i + 1 to n-1 
        for j in range((i + 1), n) : 
            if (arr[j] > arr[i]) : 
                max2 = max(max2, arr[j]) 
   
        # store maximum answer 
        ans = max(ans, max1 + arr[i] + max2) 
   
    return ans 
  
arr = [ 1,3,2,4,5,4] 
n = len(arr) 
print(maxTripletSum(arr, n)) 
  