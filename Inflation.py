"""infaction"""
def infac():
    """main"""
    n_str = input().strip()
    k = int(input())
    n_satang = round(float(n_str) * 100)
    rate_num = 381
    rate_den = 10000
    for _ in range(k):
        n_satang = (n_satang * (rate_den + rate_num)) // rate_den
    baht = n_satang // 100
    satang = n_satang % 100
    print(f"{baht}.{satang:02d}")
infac()
