"""sasomtam"""
def sasompoint():
    """main"""
    command = int(input())
    count = 0
    for i in range(command) :
        i += 0
        point = input()
        if point in '+' :
            count += 10
        elif point in '-' :
            count -= 5
        else :
            count += 0
    print(count)
sasompoint()
