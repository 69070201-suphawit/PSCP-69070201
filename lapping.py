"""แซงรอบ"""
n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(input()))
w = min(s)
count = 0
for x in s:
    if k * (x - w) < x:
        count += 1
print(count)
