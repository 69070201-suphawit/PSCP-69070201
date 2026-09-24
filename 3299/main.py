"""landokmai"""
L, N = map(int, input().split())
planted = 0
k = 0
while planted < N:
    k += 1
    planted += L * L * (k - 1) + L * (L + 1) // 2
print(k)
