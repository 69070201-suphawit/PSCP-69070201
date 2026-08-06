"""waterstatus"""
def waterstatus():
    """main"""
    temp_water = int(input())
    unit = input()
    if unit in 'F''f':
        Celcius = (temp_water - 32) / 1.8
    else :
        Celcius = temp_water
    if Celcius <= 0 :
        print("solid")
    elif Celcius >= 100 :
        print('gas')
    else :
        print('liquid')
waterstatus()
