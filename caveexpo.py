"""caveExpo"""
n = int(input())
cave = list(map(int, input().split()))
s = input().strip()
pos = cave.index(1)
chest = cave.index(2)
for c in s:
    if c == "R" and pos < n - 1:
        pos += 1
    elif c == "L" and pos > 0:
        pos -= 1
    if pos == chest:
        break
result = [0] * n
result[chest] = 2
result[pos] = 1
print(*result)
