"""min"""
def find_min():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    minimum = a
    if b < minimum :
        minimum = b
    if c < minimum :
        minimum = c
    print(minimum)
find_min()
