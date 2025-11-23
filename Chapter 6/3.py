file_name = input("Plese enter the name of the file: ")
file_path = f"./data/{file_name}"

counter = 0

with open (file_path, 'r') as file:
    
    for line in file:
        counter+=1
        print(f"{counter}:", line.rstrip())
    