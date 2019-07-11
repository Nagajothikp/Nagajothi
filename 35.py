fname = input("Enter file name: ")
num_line= 0
with open(fname, 'r') as f:
    for line in f:
        num_line += 1
print("Number of lines:")
print(num_line)