def printleaders(arr,size):
    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i]<=arr[j]:
                break
        if j==size-1:
            print(arr[i],)
arr=[16,17,4,3,5,2]
printleaders(arr,len(arr))