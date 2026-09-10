"""hotel room decoder"""
def get_first(d):
    """hotel"""
    if d[0] > 5:
        return 9
    if d[1] > 5:
        return 10
    if d[2] > 5:
        return 11
    if d[3] > 5:
        return 12
    if d[4] > 5:
        return 14
    return 13
def get_second(d):
    """main"""
    palindrome = d[0] == d[4] and d[1] == d[3]
    if palindrome:
        if d[0] + d[4] > 5:
            return 1
        if d[1] * d[3] > 5:
            return 2
        return 0
    if d[4] and round(d[0] / d[4]) > 5:
        return 1
    if d[1] - d[4] > 5:
        return 2
    return 0
def get_third(d):
    """main"""
    total_sum = sum(d)
    total_product = 1
    for x in d:
        total_product *= x
    if total_sum > 25:
        return 1
    if total_product > 55:
        return 2
    return 0
def main():
    """main"""
    n = input().strip().zfill(5)
    d = [int(c) for c in n]
    first = get_first(d)
    second = get_second(d)
    third = get_third(d)
    print(f"{first}{second}{third}")
main()
