"""Stack of bowls"""
n = int(input())
count = {}
for _ in range(n):
    x = int(input())
    count[x] = count.get(x, 0) + 1
print(max(count.values()))
