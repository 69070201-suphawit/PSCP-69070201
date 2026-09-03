"""ATM withdrawal program."""


def main():
    """Main function."""
    money = int(input())

    if 100 <= money <= 20000 and money % 100 == 0:
        b1000 = money // 1000
        money = money % 1000

        b500 = money // 500
        money = money % 500

        b100 = money // 100

        print("1000:", b1000)
        print("500:", b500)
        print("100:", b100)
    else:
        print("ERROR")


main()
