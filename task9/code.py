
from datetime import datetime


rates = {
    "bike": 10,
    "car": 20,
    "bus": 40
}

DAILY_LIMIT = {
    "bike": 100,
    "car": 200,
    "bus": 400
}

PENALTY = 50

try:
    print("===== SMART PARKING FEE MANAGEMENT =====")

    
    vehicle = input("Enter vehicle type (Bike/Car/Bus): ").lower()

    if vehicle not in rates:
        raise ValueError("Invalid vehicle category!")

    
    entry = input("Enter entry time (HH:MM): ")
    exit_time = input("Enter exit time (HH:MM): ")

    
    entry_time = datetime.strptime(entry, "%H:%M")
    exit_time = datetime.strptime(exit_time, "%H:%M")

  
    entry_minutes = entry_time.hour * 60 + entry_time.minute
    exit_minutes = exit_time.hour * 60 + exit_time.minute

    
    if exit_minutes <= entry_minutes:
        exit_minutes += 24 * 60

    duration = exit_minutes - entry_minutes

    
    hours = (duration + 59) // 60

    
    rate = rates[vehicle]
    daily_limit = DAILY_LIMIT[vehicle]

    total_fee = 0
    remaining_hours = hours

    while remaining_hours > 0:
        current_hours = min(remaining_hours, 24)
        daily_fee = min(current_hours * rate, daily_limit)
        total_fee += daily_fee
        remaining_hours -= current_hours

    
    penalty = 0
    if duration > 24 * 60:
        penalty = PENALTY

    final_fee = total_fee + penalty

    
    print("\n===== PARKING BILL =====")
    print("Vehicle Type:", vehicle.capitalize())
    print("Entry Time:", entry)
    print("Exit Time:", exit_time.strftime("%H:%M"))
    print("Parking Duration:", hours, "hours")
    print("Hourly Rate: Rs.", rate)
    print("Parking Fee: Rs.", total_fee)
    print("Penalty: Rs.", penalty)
    print("Total Amount: Rs.", final_fee)

except ValueError as error:
    print("Error:", error)

