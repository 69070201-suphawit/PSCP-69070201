"""มาเป็นทีม"""
n, m = map(int, input().split())

if n < 1 or n > 10 or m < 1 or m > 20:
    print("Data Incorrect")
else:
    vals = []
    while len(vals) < n * m:
        try:
            vals += input().split()
        except EOFError:
            break

    scores = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(vals[i * m + j]))
        scores.append(row)

    bad = False
    for i in range(n):
        for j in range(m):
            if scores[i][j] < 0 or scores[i][j] > 100:
                bad = True

    if bad:
        print("Data Incorrect")
    else:
        total = 0
        for i in range(n):
            s = 0
            mx = scores[i][0]
            for j in range(m):
                s += scores[i][j]
                if scores[i][j] > mx:
                    mx = scores[i][j]
            total += s
            print(f"Team {i + 1}: Average = {s / m:.2f}, Max = {mx}")
        print(f"Total Score of All Teams = {total}")
