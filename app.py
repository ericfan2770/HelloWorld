has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:  # Logical AND operator
    print("Eligible for loan (1)")

if has_high_income or has_good_credit:  # Logical OR operator
    print("Eligible for loan (2)")

if has_good_credit and not has_criminal_record:  # Logical NOT operator
    print("Eligible for loan (3)")
