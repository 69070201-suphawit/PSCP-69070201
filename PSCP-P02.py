"""main"""
s = input()
product = 1
has_nonzero = False
for ch in s:
    d = int(ch)
    if d:
        product *= d
        has_nonzero = True
if has_nonzero:
    print(product)
else:
    print(0)
