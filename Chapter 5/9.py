def main():
    feet = float(input("Enter the distance in feet: "))
    feet_to_inches(feet)

def feet_to_inches (feet):
    inches = feet * 12
    print(f"the {feet} feet are {inches} inches")

main()