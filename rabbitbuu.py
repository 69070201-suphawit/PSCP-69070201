"""rabbit_buu"""
s = input()
low = s.lower()
if 'buu' in low:
    best = 0
    for i, ch in enumerate(low):
        if ch == 'b':
            count = 0
            j = i + 1
            while j < len(low) and low[j] == 'u':
                count += 1
                j += 1
            if count > best:
                best = count
    print('Yes', best)
elif 'b' in low:
    i = low.index('b')
    print(s[:i + 1] + 'U' * (len(s) - i - 1))
else:
    print(('BUU' * len(s))[:len(s)])
