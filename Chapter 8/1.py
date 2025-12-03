def main():
    full_name = input("Please enter full name: ")

    name = full_name.split()

    for string in name:
        print(string[0].upper(), end="")
        print(".", end = " ")

main()