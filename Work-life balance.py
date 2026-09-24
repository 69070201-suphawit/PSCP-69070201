"""สมดุลย์ชีวิต"""
n = int(input())
heavy = 0
light = 0
for _ in range(n):
    h = int(input())
    if h > 18:
        heavy += 1
    else:
        light += 1
need = heavy - 1 - light
if need < 0:
    need = 0
print(n + need)
