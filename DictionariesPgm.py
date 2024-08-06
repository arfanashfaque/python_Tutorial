print("Welcome on board!!")
phone = input("enter the phone number: ")
number = {
    "1": "one",
    "2": "two",
    "3":"three",
    "4":"four",
    "5": "five"
}
output = ""
for ch in phone:
    output += number.get(ch , "!")  + " "# ! means any number other than 5 will give !
print(output)
# here the i/p is given as 123456789 and the output is 12345!!!!