"""pasarabbit"""
s = input().strip().upper()
n = len(s)
if all(c in "IT" for c in s):
    print("unknown", n)
else:
    state = 0
    best = cur = 0
    bad = -1
    for i, c in enumerate(s):
        if state == 1:
            if c == 'A':
                state = 3
                cur = 1
                best = max(best, cur)
                continue
            bad = i
            break
        if state == 2:
            if c in "IT":
                state = 4
                continue
            bad = i
            break
        if state == 3 and c == 'A':
            cur += 1
            best = max(best, cur)
            continue
        if state == 4 and c in "IT":
            continue
        cur = 0
        if c == 'R':
            state = 1
        elif c == 'B':
            state = 2
        elif c == 'A':
            bad = i
            break
        else:
            state = 0
    if bad == -1 and state in (1, 2):
        bad = n
    if bad == -1:
        print("yes", best)
    else:
        print("no", bad)
