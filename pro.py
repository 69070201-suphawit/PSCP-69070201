"""pro"""
def main():
    """main"""
    mar = int(input())
    pay = int(input())
    price = int(input())
    come = int(input())
    group = come // mar
    aloneguy = come % mar
    total = (group*pay*price) + (aloneguy * price)
    print(total)

main()
