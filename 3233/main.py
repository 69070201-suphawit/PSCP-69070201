"""huay"""
def huay():
    """main"""
    win_letter, win_number = input().split()
    my_letter, my_number = input().split()
    money = 0
    if my_letter == win_letter and my_number == win_number:
        money += 1000000
    elif my_letter != win_letter and my_number == win_number:
        money += 100000
    elif my_letter == win_letter and my_number[-3:] == win_number[-3:]:
        money += 2000
    elif my_letter == win_letter and my_number[-2:] == win_number[-2:]:
        money += 1000
    elif my_letter != win_letter and my_number[-3:] == win_number[-3:]:
        money = 200
    elif my_letter != win_letter and my_number[-2:] == win_number[-2:]:
        money = 100
    elif my_letter == win_letter and my_number != win_number:
        money = 20
    print(money)
huay()
