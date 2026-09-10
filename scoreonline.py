"""scoreonline"""
def scoreonline():
    """main"""
    base = int(input())
    bonus = int(input())
    days = int(input())
    if days > 3 :
        total = ( base + bonus ) * 1.5
    else :
        total = base + bonus
    if total >= 1500 :
        rank = 5
    elif total >= 1000 :
        rank = 4
    elif total >= 500 :
        rank = 3
    elif total >= 200 :
        rank = 2
    else :
        rank = 1
    if rank == 5 and days >= 7 :
        code = '99'
    elif rank == 4 and bonus > 300 :
        code = '88'
    else :
        code = '0'
    print(int(total))
    print(rank)
    print(code)
scoreonline()
