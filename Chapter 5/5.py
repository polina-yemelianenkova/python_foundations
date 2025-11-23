def main():
    actual_value = float(input("Please enter the value: "))
    calculatePropertyTax(actual_value)


def calculatePropertyTax(actual_value):
    assessment_value = actual_value * 0.6
    property_tax = assessment_value * 0.0072
    print("assessment_value is: ", assessment_value)
    print ("property_tax: ", property_tax)

main()

    