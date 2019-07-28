def isSubsetAndZero(array, length, N): 
  
    arrAnd = array[0] 
  
    for i in range(1, length) : 
        arrAnd = arrAnd & array[i] 
  
    if ((arrAnd & N) == 0): 
        print("YES") 
    else: 
        print("NO") 
  
if __name__ == "__main__": 
    array = [ 1, 2, 4 ] 
    length = len(array) 
  
    N = 3
  
    isSubsetAndZero(array, length, N) 