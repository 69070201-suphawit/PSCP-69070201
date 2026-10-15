"""ส่องไฟ"""
n = int(input())
lit = [False] * 360
for _ in range(n):
    a, b = map(int, input().split())
    k = a
    while k != b:
        lit[k] = True
        k = (k + 1) % 360
if all(lit):
    print(360)
else:
    start = lit.index(False)
    best = 0
    run = 0
    for i in range(1, 361):
        if lit[(start + i) % 360]:
            run += 1
            if run > best:
                best = run
        else:
            run = 0
    print(best)
