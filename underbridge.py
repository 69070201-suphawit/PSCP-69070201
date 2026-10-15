"""ลอดสะพาน"""
l, n = map(int, input().split())
d = [0] * (l + 2)
for _ in range(n):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] -= 1
best = 0
cur = 0
for i in range(l + 1):
    cur += d[i]
    best = max(best, cur)
print(best)
