"""milktea"""
def parse_num(s):
    "docstring"
    try:
        return int(s) # ลองแปลงเป็น int ก่อน (เช่น "10" -> 10)
                      # ถ้าสำเร็จ จะ return ค่าตรงนี้เลย ไม่ทำงานส่วน except
    except ValueError: # ถ้าบรรทัดข้างบน error แบบ ValueError
        return float(s) # # ให้กระโดดมาทำบรรทัดนี้แทน -> แปลงเป็น float ("2.5" -> 2.5)
# อะไรที่เป็นจำนวนจะเรียกใช้ฟังก์ชั่นนี้หมด
def milktea():
    """yes"""
    bubble = input().split()
    bubble_type = bubble[0]
    bubble_amount = parse_num(bubble[1])
    tea = input().split()
    tea_type = tea[0]
    sweet_level = parse_num(tea[1])
    tea_amount = parse_num(tea[2])
    cal = 0
    if bubble_type == 'H':
        cal = bubble_amount * 5
    elif bubble_type == 'O':
        cal = bubble_amount * 3
    elif bubble_type == 'J':
        cal = bubble_amount * 2
    if tea_type == 'R' and sweet_level == 1:
        cal += (12 * tea_amount)
    if tea_type == 'R' and sweet_level == 2:
        cal += (18 * tea_amount)
    if tea_type == 'R' and sweet_level == 3:
        cal += (25 * tea_amount)
    if tea_type == 'T' and sweet_level == 1:
        cal += (15 * tea_amount)
    if tea_type == 'T' and sweet_level == 2:
        cal += (20 * tea_amount)
    if tea_type == 'T' and sweet_level == 3:
        cal += (30 * tea_amount)
    if tea_type == 'M' and sweet_level == 1:
        cal += (10 * tea_amount)
    if tea_type == 'M' and sweet_level == 2:
        cal += (15 * tea_amount)
    if tea_type == 'M' and sweet_level == 3:
        cal += (20 * tea_amount)
    print(cal)
milktea()
