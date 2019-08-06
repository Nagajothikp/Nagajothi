def getSmallestAndLargest(s, k):
    currStr = s[:k]
    lexMin = currStr
    lexMax = currStr
    for i in range(k, len(s)):
        currStr = currStr[1 : k] + s[i]
    if (lexMax < currStr): 
        lexMax = currStr
        print(lexMin)
        print(lexMax)
    if __name__ == __main__:
        str1 = “GeeksForGeeks”
        k = 3
        sgetSmallestAndLargest(str1, k)

