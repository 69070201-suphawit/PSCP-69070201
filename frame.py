"""elo"""

def main():
    """elo"""
    RA = int(input())
    RB = int(input())
    side = input()
    if side == "A":
        EA = 1/(1+10**((RB-RA)/400))
        print(f"{EA:.2f}")
    elif side == "B":
        EB = 1/(1+10**((RA-RB)/400))
        print(f"{EB:.2f}")

main()
