"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
def get_level(d):
    """main"""
    if d <= 0:
        return 100
    if d == 1:
        return 60
    if d == 2:
        return 20
    return 0
rows, cols = map(int, input().split())
rr, rc = map(int, input().split())
n = int(input())
risk = []
for i in range(rows):
    risk.append([0] * cols)
for _ in range(n):
    r, c = map(int, input().split())
    for i in range(rows):
        for j in range(cols):
            lv = get_level(max(abs(i - r), abs(j - c)))
            risk[i][j] = max(risk[i][j], lv)
safe = 0
for i in range(rows):
    for j in range(cols):
        if risk[i][j] <= 0:
            safe += 1
print(safe)
print(str(risk[rr][rc]) + "%")
