"""ticket"""
def ticket():
    """main"""
    age = int(input())
    status = input()
    if age < 18 or status in 's' 'S' :
        print('20')
    elif age > 17 or status in 'a' 'A' :
        print('50')
ticket()
