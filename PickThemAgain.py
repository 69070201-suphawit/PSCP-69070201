"""pickthem"""
nums = list(map(int, input().split()))
result = []
for x in nums:
    if not x % 3 or not x % 5 :
        result.append(x)

if not result:
    print("Nope")
else:
    for x in (result[::-1]):
        print(x)
