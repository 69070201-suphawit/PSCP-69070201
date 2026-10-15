"""smarttrashcollector"""
n = int(input())
names = ["Plastic", "Can", "Glass"]
for _ in range(n):
    w = list(map(float, input().split()))
    out = [f"{sum(w):.1f}"]
    if sum(w) > 50:
        out.append("Overloaded")
    for i in range(3):
        if w[i] > 20:
            out.append("Check Type " + names[i])
    print(", ".join(out))
