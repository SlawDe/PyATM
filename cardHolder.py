class cardHolder():
    def __init__(self, cardNum, pin, firstName, lastName, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance

    ### Getter methods
    def get_cardNumber(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_balance(self):
        return self.balance

    ### Getter methods
    def set_cardNum(self,newVal1):
        self.cardNum = newVal1
    def set_pin(self,newVal1):
        self.pin = newVal1
    def set_firstName(self,newVal1):
        self.firstName = newVal1
    def set_lastName(self,newVal1):
        self.lastName = newVal1
    def set_balance(self,newVal1):
        self.balance = newVal1

    def print_out(self):
        print("Card #: ", self.cardNum)
        print("PIN #: ", self.pin)
        print("First Name #: ", self.firstName)
        print("Last Name #: ", self.lastName)
        print("Balance #: ", self.balance)