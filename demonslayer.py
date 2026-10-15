"""demonslayer"""
from collections import deque
q = deque([
    ("Spider Demon", 1),
    ("Swamp Demon", 2),
    ("Arrow Demon", 1),
    ("Hand Demon", 2),
    ("Drum Demon", 3),
    ("Mugen Train", 2),
    ("Upper Moon", 3),
])
kills = 0
attacks = 0
while kills < 5:
    name, secret = q.popleft()
    print(name)
    killed = False
    for _ in range(2):
        a = int(input())
        attacks += 1
        if a == secret:
            killed = True
            break
    if killed:
        print("kill")
        kills += 1
    else:
        print("back")
        q.append((name, secret))
print(attacks)
