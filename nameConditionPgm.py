name = input("Enter the name: ")
if len(name) < 3:
    print("The name should be atleast 3 chara")
elif len(name) > 10:
    print("Name should be  within 10 charas")
else:
    print("Perfect")