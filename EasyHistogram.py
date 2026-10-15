"""Easy Histogram"""
s = input()
for i in range(26):
    low = chr(ord("a") + i)
    up = low.upper()
    if s.count(low) > 0:
        print(low, "=", s.count(low))
    if s.count(up) > 0:
        print(up, "=", s.count(up))
