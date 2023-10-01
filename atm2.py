pin=1234
card="canara"
balance=40000
card=input("enter the card name:")
if card=="canara":
    print("""1.withdrawal \n2.balance \n3.deposite""")
    program=input("ENTER THE CHOICE:")
    match program:
        case"withdrawal":
            print("WELCOME TO OUR ATM")
            pin=int(input("enter your pin:"))
            if pin==1234:
                print("your pin is valid")
            else :
                print("invalid pin")
            if pin==1234:
                amount=int(input("ENTER THE AMOUNT:"))
                if(amount<=balance):
                    print("COLLECT YOUR AMOUNT:",amount)
                    print( "BALANCE:",balance-amount)
                    print("THANK YOU")
                else:
                    print("insufficient amount")
            
        case"balance":
            print("your balance",balance)
        case"deposite":
            dep=int(input("enter the amount to deposite:"))
            print("balance",balance+dep)
        
else:
    print("invalid pin")
    print("THANK YOU")
