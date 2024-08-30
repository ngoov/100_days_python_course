total = float(input("What is the total bill amount? $"))
tip = int(input("How much tip to give? 10,12 or 15%? "))
people_amount = int(input("Split into how many people? "))

pay_each = round(total / people_amount * (tip / 100 + 1), 2)

print(f"Each have to pay: ${pay_each}")