"""Imposter"""
players = {}
dead = {}
line = input()
while line != "Start":
    parts = line.strip("{}").split(":")
    name = parts[0].strip().strip('"')
    role = parts[1].strip().strip('"')
    players[name] = role
    line = input()
line = input()
while line != "End":
    role = players.pop(line)
    dead[line] = role
    line = input()
remain = list(players.values()).count("Impostor")
print(remain, "Impostor Remains")
print("***Alive***")
for name in sorted(players):
    print(name, ":", players[name])
print("***Dead***")
for name in sorted(dead):
    print(name, ":", dead[name])
