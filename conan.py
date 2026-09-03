"""CONAN"""
def main():
    """main"""
    text = input()
    k = int(input())
    result = ""
    for char in text:
        position = ord(char) - ord('a')
        position = position + k
        position = position % 26
        new_char = chr(position + ord('a'))
        result = result + new_char
    print(result)
main()
