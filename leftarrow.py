"""leftarrow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     nnnnnnnnnnnnnnnnnnnn"""
k = int(input())
n = int(input())
mid = n // 2
for i in range(n):
    diff = abs(i - mid)
    print(' ' * diff + '*' * k)
