def check(string) : 
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        print("Yes") 
    else : 
        print("No") 
   
if __name__ == "__main__" : 
  
    string = "1010100001122"
   
    check(string) 


