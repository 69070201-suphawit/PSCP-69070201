"""colour"""
def main():

    """main"""
    colour1 = input()
    colour2 = input()
    if (colour1 == "Red" and colour2 == "Yellow") or (colour1 == "Yellow" and colour2 == "Red"):
        print("Orange")
    elif (colour1 == "Red" and colour2 == "Blue") or (colour1 == "Blue" and colour2 == "Red"):
        print("Violet")
    elif (colour1 == "Yellow" and colour2 == "Blue") or (colour1 == "Blue" and colour2 == "Yellow"):
        print("Green")
    elif (colour1 == "Red" and colour2 == "Red"):
        print("Red")
    elif (colour1 == "Yellow" and colour2 == "Yellow"):
        print("Yellow")
    elif (colour1 == "Blue" and colour2 == "Blue"):
        print("Blue")
    else:
        print("Error")
main()
