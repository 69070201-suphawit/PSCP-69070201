"""B-Fullypair?"""
text = input().strip()
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
result = ""
for ch, num in count.items():
    if num % 2 == 1:
        result += ch
if not result:
    print("fully paired")
else:
    print(result)
