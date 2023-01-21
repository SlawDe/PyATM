from cardHolder import cardHolder

def print_menu():
    print("Please choose from one of the following options: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")
 
def deposit(cardHolder):
    try:
        deposit = float (input("How much money woult you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for you money. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float (input("How much money woult you like to withdraw: "))
        ## Check user balance
        if (cardHolder.get_balance < withdraw):
            print("You don't have enougth money !")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            #print("Your new balance is: ", str(cardHolder.get_balance()))
            print("Thank You !")            
    except:
        print("Invalid input")
    
def check_balance(cardHolder):
    print("Your current balance is: ",cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    ## Create repo list
    list_of_cardholders=[]
    list_of_cardholders.append(cardHolder("1111", 1234, "john1", "English1", 199.0))
    list_of_cardholders.append(cardHolder("1112", 1234, "Stev", "French", 299.0))
    list_of_cardholders.append(cardHolder("1113", 1234, "Mark", "Poland", 399.0))
    list_of_cardholders.append(cardHolder("1114", 1234, "Jimmy", "USA", 499.0))

    ## Promt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input ("Please enter your debit cart: ")
            ### Chaeck again repo
            debitMatch = [holder for holder in list_of_cardholders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0 ):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again")
        except:
            print("Card number not recognized. Please try again")

    ## PIN
    while True:
        try:
            userPin = int(input("Please enter you PIN: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")
        
    ## Print options
    print("Welcome ", current_user.get_firstName()," ", current_user.get_lastName())
    option = 0
    while(True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        #elif(option == 4):
            #break     
        else:
            option = 0

        print("Thank you. Have a nice day.")
