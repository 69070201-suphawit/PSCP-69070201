"""overlapcircle"""
import math
def main():
    """doc"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    r = r1+r2
    d = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if d <= r :
        print("overlapping")
    else:
        print("no overlapping")
main()
