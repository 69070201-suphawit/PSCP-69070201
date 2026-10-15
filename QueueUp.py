"""Queue up"""
_, _ = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))
for pos in a:
    i = pos - 1
    tallest = 0
    if i > 0:
        tallest = max(h[:i])
    need = tallest - h[i] + 1
    if need < 0:
        need = 0
    print(need)
