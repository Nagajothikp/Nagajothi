def findPrevious(number, n): 
    number = list(number) 
  
    i, j = -1, -1
  
    for i in range(n - 1, 0, -1): 
        if number[i] < number[i - 1]: 
            break
    if i == 0: 
        print("Previous number is not possible") 
        return
      
    x, greatest = number[i - 1], i 
    for j in range(i, n): 
        if (number[j] < x and
            number[j] > number[greatest]): 
            greatest = j 
      
    # III) Swap the above found smallest digit 
    # with number[i-1] 
    (number[greatest],  
     number[i - 1]) = (number[i - 1],  
                       number[greatest]) 
  
    l = number[i:] 
    del number[i:] 
  
    # IV) Sort the digits after(i-1) 
    # in descending order 
    l.sort(reverse = True) 
  
    number += l 
  
    # Again join the list to make it string 
    number = '' . join(number) 
    print("Greatest smaller number with", 
          "same set of digits is", number) 
  
    return
  
# Driver Code 
if __name__ == "__main__": 
    digits = "262345"
    n = len(digits) 
  
    findPrevious(digits, n) 
  