def findKHCF(x,y,k): 
  
    small = min(x, y) 
   
    count = 1
    for i in range(2,small+1): 
     
        if (x % i==0 and y % i == 0): 
            count=count + 1
        if (count == k): 
            return i 
     
   
    return -1
  
  
x = 4
y = 24
k = 3
print(findKHCF(x, y, k))