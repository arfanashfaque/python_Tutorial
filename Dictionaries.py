customer = {
    "name" : "Arfan Ashfaque",
    "age" : 29,
    "is_verified" : True
}
print(customer["name"]) #output: Arfan Ashfaque
print(customer.get("birthdate"))  #output : none
#print(customer["birthdate"]) will give error
print(customer.get("birthdate","Aug 12 1994")) # this will update the birthdate