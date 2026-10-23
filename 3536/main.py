"""isPrime_large"""
n = int(input())
if n < 2:
    print("NO")
else:
    limit = int(n ** 0.5)
    is_prime = True
    i = 2
    while i <= limit:
        if not n % i:
            is_prime = False
            break
        i += 1
    print("YES" if is_prime else "NO")
