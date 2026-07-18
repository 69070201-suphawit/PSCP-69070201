"""calculator"""
def main():
    """main"""
    n = int(input())
    if n == 1 :
        print('1')
    else :
        total_presses = 1 + (n - 1)
        for i in range(1, n + 1):
            total_presses += len(str(i))
        print(total_presses)
main()
