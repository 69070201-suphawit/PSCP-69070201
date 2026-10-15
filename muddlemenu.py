"""Muddle Menu"""
menu = []
line = input().strip()
while line != "DONE":
    if line == "SOMETHING'S WRONG":
        menu = []
    elif line == "CLOSED":
        menu = []
        break
    elif line.startswith("Can't do: "):
        name = line[len("Can't do: "):]
        if name in menu:
            menu.remove(name)
    else:
        name, num = line.rsplit(" #", 1)
        if num == "N":
            menu.append(name)
        else:
            menu.insert(int(num) - 1, name)
    line = input().strip()
print("Full Course:", menu, "Reversed:", menu[::-1])
