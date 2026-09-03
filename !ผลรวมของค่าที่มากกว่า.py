"""ผลรวมของค่าที่มากกว่า"""
n = int(input())
value = []
for _ in range(n):
    a = int(input())
    b = int(input())
    if a > b:
        value.append(a)
    else:
        value.append(b)
if n == 1:
    print(value[0])
else:
    equation = str(value[0])
    for i in range(1, n):
        equation = equation + " + " + str(value[i])
    print(f"{equation} = {sum(value)}")
