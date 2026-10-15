"""main"""
s = input()
upper = 0
lower = 0
digit = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
print(upper, lower, digit)
