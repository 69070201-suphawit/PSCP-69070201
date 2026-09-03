"""สินค้าส่งออก"""
num = int(input())
all_list = []
even_list = []
odd_list = []

for _ in range(num):
    num2 = int(input())
    all_list.append(num2)
    if not num2 % 2:
        even_list.append(num2)
    else:
        odd_list.append(num2)

print("SUM", sum(all_list))
print("EVEN", len(even_list))
print("ODD", len(odd_list))
