"""countsara"""
text = input()
sara = ["a","e","i","o","u"]
count = 0
for char in text :
    if char in sara :
        count += 1
print(count)
