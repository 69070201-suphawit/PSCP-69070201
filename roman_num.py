"""roman"""
def romannum():
    """main"""
    num = int(input())
    if num > 9 or not num :
        print('Error : Out of range')
    elif num < 0 :
        print('Error : Please input positive number')
    else :
        roman_list = [ 'I' , 'II' , 'III' , 'IV' , 'V' , 'VI' , 'VII' , 'VIII' , 'IX' ]
    # ดึงค่าออกมา (num - 1 เพราะ List เริ่มต้นที่ Index 0)
        print(roman_list[num-1])
romannum()
