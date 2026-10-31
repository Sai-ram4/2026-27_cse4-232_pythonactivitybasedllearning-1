



storage_limits = {
    "A": 100,
    "B": 80,
    "C":60,
allowed_groups = ["X", "Y", "Z"]


incompatible_pairs = [
    ("X", "Y")
]

inventory = []
errors = []

print("===== LABORATORY INVENTORY VALIDATION =====")

try:
    n = int(input("Enter number of inventory records: "))

    if n <= 0:
        raise ValueError("Number of records must be positive.")

    
    for i in range(n):
        print("\nRecord", i + 1)

        name = input("Enter item name: ")
        category = input("Enter storage category (A/B/C): ").upper()
        group = input("Enter compatibility group (X/Y/Z): ").upper()
        quantity = float(input("Enter quantity: "))

        record = {
            "name": name,
            "category": category,
            "group": group,
            "quantity": quantity
        }

        inventory.append(record)

  
    for item in inventory:

        if item["category"] not in storage_limits:
            errors.append(
                item["name"] + ": Invalid storage category"
            )
            continue

        if item["group"] not in allowed_groups:
            errors.append(
                item["name"] + ": Invalid compatibility group"
            )
            continue

        if item["quantity"] <= 0:
            errors.append(
                item["name"] + ": Quantity must be positive"
            )

    
    category_totals = {}

    for item in inventory:
        category = item["category"]

        if category in storage_limits and item["quantity"] > 0:
            category_totals[category] = (
                category_totals.get(category, 0)
                + item["quantity"]
            )

  
    for category, total in category_totals.items():

        if total > storage_limits[category]:
            errors.append(
                f"Category {category}: Quantity limit exceeded "
                f"({total} > {storage_limits[category]})"
            )

    
    for i in range(len(inventory)):
        for j in range(i + 1, len(inventory)):

            item1 = inventory[i]
            item2 = inventory[j]

            if (
                item1["category"] == item2["category"]
                and item1["category"] in storage_limits
                and item1["group"] in allowed_groups
                and item2["group"] in allowed_groups
            ):

                pair = (item1["group"], item2["group"])
                reverse_pair = (item2["group"], item1["group"])

                if (
                    pair in incompatible_pairs
                    or reverse_pair in incompatible_pairs
                ):
                    errors.append(
                        f"Compatibility violation: "
                        f"{item1['name']} and {item2['name']} "
                        f"in Category {item1['category']}"
                    )

    
    print("\n===== INVENTORY VALIDATION REPORT =====")

    for category, total in category_totals.items():
        print(
            f"Category {category}: {total} / "
            f"{storage_limits[category]} units"
        )

    if errors:
        print("\nINVALID RECORDS / COMBINATIONS:")

        for error in errors:
            print("-", error)

        print("\nStatus: VALIDATION FAILED")

    else:
        print("\nAll inventory records are valid.")
        print("Status: VALIDATION SUCCESSFUL")

    print("\nTotal Records:", len(inventory))
    print("Total Issues:", len(errors))

except ValueError as error:
    print("\nInput Error:", error)

