"""BusStop"""
p = int(input())
n = int(input())
stops = []
for _ in range(n):
    line = input().split()
    if line:
        stops.append(list(map(int, line)))
stops.sort()
bus = []
count = 0
for s in stops:
    here = s[0]
    stay = []
    for d in bus:
        if d == here:
            count += 1
        else:
            stay.append(d)
    bus = stay
    for d in s[1:]:
        if len(bus) < p and d > here:
            bus.append(d)
print(count)
