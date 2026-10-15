"""Giraffe"""
n = int(input())
h = []
i = 0
while i < n:
    h = h + [int(input())]
    i = i + 1
count = 0
i = 0
while i < n:
    ok = True
    if i > 0 and h[i] < h[i - 1]:
        ok = False
    if i < n - 1 and h[i] < h[i + 1]:
        ok = False
    if ok:
        count = count + 1
    i = i + 1
print(count)
