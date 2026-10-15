"""Pig"""
n = int(input())
w = list(map(int, input().split()))
m = []
for i in range(0, n * 2, 2):
    m.append(max(w[i], w[i + 1]))
if n == 1:
    print(m[0])
else:
    print(" + ".join(map(str, m)), "=", sum(m))
