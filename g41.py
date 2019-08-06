
  
MAX_SIZE=10
def sortByRow(mat, n, ascending): 
  
    for i in range(n): 
        if (ascending):     
            mat[i].sort() 
        else: 
            mat[i].sort(reverse=True) 
def transpose(mat, n): 
  
    for i in range(n): 
        for j in range(i + 1, n):  
            temp = mat[i][j] 
            mat[i][j] = mat[j][i] 
            mat[j][i] = temp 
  
def sortMatRowAndColWise(mat, n): 
    sortByRow(mat, n, True) 
    transpose(mat, n) 
    sortByRow(mat, n, False) 
    transpose(mat, n) 
def printMat(mat, n): 
  
    for i in range(n): 
        for j in range(n): 
            print(mat[i][j] , " ", end="") 
        print() 
n = 3
       
mat = [[3, 2, 1], 
    [9, 8, 7],  
    [6, 5, 4]] 
   
print("Original Matrix:") 
printMat(mat, n) 
   
sortMatRowAndColWise(mat, n) 
   
print("Matrix After Sorting:") 
printMat(mat, n) 
  