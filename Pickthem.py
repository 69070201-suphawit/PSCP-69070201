"""Pickthem"""
import json
data = json.loads(input())
found = False
for x in data:
    if not x % 2:
        print(x)
        found = True
if not found:
    print("Nope")
