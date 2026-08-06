"""Amount"""
def saraamount():
    """main"""
    text_amount = int(input())
    sara = ['A','E','I','O','U']
    count = 0
    for _ in range(text_amount):
        char = input()
        if char in sara :
            count += 1
    print(count)
saraamount()
