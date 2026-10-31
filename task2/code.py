


FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.05

bills = []


def calculate_energy(units):

    if units <= 100:
        energy = units * 1.50

    elif units <= 200:
        energy = (100 * 1.50) + ((units - 100) * 2.50)

    else:
        energy = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    return energy



n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units: "))


    energy = calculate_energy(units)

    
    fixed = FIXED_CHARGE

    
    surcharge = (energy + fixed) * SURCHARGE_RATE

  
    if units <= 100:
        rebate = energy * REBATE_RATE
    else:
        rebate = 0

    
    total = energy + fixed + surcharge - rebate

    bills.append([month, units, total])

    print("Energy Charges: Rs.", round(energy, 2))
    print("Fixed Charges: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))



print("\n----- MONTHLY BILL COMPARISON -----")

for i in range(len(bills)):

    print(bills[i][0], ":", round(bills[i][2], 2))

    if i > 0:

        previous = bills[i - 1][2]
        current = bills[i][2]

        increase = ((current - previous) / previous) * 100

        print("Bill Change:", round(increase, 2), "%")

        if increase > 30:
            print("WARNING: Unusual Bill Increase!")

        else:
            print("Normal Bill Change")

print("\nBilling Process Completed!")

