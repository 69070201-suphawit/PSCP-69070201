"""fatrabbit"""
n = int(input())
overweight_count = 0
heaviest_name = ""
heaviest_weight = -1
for _ in range(n):
    parts = input().split()
    name = parts[0]
    weight = int(parts[1])
    if weight > 15:
        overweight_count += 1
    if weight > heaviest_weight:
        heaviest_weight = weight
        heaviest_name = name
print(overweight_count)
print(heaviest_name)
