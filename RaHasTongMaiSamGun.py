"""รหัสต้องไม่ซ้ำกัน"""
n = int(input())
codes = list(map(int, input().split(" ", n - 1)))
rare = []
for c in codes:
    if codes.count(c) == 1:
        rare.append(c)
rare.sort()
print(" ".join(map(str, rare)))
