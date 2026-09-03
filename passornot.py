"""ผ่านหรือไม่"""
def main():
    """main"""
    n = int(input())
    total = 0
    all_pass = True
    for _ in range(n):
        score = int(input())
        total = total + score
        if score < 50:
            all_pass = False
    average = total / n
    print(f"{average:.1f}")
    if all_pass and average >= 60.0:
        print("PASS")
    else:
        print("FAIL")
main()
