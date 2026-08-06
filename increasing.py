"""increasing"""
def increasing():
    """main"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 < num2 < num3 :
        print("increasing")
    elif num1 > num2 > num3 :
        print("decreasing")
    else :
        print("neither")
increasing()
