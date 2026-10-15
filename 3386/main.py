"""Duplicate I"""
m = int(input())
n = int(input())
a = []
i = 0
while i < m:
    a = a + [input().strip()]
    i = i + 1
b = []
i = 0
while i < n:
    b = b + [input().strip()]
    i = i + 1
both = []
i = 0
while i < m:
    if a[i] in b and a[i] not in both:
        both = both + [a[i]]
    i = i + 1
k = len(both)
i = 1
while i < k:
    cur = both[i]
    j = i - 1
    while j >= 0 and int(both[j]) < int(cur):
        both[j + 1] = both[j]
        j = j - 1
    both[j + 1] = cur
    i = i + 1
if not k:
    print("Nope")
else:
    i = 0
    while i < k:
        print(both[i])
        i = i + 1
