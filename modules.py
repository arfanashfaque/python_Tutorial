
name = input("enter ur name: ")
print("Hi " + name )

weight = int(input("enter the weight: "))
unit = input("Enter the unit L or K :")
if unit.upper() == "L":
    weight_kgs = weight * 0.45
    print(f"your weight in kgs is { weight_kgs}kgs")
elif unit.upper() == "K":
    weight_lbs = int(weight) / 0.45
    print(f"Your weight in Lbs is {weight_lbs} lbs")
