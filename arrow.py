"""arrow"""
side = input()
n = int(input())
pairs = []
for i in range(n):
    indent = 2 * i
    star = n - i
    pairs.append((indent, star))
for i in range(n - 2, -1, -1):
    indent = 2 * i
    star = n - i
    pairs.append((indent, star))
width = 2 * n - 1
for direction, direct in enumerate(side):
    for indent, star in pairs:
        if direct == 'R':
            print(" " * indent + '*' * star)
        else:
            print(" " * (width - indent - star) + '*' * star)
    if direction != len(side) - 1:
        print()
  