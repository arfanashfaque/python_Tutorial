try :
    age = int(input("Enter the age:" ))
    income = 20000
    risk = income / age
    print(risk)
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid message")