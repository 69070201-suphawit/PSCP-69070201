"""sumofnumber"""
target = int(input())
total = 0
while True:
    n = int(input())
    if n == -1:
        break
    total += n
    if total == target:
        break
print(total)
