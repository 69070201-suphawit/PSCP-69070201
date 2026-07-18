"""season"""
def main():
    """main"""
    month = int(input())
    day = int(input())
    if month in [1,2,3] :
        if month == 3 and day >= 21 :
            print("spring")
        else :
            print("winter")
    if month in [4,5,6] :
        if month == 6 and day >= 21 :
            print("summer")
        else :
            print("spring")
    if month in [7,8,9] :
        if month == 9 and day >= 21 :
            print("fall")
        else :
            print("summer")
    if month in [10,11,12] :
        if month == 12 and day >= 21 :
            print("winter")
        else :
            print("fall")
main()
