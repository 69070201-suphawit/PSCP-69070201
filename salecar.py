"""Sale Car"""
n = int(input())
cars = []
for i in range(n):
    _, v = input().split()
    cars.append(int(v))
best = 0
count = 0
for i in range(n - 1, -1, -1):
    if cars[i] > best:
        best = cars[i]
    else:
        count += 1
print(count)
