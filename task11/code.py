

branches = {
    "CS": "Computer Science",
    "EC": "Electronics",
    "ME": "Mechanical",
    "CE": "Civil",
    "EE": "Electrical"
}

valid_records = []
invalid_records = []

print("===== CAMPUS REGISTRATION ID ANALYZER =====")

try:
    n = int(input("Enter number of student records: "))

    if n <= 0:
        raise ValueError("Number of records must be positive.")

    for i in range(n):

        print("\nStudent Record", i + 1)

        student_id = input("Enter registration ID: ").strip().upper()

        
        if len(student_id) != 7:
            invalid_records.append(
                (student_id, "ID must contain exactly 7 characters")
            )
            continue

        
        year_code = student_id[0:2]
        branch_code = student_id[2:4]
        sequence = student_id[4:7]

        
        if not year_code.isdigit():
            invalid_records.append(
                (student_id, "Invalid admission year")
            )
            continue

        
        if branch_code not in branches:
            invalid_records.append(
                (student_id, "Invalid branch code")
            )
            continue

        
        if not sequence.isdigit() or sequence == "000":
            invalid_records.append(
                (student_id, "Invalid student sequence number")
            )
            continue

        
        admission_year = 2000 + int(year_code)

        
        record = {
            "id": student_id,
            "year": admission_year,
            "branch": branches[branch_code],
            "branch_code": branch_code,
            "sequence": sequence
        }

        valid_records.append(record)

    
    print("\n===== VALID STUDENT RECORDS =====")

    for record in valid_records:
        print("Registration ID:", record["id"])
        print("Admission Year:", record["year"])
        print("Branch:", record["branch"])
        print("Sequence Number:", record["sequence"])
        print("------------------------------")

    
    print("\n===== INVALID STUDENT RECORDS =====")

    if invalid_records:
        for student_id, reason in invalid_records:
            print(student_id, "-", reason)
    else:
        print("No invalid records found.")

    
    print("\n===== BRANCH-WISE SUMMARY =====")

    for code, name in branches.items():
        count = sum(
            1 for record in valid_records
            if record["branch_code"] == code
        )
        print(name, ":", count)

    
    print("\n===== YEAR-WISE SUMMARY =====")

    years = sorted(set(
        record["year"] for record in valid_records
    ))

    for year in years:
        count = sum(
            1 for record in valid_records
            if record["year"] == year
        )
        print(year, ":", count)
    print("\n===== FINAL SUMMARY =====")
    print("Total Records:", n)
    print("Valid Records:", len(valid_records))
    print("Invalid Records:", len(invalid_records))

except ValueError as error:
    print("Input Error:", error)
