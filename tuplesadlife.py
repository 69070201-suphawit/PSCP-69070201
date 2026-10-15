"""tuplesadlife"""
t = tuple(input().split())
v = input().strip()
c = t.count(v)
if c > 0:
    i = t.index(v)
    for _ in range(c):
        print(*[i] * c)
