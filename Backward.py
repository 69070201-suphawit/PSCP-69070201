"""BackWard"""
data = []
line = input()
while line != "NULL":
    data.append(line)
    line = input()
for i in range(len(data) - 1, -1, -1):
    print(data[i])
