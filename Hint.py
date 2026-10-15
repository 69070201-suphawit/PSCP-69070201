"""Hint"""
a = input().split()
b = input().split()
c = input().split()
def check(num, op, d):
    """main"""
    if op == "==":
        return num == d
    if op == ">":
        return num > d
    if op == "<":
        return num < d
    if op == ">=":
        return num >= d
    if op == "<=":
        return num <= d
    return num != d
for n in range(1000):
    u = n % 10
    t = n // 10 % 10
    h = n // 100
    x = check(u, a[0], int(a[1]))
    y = check(t, b[0], int(b[1]))
    z = check(h, c[0], int(c[1]))
    if x and y and z:
        print(f"{n:03d}")
