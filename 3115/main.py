"""aecade"""
def arcade():
    """main"""
    data = input().split()
    num = int(data[0])
    check = int(data[1])

    count = [0] * 1441

    for i in range(num):
        room = input().split()
        start = int(room[0])
        stop = int(room[1])
        for t in range(start, stop):
            count[t] += 1

    times = input().split()

    for i in range(check):
        k = int(times[i])
        print(count[k], end=' ')

arcade()
