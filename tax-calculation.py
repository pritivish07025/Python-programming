# Program for tax calculation

name = input("Enter name of the person: ")
salary = float(input("Enter salary: "))

if salary > 5000:
    tax = 0.10 * salary
    netsalary = salary - tax

    print("Tax amount is:", tax)
    print("The net salary of " + name + " is", netsalary)

else:
    netsalary = salary

    print("No taxable amount")
    print("The net salary of " + name + " is", netsalary)