"""password generator"""
def main():

    """main"""
    name = input()
    lastname = input()
    age = input()
    if  len(name) >= 5 and len(lastname) >= 5:
        password = name[0:2] + lastname[-1:] + age[-1:]
        print(password)
    else:
        password = name[0] + age + lastname[-1]
        print(password)
main()
