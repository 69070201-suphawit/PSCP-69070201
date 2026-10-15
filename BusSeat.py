"""Busseat"""
seats = int(input())
rows = int(input())
me = int(input())
for r in range(seats, 0, -1):
    line = []
    for c in range(rows):
        num = c * seats + r
        if num == me:
            line.append("XX")
        else:
            line.append(f"{num:02d}")
    print(" ".join(line))
    if r % 2 == 1 and r != 1:
        print()
