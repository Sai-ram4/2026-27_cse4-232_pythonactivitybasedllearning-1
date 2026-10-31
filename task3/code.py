


print("===== HOSPITAL BILLING SYSTEM =====")


name = input("Enter Patient Name: ")

age = int(input("Enter Patient Age: "))

patient_type = input(
    "Enter Patient Type (General/Senior/Insurance): "
).strip().lower()


if age <= 0 or age > 120:
    print("Invalid Age!")
    exit()

if patient_type not in ["general", "senior", "insurance"]:
    print("Invalid Patient Type!")
    exit()


consultation = float(input("Enter Consultation Charges: "))
diagnostic = float(input("Enter Diagnostic Charges: "))
treatment = float(input("Enter Treatment Charges: "))


if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid Charges! Negative values are not allowed.")
    exit()


total = consultation + diagnostic + treatment


if patient_type == "senior":
    concession_rate = 10

elif patient_type == "insurance":
    concession_rate = 20

else:
    concession_rate = 0


concession = total * concession_rate / 100


final_bill = total - concession

if final_bill < 5000:
    classification = "Low Payment"

elif final_bill <= 15000:
    classification = "Medium Payment"

else:
    classification = "High Payment"


print("\n===== PATIENT BILL DETAILS =====")

print("Patient Name:", name)
print("Patient Age:", age)
print("Patient Type:", patient_type.capitalize())

print("--------------------------------")
print("Consultation Charges: Rs.", consultation)
print("Diagnostic Charges: Rs.", diagnostic)
print("Treatment Charges: Rs.", treatment)

print("--------------------------------")
print("Total Bill: Rs.", round(total, 2))
print("Concession:", concession_rate, "%")
print("Concession Amount: Rs.", round(concession, 2))
print("Final Bill: Rs.", round(final_bill, 2))

print("Patient Classification:", classification)

print("--------------------------------")
print("Billing Completed Successfully!")

