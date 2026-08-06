"""thunderXpress"""
def thunderxpress():
    """main"""
    text = input()
    text_split = text.split(" ")
    first = text_split[0]
    last = text_split[1]
    weight = float(input())
    if first in 'BKK' and last in 'CNX' :
        print(f'{10 + (weight * 30):.2f}')
    elif first in 'CNX' and last in 'UBP' :
        print(f'{15 + (weight * 40):.2f}')
    elif first in 'UBP' and last in 'BKK' :
        print(f'{20 + (weight * 40):.2f}')
    elif first in 'BKK' and last in 'PKT' :
        print(f'{25 + (weight * 50):.2f}')
    elif first in 'PKT' and last in 'CNX' :
        print(f'{30 + (weight * 60):.2f}')
    elif first in 'UBP' and last in 'PKT' :
        print(f'{40 + (weight * 70):.2f}')
    else :
        print('Error')
thunderxpress()
