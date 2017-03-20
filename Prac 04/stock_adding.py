
def main():
    incomes = []
    number_of_months_accounted = int(input("How many number_of_months_accounted? "))

    for month in range(1, number_of_months_accounted + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        str.format()
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months_accounted + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()