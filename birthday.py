"""birthday"""
from datetime import date # นำเข้า date เพื่อใช้สร้างวันที่และคำนวณวัน
def birthday():
    """main"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    y2 = int(input())
    m2 = int(input())
    d2 = int(input())
    # สร้างวันที่จากข้อมูลที่รับมา
    date1 = date(y1,m1,d1)
    date2 = date(y2,m2,d2)
    # หาจำนวนวันที่ห่างกันโดยที่date1 - date2 จะได้ช่วงเวลาที่ต่างกัน
    # .days เพื่อดึงจำนวนวันออกมาและabs()เพื่อทำให้เป็นค่าบวกเสมอ
    diff = abs((date1-date2).days)
    # ถ้าวันที่ห่างกันไม่เกิน 7 วัน
    if diff <= 7:
        print(0)
    # ถ้า date1 มาก่อน date2
    elif date1 < date2:
        print(1)
    # นอกนั้นแสดงว่า date1 มาหลัง date2
    else:
        print(2)
birthday()
