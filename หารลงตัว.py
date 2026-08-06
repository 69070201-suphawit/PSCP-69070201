"""หารลงตัว"""
def main():
    """main"""
    num_1 = int(input())
    num_2 = int(input())
    if not num_2 :
        print('no')
        return
    if not num_1 % num_2 :
        print('yes')
    else :
        print('no')
main()
