def newString(s, k): 
    X = "" 
  
    while (len(s) > 0): 
        temp = s[0] 
        i = 1
        while(i < k and i < len(s)): 
            if (s[i] < temp): 
                temp = s[i] 
  
            i += 1
          
        
        X = X + temp 
        for i in range(k): 
            if (s[i] == temp): 
                s = s[0:i] + s[i + 1:] 
                break
          
    return X 
  
# Driver Code 
if __name__ == '__main__': 
    s = "gaurang"
    k = 3
    print(newString(s, k)) 
  