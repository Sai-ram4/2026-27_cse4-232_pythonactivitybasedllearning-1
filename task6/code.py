


print("===== ATM TRANSACTION SYSTEM =====")


balance = float(input("Enter Initial Balance: Rs. "))

if balance < 0:
    print("Invalid Initial Balance!")
    exit()


withdrawal_limit = 10000
n = int(input("Enter Number of Transactions: "))

if n <= 0:
    print("Invalid Number of Transactions!")
    exit()


total_deposits = 0
total_withdrawals = 0
rejected_transactions = 0


transactions = []

for i in range(n):

    print("\nTransaction", i + 1)

    transaction_type = input(
        "Enter Transaction Type (deposit/withdraw): "
    ).strip().lower()

    amount = float(input("Enter Amount: Rs. "))

    
    if amount <= 0:

        print("Transaction Rejected: Invalid Amount!")

        rejected_transactions += 1

        transactions.append(
            [transaction_type, amount, "Rejected"]
        )

    
    elif transaction_type == "deposit":

        balance += amount
        total_deposits += amount

        print("Deposit Successful!")
        print("Current Balance: Rs.", round(balance, 2))

        transactions.append(
            [transaction_type, amount, "Successful"]
        )

    
    elif transaction_type == "withdraw":

        if amount > withdrawal_limit:

            print("Transaction Rejected: Withdrawal Limit Exceeded!")

            rejected_transactions += 1

            transactions.append(
                [transaction_type, amount, "Rejected"]
            )

        elif amount > balance:

            print("Transaction Rejected: Insufficient Balance!")

            rejected_transactions += 1

            transactions.append(
                [transaction_type, amount, "Rejected"]
            )

        else:

            balance -= amount
            total_withdrawals += amount

            print("Withdrawal Successful!")
            print("Current Balance: Rs.", round(balance, 2))

            transactions.append(
                [transaction_type, amount, "Successful"]
            )

    else:

        print("Transaction Rejected: Invalid Transaction Type!")

        rejected_transactions += 1

        transactions.append(
            [transaction_type, amount, "Rejected"]
        )



print("\n===== TRANSACTION HISTORY =====")

for i, transaction in enumerate(transactions, start=1):

    print(
        i,
        transaction[0].capitalize(),
        "Rs.", transaction[1],
        "-",
        transaction[2]
    )



print("\n===== ATM TRANSACTION SUMMARY =====")

print("Total Deposits: Rs.", round(total_deposits, 2))

print("Total Withdrawals: Rs.",
      round(total_withdrawals, 2))

print("Rejected Transactions:", rejected_transactions)

print("Final Account Balance: Rs.",
      round(balance, 2))

print("\nATM Transaction Process Completed!")

