"""บุพเพสันนิวาส"""
a = input().strip()
b = input().strip()
n = max(len(a), len(b))
x = ""
y = ""
for i in range(n):
    x += a[i % len(a)]
    y += b[i % len(b)]
s = ""
for i in range(n):
    if x[i].lower() in "love" or y[i].lower() in "love":
        s += "w"
    else:
        s += "$"
if s.count("w") % 2 == 1:
    best = 0
    cur = 0
    for c in s:
        if c == "w":
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    s += str(best)
elif "ww" not in s:
    s += "#"
print(s)
