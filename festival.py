"""festival"""
def main():
    """main"""
    text = input()
    pos_x = 0
    pos_y = 0
    for letter in text:
        if letter == "N":
            pos_y = pos_y + 1
        elif letter == "S":
            pos_y = pos_y - 1
        elif letter == "E":
            pos_x = pos_x + 1
        elif letter == "W":
            pos_x = pos_x - 1
    if pos_x < 0:
        diff_x = -pos_x
    else:
        diff_x = pos_x
    if pos_y < 0:
        diff_y = -pos_y
    else:
        diff_y = pos_y
    total = diff_x + diff_y
    print(pos_x, pos_y, total)
main()
