"""Resistor"""
digit = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
         "Green": 5, "Blue": 6, "Purple": 7, "Grey": 8, "White": 9}
mult = {"Black": 1, "Brown": 10, "Red": 100, "Orange": 1000,
        "Yellow": 10000, "Green": 100000, "Blue": 1000000,
        "Purple": 10000000, "Gold": 0.1, "Silver": 0.01}
tol = {"Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25,
       "Purple": 0.1, "Grey": 0.05, "Gold": 5, "Silver": 10}
c = []
for _ in range(4):
    c.append(input().strip().capitalize())
if c[0] in digit and c[1] in digit and c[2] in mult and c[3] in tol:
    value = (digit[c[0]] * 10 + digit[c[1]]) * mult[c[2]]
    low = value * (100 - tol[c[3]]) / 100
    high = value * (100 + tol[c[3]]) / 100
    print(f"{low:.4f}")
    print(f"{high:.4f}")
else:
    print("Error")
