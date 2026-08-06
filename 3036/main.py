"""castle"""
import math
def castle():
    """main"""
    n = int(input())
    # กรณีพิเศษ ห้องที่ 1 ไม่มีผนัง
    if n == 1 :
        print(0)
        return
    # หาเลขชั้นของห้อง
    R = math.ceil(math.sqrt(n))
    # จำนวนห้องทั้งหมดก่อนถึงชั้นปัจจุบัน
    room_before = (R - 1) ** 2
    # หาตำแหน่งของห้องภายในชั้นนั้น
    P = n - room_before
    # ตรวจว่าตำแหน่งในชั้นเป็นเลขคี่หรือเลขคู่
    if P % 2 :
        # ถ้าเป็นเลขคี่ จำนวนผนังคำนวณด้วยสูตรนี้
        wall = 2 * (R - 1)
    else :
        #ถ้าเลขคู่ก็สูตรนี้
        wall = (2 * R) - 3
    print(wall)
castle()
