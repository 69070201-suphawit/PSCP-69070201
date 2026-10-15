"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
def main():
    """Calculate defective tiles and penalty."""
    n, penalty = input().split()
    n = int(n)
    penalty = float(penalty)

    tiles = []
    for _ in range(n):
        row = list(map(int, input().split()))
        tiles.append(row)

    total_bad_tiles = 0
    total_bad_points = 0

    col_bad_tiles = [0] * n
    col_bad_points = [0] * n

    for row in tiles:
        bad_tiles = 0
        bad_points = 0

        for j in range(n):
            if row[j] > 0:
                bad_tiles += 1
            bad_points += row[j]

            if row[j] > 0:
                col_bad_tiles[j] += 1
            col_bad_points[j] += row[j]

        total_bad_tiles += bad_tiles
        total_bad_points += bad_points

        print(*row, bad_tiles, bad_points)

    print(*col_bad_tiles)
    print(*col_bad_points)

    print(total_bad_tiles, total_bad_points,
          f"{total_bad_points * penalty:.2f}")
main()
