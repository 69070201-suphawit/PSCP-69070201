"""giftandthief"""
def main():
    """main"""
    line = input()
    numbers = line.split()
    n = int(numbers[0])
    k = int(numbers[1])
    t = int(numbers[2])
    current_person = 1
    count = 1
    if current_person == t:
        print(count)
        return
    while True:
        index = current_person - 1
        index = index + k
        index = index % n
        next_person = index + 1
        if next_person == 1:
            break
        count = count + 1
        current_person = next_person
        if current_person == t:
            break
    print(count)
main()
