"""frogjump"""
def frogjump():
    """main"""
    x , y = map(int, input().split())
    distance = 0
    jump = 0
    while distance < y:
        if x <= 0 :
            jump = -1
            break
        distance += x
        jump += 1
        x -= 2
    print(jump)
frogjump()
