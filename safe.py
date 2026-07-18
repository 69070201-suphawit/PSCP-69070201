"""safe"""
def main():
    """main"""
    word = input()
    Number = int(input())
    if word == "H" and Number == 4567:
        print("safe unlocked")
    elif word == "H" and Number != 4567:
        print("safe locked - change digit")
    elif word != "H" and Number == 4567:
        print("safe locked - change char")
    elif word != "H" and Number != 4567:
        print("safe locked")
main()
