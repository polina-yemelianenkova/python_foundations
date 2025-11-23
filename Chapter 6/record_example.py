def input_name():
    name = input("Please enter the first name: ")
    while not name:
        print("Error: enter a name: ")
        name = input("Please enter the first name: ")
    return name

def input_year():
    year = input("Please enter the year: ")
    while year == "":
        print("Error: enter a year: ")
        year = int(input("Please enter the year: "))
    return int(year)

def print_record(name, year):
    print(f"Name: {name}, Year: {year}")


def main():
    file_path = "./data/names.txt"
    print("Welcome!")
    new_record = input("Would you like to create new record?")
    while new_record == "":
        print("Error: enter y or n")
        new_record = input("Would you like to create new record?")

    while new_record == "y":
        name = input_name()
        year = input_year()
        with open (file_path, "a") as file:
            file.write(f"{name} {year}\n")
        new_record = input("Would you like to add another? ")

    with open (file_path) as file:
        for line in file:
            name, year = line.rstrip("\n").split(" ")
            print_record(name, year)

if __name__ == "__main__":
    main()
