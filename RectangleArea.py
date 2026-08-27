"""rectangle_overlap"""
def calculate_overlap():
    """main"""
    rect_a = list(map(int, input().split()))
    rect_b = list(map(int, input().split()))

    overlap_w = min(rect_a[0] + rect_a[2], rect_b[0] + rect_b[2]) - max(
        rect_a[0], rect_b[0]
    )
    overlap_h = min(rect_a[1] + rect_a[3], rect_b[1] + rect_b[3]) - max(
        rect_a[1], rect_b[1]
    )

    if overlap_w > 0 and overlap_h > 0:
        print(overlap_w * overlap_h)
    else:
        print("no overlapping")
calculate_overlap()
