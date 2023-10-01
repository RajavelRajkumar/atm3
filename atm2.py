atm="1234"
card="canara"
balance=40000
atm=input("enter the pin:")
if atm=="1234":
    program=input("ENTER THE CHOICE:")
    match program:
        case"withdrawal":
            print("WELCOME TO OUR ATM")
            print("insert your card")
            card=input("enter your card name:")
            if card=="canara":
                print("your card is valid")
            else :
                card!="canara"
                print("invalid card")
            if card=="canara":
                amount=int(input("ENTER THE AMOUNT:"))
                print("COLLECT YOUR AMOUNT:",amount)
                print( "BALANCE:",balance-amount)
                print("THANK YOU")
        case"balance":
            print("your balance",balance)
        case"deposite":
            dep=int(input("enter the amount to deposite:"))
            print("balance",balance+dep)
        
else:
    print("invalid pin")
    print("THANK YOU")
