def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
            print(string[::-1])
              
    print(string) 
  
string ="hi apple bae"
rem_vowel(string) 