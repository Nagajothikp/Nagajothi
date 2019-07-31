def printRepeating(arr, size): 
  
    print("Repeating elements are ", 
                         end = '') 
    for i in range (0, size): 
        for j in range (i + 1, size): 
            if arr[i] == arr[j]: 
                print(arr[i], end = ' ') 
      
arr = [1 ,2 ,3 ,2 ,1] 
arr_size = len(arr) 
printRepeating(arr, arr_size) 
  