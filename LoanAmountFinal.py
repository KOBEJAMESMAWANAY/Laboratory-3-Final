def Laboratory_3_Loan_Amount():
    salary = float(input("Please enter your monthly salary: "))
    loan_amount = float(input("Please enter the loan amount you want to request: "))

    if salary >= 30000.00:
        max_loan_amount = salary * 10
        if loan_amount <= max_loan_amount:
            print("Congratulations! You are eligible for the loan.")
            months_to_pay = int(input("How many months do you want to pay the loan? "))
            interest = loan_amount * 10
            total_amount = loan_amount + interest
            print(f"Total amount to be paid: {total_amount:.2f}")
            print(f"Monthly payment over the {months_to_pay} months: {total_amount / months_to_pay:.2f}")
        else:
            print("Your loan request is too high. Please enter an amount maximum to:", max_loan_amount)
    else:
        print("Unfortunately, your salary is too low. You need at least a monthly salary of 30000.00.")

Laboratory_3_Loan_Amount()
