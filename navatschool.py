"""main"""
def password():
    """main"""
    text = input()

    first = text[0].upper()
    last = text[-1].upper()
    n = len(text)

    data = []

    for i in range(10):
        if (i + 1) % 2 == 1:
            x = ord(first) + i
        else:
            x = ord(last) - i

        x = x % n

        if x > 9:
            x = x % 10

        data.append(x)

    print(*data[2:8])

password()
