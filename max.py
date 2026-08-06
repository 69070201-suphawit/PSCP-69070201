"""max"""
def find_max():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    maximum = a
    if b > maximum :
        maximum = b
    if c > maximum :
        maximum = c
    print(maximum)
find_max()
