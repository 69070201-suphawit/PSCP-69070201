"""elonmusk"""
x, k = input().split()
x = int(x)
mid = x // 2

for row in range(x):
    result = ""
    for col in range(x):
        if col in (row, x - 1 - row):
            if k == "#":
                result += "#"
            else:
                offset = abs(row - mid)
                result += chr(ord(k) + offset)
        else:
            result += "-"
    print(result)
