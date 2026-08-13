"""wonderland_milk"""
def calculate_max_milk():
    """ฟังก์ชันคำนวณจำนวนนมวัวสูงสุดที่ลูกค้าจะได้รับ"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    initial_bottles = d // a
    total_bottles = initial_bottles
    current_caps = initial_bottles

    if b > 0 and c > 0:
        while current_caps >= b:
            exchanged_bottles = (current_caps // b) * c
            total_bottles += exchanged_bottles
            current_caps = (current_caps % b) + exchanged_bottles
    print(total_bottles)
calculate_max_milk()
