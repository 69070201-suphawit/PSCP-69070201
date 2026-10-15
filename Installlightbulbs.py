"""ติดตั้งหลอดไฟ"""
n = int(input())
heights = []
for _ in range(n):
    heights.append(int(input()))
heights.sort()
total = 0
prefix = 0
for h in heights:
    prefix += h
    total += prefix * 2
print(total)
