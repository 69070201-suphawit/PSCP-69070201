"""Bird"""
n = int(input())
h = list(map(int, input().split()))
count = 0
for i in range(n):
    if (not i or h[i] > h[i - 1]) and (i == n - 1 or h[i] > h[i + 1]):
        count += 1
print(count)
