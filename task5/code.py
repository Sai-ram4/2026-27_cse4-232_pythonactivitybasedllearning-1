


print("===== RAILWAY RESERVATION SYSTEM =====")

classes = {
    "sleeper": 1.0,
    "ac3": 1.5,
    "ac2": 2.0
}

reservation_fee = 40


distance = float(input("Enter journey distance (KM): "))

if distance <= 0:
    print("Invalid journey distance!")
    exit()

print("\nAvailable Classes:")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")

travel_class = input("Enter travel class: ").strip().lower()

if travel_class not in classes:
    print("Invalid Travel Class!")
    exit()

number = int(input("Enter number of passengers: "))

if number <= 0:
    print("Invalid number of passengers!")
    exit()

total_amount = 0
total_refund = 0


for i in range(number):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    if age < 0 or age > 120:
        print("Invalid age! Please enter again.")
        exit()

    
    if distance <= 100:
        base_fare = distance * 1.0

    elif distance <= 500:
        base_fare = (100 * 1.0) + ((distance - 100) * 1.5)

    else:
        base_fare = (
            100 * 1.0
            + 400 * 1.5
            + (distance - 500) * 2.0
        )

    
    class_fare = base_fare * classes[travel_class]

    
    if age < 5:
        concession = 100
    elif age >= 60:
        concession = 20
    else:
        concession = 0

    concession_amount = class_fare * concession / 100

    
    if age < 5:
        reservation = 0
        final_fare = 0
    else:
        reservation = reservation_fee
        final_fare = (
            class_fare - concession_amount + reservation
        )

    total_amount += final_fare

    
    print("\n----- TICKET DETAILS -----")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Travel Class:", travel_class.upper())
    print("Distance:", distance, "KM")
    print("Basic Fare: Rs.", round(class_fare, 2))
    print("Concession:", concession, "%")
    print("Concession Amount: Rs.",
          round(concession_amount, 2))
    print("Reservation Fee: Rs.", reservation)
    print("Final Fare: Rs.", round(final_fare, 2))

    
    cancel = input("Cancel ticket? (yes/no): ").strip().lower()

    if cancel == "yes":

        
        if final_fare == 0:
            penalty = 0
        else:
            penalty = final_fare * 10 / 100

        refund = final_fare - penalty

        total_refund += refund
        total_amount -= final_fare

        print("Cancellation Penalty: Rs.",
              round(penalty, 2))
        print("Refund Amount: Rs.",
              round(refund, 2))

    else:
        print("Ticket Confirmed!")


print("\n===== RESERVATION SUMMARY =====")

print("Total Passengers:", number)
print("Total Active Booking Amount: Rs.",
      round(total_amount, 2))

print("Total Refund Amount: Rs.",
      round(total_refund, 2))

print("\nReservation Process Completed!")

