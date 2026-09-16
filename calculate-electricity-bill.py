units = int(input("Enter number of units consumed: "))

if units > 500:
    amount = units * 9.25
    surcharges = 80

elif units >= 300:
    amount = units * 7.75
    surcharges = 70

elif units >= 200:
    amount = units * 5.25
    surcharges = 50

elif units >= 100:
    amount = units * 3.75
    surcharges = 30

else:
    amount = units * 2.25
    surcharges = 20

totalbill = amount + surcharges

print("Electricity bill = %.2f" % totalbill)