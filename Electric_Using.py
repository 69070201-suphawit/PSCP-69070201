"""Electric_Using"""
n = int(input())
elect = [(10,5),(40,7),(50,10),(100,12)]
lectric_use = 0
remain = n
for size,rate in elect:
    use = min(remain, size)
    lectric_use += use * rate
    remain -= use
lectric_use += remain * 15
total = lectric_use * 107 + 50 * n
padset = (total + 5) // 10
print(f'{padset // 10}.{padset % 10}')
