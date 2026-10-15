"""Shorten"""
x = int(input())
out = ""
if x != -1:
    start = x
    prev = x
    x = int(input())
    while x != -1:
        if x != prev + 1:
            if start == prev:
                out = out + str(start) + ", "
            else:
                out = out + str(start) + "-" + str(prev) + ", "
            start = x
        prev = x
        x = int(input())
    if start == prev:
        out = out + str(start)
    else:
        out = out + str(start) + "-" + str(prev)
print(out)
