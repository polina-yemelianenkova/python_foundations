import json
import pathlib

def input_int(msg:str) -> int:
    is_valid = False
    while not is_valid:
     try:
        number = int(input(msg))
        return number
     except ValueError:
        print("Error: enter an integer number.")


def create_newrecord(name, year) -> dict:
    return{
        "name": name,
        "year": year
    }

def display_record(record):
    print(f"Name: {record['name']}, Year: {record['year']}")

def main():
    file_path = pathlib.Path("./data/records.json")
    if not file_path.exists():
       with open(file_path, "w") as file:
           data = []
           json.dump(data, file)
    with open(file_path, "r") as file:
        data = json.load(file)
        for record in data:
            display_record(record)

    new_record = input("do you wish to create a new record? y/n: ")
    while new_record == 'y':
        name = input("What's the name?")
        year = input_int("What's the year?")
        new = create_newrecord(name, year)
        data.append(new)
        new_record = input("do you wish to create a new record? y/n: ")

    with open (file_path, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()