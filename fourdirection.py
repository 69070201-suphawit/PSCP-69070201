"""fourdirection"""
arrows = {
    "U": ["  *  ", " *** ", "* * *", "  *  ", "  *  "],
    "D": ["  *  ", "  *  ", "* * *", " *** ", "  *  "],
    "L": ["  *  ", " *   ", "*****", " *   ", "  *  "],
    "R": ["  *  ", "   * ", "*****", "   * ", "  *  "],
}
s = input().strip()
for row in range(5):
    line = ""
    for c in s:
        line += arrows[c][row] + " "
    print(line)
