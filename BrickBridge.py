"""BrickBridge"""
def brickbridge():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())
    use_big = min(goal // 5 , b)
    all_biguse = use_big * 5
    remaining = goal - all_biguse
    if remaining > a :
        print('-1')
    else :
        print(remaining)
brickbridge()
