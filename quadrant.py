"""quadrant"""
def main():
    """main"""
    num_x = int(input())
    num_y = int(input())
    if not num_x and not num_y :
        print("O")
    elif not num_x :
        print("Y")
    elif not num_y :
        print("X")
    elif num_x > 0 and num_y > 0 :
        print("Q1")
    elif num_x < 0 < num_y  :
        print("Q2")
    elif num_x < 0 and num_y < 0 :
        print("Q3")
    elif num_x > 0 > num_y :
        print("Q4")
main()
