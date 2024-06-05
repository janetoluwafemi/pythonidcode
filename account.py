class accounts:
    def __init__(self,first_name,last_name,phone_number,account_number,pin,balance):
        self.account_balance = balance
        self.firstname = first_name
        self.lastname = last_name
        self.number = phone_number
        self.accountnumber = account_number
        self.pin = pin

    my_account = accounts("Jan")
    def create_account(self):
        balance = 0.0
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        phone_number = input("Enter your phone number: ")
        account_number = phone_number[1:]
        pin = input("Enter your pin: ")
        print("Account created successfully")

    def deposit(self):
        account_number = input("Enter person account number: ")
        amount = float(input("Enter the amount you want to deposit"))
        pin = input("Enter your pin: ")
        for account in accounts:
            if(account_number == accounts and pin == accounts):
                account_balance += amount












