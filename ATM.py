class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your name has been changed to: ", self.name)

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to: ", self.pin)

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to: ", self.password)
        
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name,pin,password)
        self.balance = 0 
       
    def show_balance(self):
        (float(self.balance))
        print(f"{self.name}'s Current Balance is: $ {self.balance}")

    def withdraw(self):
        take_amt = float(input("Enter the $ amount to withdraw: $ "))
        self.balance =  self.balance - take_amt


    def deposit(self): 
        print(f"Welcome Back, {self.name}!")
        add_amt = float(input("Enter the $ amount to deposit: $ "))
        self.balance =  self.balance + add_amt
        print(f"Succcessfully deposited ${add_amt} to {self.name}'s balance!")
    

    def transfer_money(self, user2):
        print("Please Wait. Attempting to Transfer Money.")
        print("Authentication Required! Please Answer the following questions.")
        userpin =float(input(f"{self.name}, Please enter your pin to continue: "))

        if self.pin != userpin:
            print(self.pin != userpin)
            print("Authentication Failed!")
            return False 
        
        print(f"Congradulations {self.name}, Authentication Successful!")
        transfer_amt = float(input(f"Enter the $ amount to transfer to {user2.name}: $ "))

        user2.balance =  user2.balance + transfer_amt
        self.balance =  self.balance - transfer_amt
        print(f"Succcessfully deposited ${transfer_amt} to {user2.name}'s balance!")

        return True

    def request_money(self,user2):
        print("Please Wait. Attempting to Request Money.")
        print("Authentication Required! Please Answer the following questions.")
        user2_pin = float(input(f"Please enter the pin for {user2.name}: "))

        if user2_pin == user2.pin:
            userpassword = input(f"{self.name}, Enter your password, : ")

            if userpassword == self.password:
                print(f"Congradulations {self.name}, Authentication Successful!")

                req_amt = float(input(f"Enter the $ amount you would like to request from {user2.name}: $ "))
                user2.balance = user2.balance - req_amt
                self.balance =  self.balance + req_amt
                return True
                print(f"Succcessfully requested ${req_amt} from {self.name}'s balance!")

            print("Authentication Failed. Please try again.")
            return False   
        print("Authentication Failed. Please try again.")
        return False 


    """ Driver Code for Task 1 """

# user1 = User("Jane",1234, "janespassword")
# print(user1.name, user1.pin, user1.password)

    """ Driver Code for Task 2 """

# user1 = User("Jane",1234, "janespassword")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Jane Doe")
# user1.change_pin(4321)
# user1.change_password("bestpassword")


""" Driver Code for Task 3"""
# bankuser1 = BankUser("Jane",1234,"bestpassword")
# print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)

""" Driver Code for Task 4"""

# bankuser1 = BankUser("Jane Doe", 4321,"bestpassword")

# bankuser1.show_balance()
# bankuser1.deposit()
# bankuser1.show_balance()
# bankuser1.withdraw()
# bankuser1.show_balance()

""" Driver Code for Task 5"""
bankuser1 = BankUser("Bob Doe", 4321,"bestpassword")
bankuser2 = BankUser("Linda Doe", 1234,"somepassword")

print(bankuser1.name, bankuser1.pin, bankuser1.password)
print(bankuser2.name, bankuser2.pin, bankuser2.password)


bankuser2.deposit()
bankuser1.show_balance()
bankuser2.show_balance()

bankuser2.transfer_money(bankuser1)
bankuser1.show_balance()
bankuser2.show_balance()

bankuser2.request_money(bankuser1)
bankuser1.show_balance()
bankuser2.show_balance()