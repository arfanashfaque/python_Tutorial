from openpyxl.chart import layout

print("Welcome to XYZ BANK")
restart = 'Y'
chances = 3
balance = 12556.58
try :
 while chances >= 0:
     pin = int(input("Enter Your PIN: "))
    if pin == 1234:
        print("Welcome \n")
        while restart not in ("n","N","No","NO"):
            print("Press 1 for Balance Enquiry\n")
            print("Press 2 for Cash Widthdraw\n")
            print("Press 1 for To Pay\n")
            print("Press 1 for Remove Card\n")
            opt = int(input("choose\n"))
            if opt == 1:
                print("Your Account Balance is : ",balance,"Rs\n")
                if restart in ("n","N","No","NO"):
                    print("Thank You\n")
                    break
            elif opt==2:
                opt2 = 'y'
                withdraw = float(input("How much like to withdraw:\n"))
                if withdraw in [100,200,500,2000]:
                    balance = balance - withdraw
                    print("Your Balance now is:",balance,"Rs\n")
                    restart = input("Would you like to go back?\n")
                    if restart in ("n","N","No","NO"):
                        print("Thank You\n")
                        break
            else:
                print("Enter correct number\n")
        expect: NameError
        print("Error!!!")
        restart = 'Y'
    elif pin != 1234 :
        print("Incorrect PIN\n")
        chances = chances - 1
        if chances == 0:
            print("\n Sorry you have reached max number of attempts")
            break






