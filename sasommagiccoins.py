"""magiccoins"""
n = int(input())
fire = 0
water = 0
earth = 0
for _ in range(n):
    c = list(map(int, input().split()))
    fire += max(c[0], c[3])
    water += max(c[1], c[4])
    earth += max(c[2], c[5])
print("Total:", fire + water + earth)
print("Fire:", fire)
print("Water:", water)
print("Earth:", earth)
if fire > water + earth:
    print("Bonus: YES")
else:
    print("Bonus: NO")
