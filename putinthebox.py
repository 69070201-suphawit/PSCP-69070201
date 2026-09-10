"""putinthebox"""
W, L, M, N = map(int, input().split())
best = W * L
for a in range(M, N + 1):
    waste = (W % a) * (L % a)
    if waste < best:
        best = waste
print(best)
