"""passOrNot"""
def passornot():
    """main"""
    midterm = int(input())
    final = int(input())
    total_score = midterm + final
    print(total_score)
    if total_score >= 50 :
        print('pass')
    else :
        print('fail')
passornot()
