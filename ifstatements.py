is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price = 1000000
good_credit = False
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: KES{down_payment}")

#Logical operators

has_high_income = False
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for Loan")

if has_high_income or has_good_credit:
    print("Eligible for Loan2")

if has_good_credit and not has_criminal_record:
    print("Eligible for Loan3")

#Comparison operators
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
