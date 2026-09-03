"""จำนวนเฉพาะ"""
a, b = input().split()
start = int(a)
end = int(b)
prime_list = []

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if not num % i:
                break
        else:
            prime_list.append(num)
if prime_list:
    print(*prime_list)
print("Total primes:",len(prime_list))
