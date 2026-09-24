"""movie_ticket"""
def main():
    """main"""
    seat = int(input())
    while seat > 0:
        try:
            age, amount = map(int, input().split())
        except EOFError:
            break
        if age < 15 :
            print(-1)
        elif amount > seat :
            print(-2)
        else :
            if 15 <= age <= 22:
                Price = 120
            elif age >= 60 :
                Price = 75
            else :
                Price = 150
            seat -= amount
            print(Price * amount,seat)
main()
