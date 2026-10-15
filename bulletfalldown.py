"""ตำบลกระสุนตก"""
import math
n = int(input())
shots = []
for _ in range(n):
    x, y, d = map(int, input().split())
    shots.append((x, y, d))
x0, y0, d0 = shots[0]
answers = []
for tx in range(max(0, x0 - d0), min(1000, x0 + d0) + 1):
    rem = d0 * d0 - (tx - x0) ** 2
    r = math.isqrt(rem)
    if r * r != rem:
        continue
    for ty in sorted({y0 - r, y0 + r}):
        if ty < 0 or ty > 1000:
            continue
        ok = True
        for x, y, d in shots:
            if (tx - x) ** 2 + (ty - y) ** 2 != d * d:
                ok = False
        if ok:
            answers.append((tx, ty))
print(answers[0][0], answers[0][1])
