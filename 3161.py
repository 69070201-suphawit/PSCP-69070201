"""แสดงสัญลักษณ์ตามตำแหน่งที่หาร 5"""
def main():
    """main"""
    n = int(input())
    result = ""
    for position in range(1, n + 1):
        if not position % 5:
            result = result + "X"
        else:
            result = result + "*"
    print(result)
main()
