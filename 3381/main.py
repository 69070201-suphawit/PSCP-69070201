"""Point Sorting"""
t = int(input())
while t > 0:
    n = int(input())
    xs = []
    ys = []
    i = 0
    while i < n:
        p = input().split()
        xs = xs + [int(p[0])]
        ys = ys + [int(p[1])]
        i = i + 1
    i = 1
    while i < n:
        cx = xs[i]
        cy = ys[i]
        j = i - 1
        while j >= 0 and (xs[j] + ys[j] > cx + cy or (xs[j] + ys[j] == cx + cy and ys[j] < cy)):
            xs[j + 1] = xs[j]
            ys[j + 1] = ys[j]
            j = j - 1
        xs[j + 1] = cx
        ys[j + 1] = cy
        i = i + 1
    i = 0
    while i < n:
        print(str(xs[i]) + " " + str(ys[i]))
        i = i + 1
    t = t - 1
