


print("===== ATTENDANCE RECOVERY CALCULATOR =====")


total_classes = int(input("Enter Total Classes Conducted: "))
attended_classes = int(input("Enter Classes Attended: "))

threshold = float(input("Enter Eligibility Percentage: ")
if total_classes <= 0:
    print("Invalid Total Classes!")
    exit()

if attended_classes < 0 or attended_classes > total_classes:
    print("Invalid Attended Classes!")
    exit()

if threshold <= 0 or threshold > 100:
    print("Invalid Eligibility Percentage!")
    exit()


current_percentage = (
    attended_classes / total_classes
) * 100

print("\n===== CURRENT ATTENDANCE =====")

print("Total Classes:", total_classes)
print("Classes Attended:", attended_classes)

print("Current Attendance:",
      round(current_percentage, 2), "%")

print("Eligibility Threshold:", threshold, "%")

if current_percentage >= threshold:

    print("\nStatus: ELIGIBLE")
    print("You have already reached the attendance target.")

else:

    print("\nStatus: NOT ELIGIBLE")

    
    required_classes = 0

    while (
        attended_classes + required_classes
    ) / (
        total_classes + required_classes
    ) * 100 < threshold:

        required_classes += 1

    print("\nMinimum Consecutive Classes Required:",
          required_classes)

    
    scenarios = {
        "100% Attendance": 1.0,
        "90% Attendance": 0.9,
        "80% Attendance": 0.8
    }

    print("\n===== FUTURE ATTENDANCE SCENARIOS =====")

    for scenario, rate in scenarios.items():

        future_classes = required_classes

        future_attended = round(
            future_classes * rate
        )

        final_attended = (
            attended_classes + future_attended
        )

        final_total = (
            total_classes + future_classes
        )

        final_percentage = (
            final_attended / final_total
        ) * 100

        print("\nScenario:", scenario)

        print("Future Classes:", future_classes)

        print("Future Classes Attended:",
              future_attended)

        print("Final Attendance:",
              round(final_percentage, 2), "%")

        if final_percentage >= threshold:
            print("Status: ELIGIBLE")
        else:
            print("Status: NOT ELIGIBLE")

print("\nAttendance Calculation Completed!")

