
from collections import Counter 
  
def anagram(input1, input2): 
    return Counter(input1) == Counter(input2) 
  
if __name__ == "__main__": 
    input1 = 'abcd'
    input2 = 'dcab'
    print (anagram(input1, input2))