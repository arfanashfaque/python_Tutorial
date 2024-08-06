price = 100000
has_good_credit = False
has_medium_credit = False

if has_good_credit:
    downPayment = 0.1 * price
elif has_medium_credit:
    downPayment = 0.2 * price
else:
    downPayment = 0.25 * price

print(f"DownPayment = ${downPayment}")
print("Price of house : $" + str(price))
print(f"Price of the house with credit :${ price + downPayment}")
