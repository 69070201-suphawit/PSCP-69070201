"""aeiou"""
def aeiou():
    """main"""
    text = input().lower()
    sara = 'aeiou'
    for i in sara:
        count = text.count(i)
        if count > 0:
            print(f'{i} : {count}')
aeiou()
