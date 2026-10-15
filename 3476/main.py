"""CuteCat CuteFox"""
n = int(input())
group = {}
for _ in range(n):
    line = input().strip().strip("{}")
    k, v = line.split(":")
    k = k.strip().strip('"').strip("'")
    v = v.strip().strip('"').strip("'")
    group[k] = v
if "Cat01" not in group.values() and "Garfield" not in group:
    group["Garfield"] = "Cat01"
if "Fox01" not in group.values() and "Fubuki" not in group:
    group["Fubuki"] = "Fox01"
cats = {name: code for name, code in group.items() if code.startswith("Cat")}
foxes = {name: code for name, code in group.items() if code.startswith("Fox")}
print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")
for name in sorted(cats, key=lambda nm: int("".join(ch for ch in cats[nm] if ch.isdigit()))):
    print(f"{name} : {cats[name]}")
for name in sorted(foxes, key=lambda nm: int("".join(ch for ch in foxes[nm] if ch.isdigit()))):
    print(f"{name} : {foxes[name]}")
