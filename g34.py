def editDistance(str1, str2, m , n): 
    if m==0: 
         return n 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n==0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
  
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                   editDistance(str1, str2, m-1, n-1)    # Replace 
                   ) 
  
# Driver program to test the above function 
str1 = "sunday"
str2 = "saturday"
print (editDistance(str1, str2, len(str1), len(str2)) )
  