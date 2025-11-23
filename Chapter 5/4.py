def main():
    loan_payment = float(input("Enter the loan payment: "))
    insurance = float(input("Enter the insurance payment: "))
    gas = float(input("Enter the gas payment: "))
    oil = float(input("Enter the oil payment: "))
    tires = float(input("Enter the tires payment: "))
    maintenance = float(input("Enter the maintenance payment: "))
    costs(loan_payment,insurance,gas,oil,tires,maintenance)


def costs(loan_payment,insurance,gas,oil,tires,maintenance):
 
    total = loan_payment + insurance + gas + oil + tires + maintenance
    annual = total * 12

    print("Total is: ", total)
    print("Annual payment is: ", annual)

main()