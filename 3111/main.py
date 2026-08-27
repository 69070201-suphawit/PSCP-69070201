"""school"""
def school():
    """main"""
    member = input().strip().upper()
    n = int(input())
    total = 0
    for i in range(n):
        i += 0
        price = float(input())
        total = total + price
        if member == 'Y':
            discount = total * 0.05
        elif total >= 500:
            discount = total * 0.03
        else:
            discount = 0
    net = total - discount
    net = int(net * 100 + 0.5000001) / 100
    print(f"{net:.2f}")
school()
