


print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")


usage = float(input("Enter monthly data usage (GB): "))
required_validity = int(input("Enter required validity days: "))
budget = float(input("Enter your budget (Rs.): ")
if usage < 0 or required_validity <= 0 or budget < 0:
    print("Invalid Input!")
    exit()


plans = [
    {
        "name": "Basic Plan",
        "price": 149,
        "data": 2,
        "validity": 28,
        "extra": 20
    },
    {
        "name": "Smart Plan",
        "price": 249,
        "data": 10,
        "validity": 28,
        "extra": 15
    },
    {
        "name": "Premium Plan",
        "price": 399,
        "data": 30,
        "validity": 56,
        "extra": 10
    },
    {
        "name": "Unlimited Plan",
        "price": 599,
        "data": 50,
        "validity": 84,
        "extra": 5
    }
]

eligible_plans = []

print("\n===== PLAN COMPARISON =====")


for plan in plans:

    excess_data = max(0, usage - plan["data"])

    excess_charge = excess_data * plan["extra"]

    total_cost = plan["price"] + excess_charge

    print("\nPlan:", plan["name"])
    print("Plan Price: Rs.", plan["price"])
    print("Data Limit:", plan["data"], "GB")
    print("Validity:", plan["validity"], "days")
    print("Excess Data:", excess_data, "GB")
    print("Excess Charge: Rs.", excess_charge)
    print("Total Cost: Rs.", total_cost)

    
    if (plan["data"] >= usage and
        plan["validity"] >= required_validity and
        total_cost <= budget):

        eligible_plans.append({
            "name": plan["name"],
            "cost": total_cost,
            "validity": plan["validity"],
            "data": plan["data"]
        })


print("\n===== BEST PLAN RESULT =====")

if len(eligible_plans) > 0:

    best_plan = min(
        eligible_plans,
        key=lambda x: x["cost"]
    )

    print("Best Plan:", best_plan["name"])
    print("Total Cost: Rs.", best_plan["cost"])
    print("Data Limit:", best_plan["data"], "GB")
    print("Validity:", best_plan["validity"], "days")

else:
    print("No eligible plan found!")
    print("Please increase your budget or adjust your requirements.")

print("\nOptimization Completed!")

