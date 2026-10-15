"""arrayhahe"""
arr = [0] * 50
for i in range(3):
    arr[i] = int(input())
    print("Input number", i + 1, "stored.")
data = arr[:3]
while True:
    choice = int(input())
    if not choice:
        break
    if choice == 1:
        print("Original order:", *data)
    elif choice == 2:
        print("Descending order:", *sorted(data, reverse=True))
    elif choice == 3:
        print("Ascending order:", *sorted(data))
