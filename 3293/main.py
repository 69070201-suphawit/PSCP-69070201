"""BigFrame"""
lines = [input() for _ in range(5)]
w = max(len(s) for s in lines)
border = '*' * (w+4)
print(border)
for s in lines:
    print('* ' + s.ljust(w) + ' *')
print(border)
