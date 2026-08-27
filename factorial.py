"""factorial"""
def factorial():
    """main"""
    num = int(input())
    amount = 1
    for i in range(1, num + 1):
        amount *= i
    print(amount)
factorial()
