"""array2Dcheck"""
a = []
for _ in range(5):
    a.append(list(map(int, input().split())))
bad_row = -1
bad_col = -1
for i in range(5):
    if sum(a[i]) % 2 == 1:
        bad_row = i
for j in range(5):
    total = 0
    for i in range(5):
        total += a[i][j]
    if total % 2 == 1:
        bad_col = j
print(bad_row, bad_col)
