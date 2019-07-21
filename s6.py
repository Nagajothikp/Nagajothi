string,string2 = input().split()
if len(string) != len(string2):
    print("No")
else:
    for i in range(0,len(string)):
        if string.count(string[i])==string2.count(string2[i]):
            print("yes")
            break
        else:
            print("no")
            break