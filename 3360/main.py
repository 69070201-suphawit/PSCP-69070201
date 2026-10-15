"""หั่นขนมปัง"""
line = input().split()
w = int(line[0])
h = int(line[1])
m = int(line[2])
n = int(line[3])
xs = input().split()
a1 = 0
a2 = 0
prev = 0
i = 0
while i <= m:
    if i < m:
        cur = int(xs[i])
    else:
        cur = w
    g = cur - prev
    if g > a1:
        a2 = a1
        a1 = g
    elif g > a2:
        a2 = g
    prev = cur
    i = i + 1
ys = input().split()
b1 = 0
b2 = 0
prev = 0
i = 0
while i <= n:
    if i < n:
        cur = int(ys[i])
    else:
        cur = h
    g = cur - prev
    if g > b1:
        b2 = b1
        b1 = g
    elif g > b2:
        b2 = g
    prev = cur
    i = i + 1
first = a1 * b1
c1 = a1 * b2
c2 = a2 * b1
if c1 > c2:
    second = c1
else:
    second = c2
print(first, second)
