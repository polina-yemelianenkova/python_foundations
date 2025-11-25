def read_file_into_list()->list:
    list = []
    file_path = "Chapter 7/charge_accounts.txt"
    with open (file_path,"r") as file:
        for i in file:
            list.append(i.rstrip())
    print(list)
    return list

def search(list:list):
    charge_number = input("Please enter the charge number: ")
    if charge_number in list:
        print("Found!")
    else:
        print("Not found.")

search(read_file_into_list())

    


