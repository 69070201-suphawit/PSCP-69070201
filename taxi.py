"""taxi"""
def taxi():
    """main"""
    distance = int(input())
    if distance <= 0 :
        price = 0
    elif distance <= 1 :
        price = 35
        # 35(กม.แรก) + ระยะทาง - 1 * 5 บาท คือเกิน1กิโล+5บาท
    elif distance <= 10 :
        price = 35 + (distance - 1) * 5
    else :
        # 35 (กม.แรก) + 45 (9 กม.ถัดมา * 5 บาท) + (ส่วนที่เกิน 10 กม. * 8 บาท)
        price = 35 + 45 + (distance - 10) * 8
    print(price)
taxi()
