def get_file_path()->str:
    file_name = input("Plese enter the name of the file: ")
    file_path = f"./data/{file_name}"
    return file_path


def read_file(file_path:str):
    with open (file_path, "r") as file:
        for idx, line in enumerate(file):
            if idx == 5:
                break
            print(line.rstrip())
            

if __name__ == "__main__":
    file_path = get_file_path()
    read_file(file_path)
