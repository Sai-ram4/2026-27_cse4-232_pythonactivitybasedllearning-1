


print("===== WAREHOUSE INVENTORY SYSTEM =====")
n = int(input("Enter Number of Products: "))

if n <= 0:
    print("Invalid Number of Products!")
    exit()


total_opening = 0
total_incoming = 0
total_dispatched = 0
total_closing = 0
total_discrepancies = 0


inventory = []


for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter Product Name: ")

    opening = int(input("Enter Opening Stock: "))
    incoming = int(input("Enter Incoming Stock: "))
    dispatched = int(input("Enter Dispatched Stock: "))
    actual_closing = int(input("Enter Actual Closing Stock: "))
    minimum_stock = int(input("Enter Minimum Stock Level: "))

  
    if (opening < 0 or incoming < 0 or
        dispatched < 0 or actual_closing < 0 or
        minimum_stock < 0):

        print("Invalid Stock Quantity!")
        exit()

    if dispatched > opening + incoming:
        print("Error: Dispatched stock exceeds available stock!")
        exit()

    
    expected_closing = opening + incoming - dispatched

    
    discrepancy = actual_closing - expected_closing

    
    replenishment = max(
        0, minimum_stock - actual_closing
    )

    
    if discrepancy == 0:
        status = "Stock Matched"
    else:
        status = "Discrepancy Detected"
        total_discrepancies += 1

    
    inventory.append([
        name,
        opening,
        incoming,
        dispatched,
        expected_closing,
        actual_closing,
        discrepancy,
        replenishment,
        status
    ])

    
    total_opening += opening
    total_incoming += incoming
    total_dispatched += dispatched
    total_closing += actual_closing


print("\n===== INVENTORY RECONCILIATION REPORT =====")

for item in inventory:

    print("\nProduct Name:", item[0])
    print("Opening Stock:", item[1])
    print("Incoming Stock:", item[2])
    print("Dispatched Stock:", item[3])
    print("Expected Closing Stock:", item[4])
    print("Actual Closing Stock:", item[5])
    print("Discrepancy:", item[6])
    print("Replenishment Required:", item[7])
    print("Status:", item[8])

# Final Summary
print("\n===== WAREHOUSE SUMMARY =====")

print("Total Opening Stock:", total_opening)
print("Total Incoming Stock:", total_incoming)
print("Total Dispatched Stock:", total_dispatched)
print("Total Actual Closing Stock:", total_closing)

print("Products With Discrepancies:",
      total_discrepancies)

total_replenishment = sum(
    item[7] for item in inventory
)

print("Total Replenishment Required:",
      total_replenishment)

print("\nInventory Reconciliation Completed!")

