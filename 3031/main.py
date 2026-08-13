"""ink"""
import math
def calculate_flooded_time():
    """main"""
    s_val, n_val = map(int, input().split())

    for _ in range(n_val):
        x_pos, y_pos = map(int, input().split())

        r_squared = x_pos * x_pos + y_pos * y_pos
        area_needed = 3.1416 * r_squared
        exact_time = area_needed / s_val

        flooded_second = math.ceil(exact_time)
        print(flooded_second)
calculate_flooded_time()
