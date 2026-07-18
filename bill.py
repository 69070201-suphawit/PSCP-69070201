"""Bill"""
def main():
    """main"""

    price = int(input())
    service = (price * 10) / 100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    vat = (price + service) * 7 / 100
    print(f"{price + service + vat:.2f}")

main()
