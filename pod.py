"""pod"""
def calculate_remaining_passengers():
    """main"""
    first_line = input().split()
    n = int(first_line[0])
    k = int(first_line[1])

    line_counts = [0] * (k + 1)

    for _ in range(n):
        line_num = int(input())
        line_counts[line_num] += 1

    max_pods = min(line_counts[1 : k + 1])
    remaining_passengers = n - (max_pods * k)

    print(remaining_passengers)
calculate_remaining_passengers()
