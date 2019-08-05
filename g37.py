import math 
  
def number_of_teams(M):  
      
    N1, N2, sqr = 0,0,0
  
  
    N1 = (1 + sqr) / 2
  
    N2 = (1 - sqr) / 2
  
    if (N1 > 0): 
        return int(N1)  
    return int(N2)  
  
def main():  
    M = 45
    print(number_of_teams(M)) 
if __name__ == '__main__': 
    main() 
      
  
def number_of_teams(M):  
      
    N1, N2, sqr = 0,0,0
  
    sqr = math.sqrt(1 + (8 * M))  
  
    N1 = (1 + sqr) / 2
  
    N2 = (1 - sqr) / 2
  
    if (N1 > 0): 
        return int(N1)  
    return int(N2)  
  
def main():  
    M = 45
    print(number_of_teams(M)) 
if __name__ == '__main__': 
    main() 
      