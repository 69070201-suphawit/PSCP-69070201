"""Coke"""
price = int(input())
cap = int(input())
new_price = int(input())
bottle = int(input())
# ตรวจก่อนว่ามีโปรมั้ย
if not bottle:
    print(0)
# ถ้า bottle == 0 หรือก็คือไม่ซื้อเลย จ่าย 0 บาท ใช้โปรไม่คุ้ม
elif not cap or new_price >= price:
    print(bottle*price)
# กรณีที่ 3: มีโปรโมชั่นที่คุ้มค่า (new_price ถูกกว่า price)
else:
# จ่ายขวดแรกในราคาเต็มไปก่อน 1 ขวดเพื่อให้ขวดที่เหลือหารลงตัวเป็นกลุ่มโปรได้
    remain_bottle = bottle - 1
# ราคาต่อ 1 ชุดโปรโมชั่น คือ ซื้อ (cap-1) * ขวดราคาปกติ + ขวดราคาพิเศษ
    promotion = ((cap - 1) * price) + new_price
# หาว่าขวดที่เหลือ (remain_bottle) แบ่งเป็นชุดโปรโมชั่นได้กี่ชุดเต็มๆ
    full_promotion = remain_bottle // cap
# ขวดที่เหลือจากการแบ่งชุดโปร (แบ่งไม่ครบ 1 ชุด) ต้องจ่ายราคาปกติ
    left_promotion = remain_bottle % cap
# รวมราคาทั้งหมด
    totalcost = ( price + ( full_promotion * promotion ) + (left_promotion * price ))
    print(totalcost)
