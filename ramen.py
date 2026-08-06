"""ramen"""
def ramen():
    """main"""
    size , flavor = input().split()
    topping_data = input().split()
    # กำหนดค่าเริ่มต้นให้ตัวแปร price เพื่อแก้ไข Undefined variable 'price'
    price = 0
    if size == 'S' :
        price = 60
    elif size == 'M' :
        price = 80
    elif size == 'L' :
        price = 100
    if flavor == 'T' :
        price += 20
    # คิดราคาท้อปปิ้ง
    # หากค่าที่รับมาในtopping มากกว่า1 จะเพิ่มตัว amountไปอีกเป็ฯค่าตัวที่2
    # หากค่าในtoppingไม่เกิน1 จะมีแค่toppingไม่มีamount
    if len(topping_data) >= 2 :
        topping_type = topping_data[0]
        amount = int(topping_data[1])
        if topping_type == 'P' :
            price += amount * 15
        elif topping_type == 'E' :
            price += amount * 10
    print(price)
ramen()
