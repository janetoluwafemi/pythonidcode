contacts = []
def create_account(first_name,last_name,phone_number,pin,account_number, balance):
    balance = 0.0
    first_name = input("Enter your first: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")
    pin = input("Enter your pin: ")
    account_number = phone_number[1:]
    contacts.append([first_name,last_name,phone_number,pin,account_number,balance])
    print("Account created successfully")

def remove_account(account_number):
    phone_number = input("Enter your phone number: ")
    account_number = phone_number[1:]
    for contact in contacts:
        if(phone_number == contacts[2] and account_number == contacts[4]):
            contacts.remove(contacts[0])
            contacts.remove(contacts[1])
            contacts.remove(contacts[2])
            contacts.remove(contacts[3])
            contacts.remove(contacts[4])
            contacts.remove(contacts[5])

def transfer(person_account_number,pin,amount):
    person_account = input("Enter person's account number: ")
    person_name = "Oluwafemi Ifeoluwa"
    print(person_name)
    amount = float(input("Enter the amount you want to transfer: "))
    pin = input("Enter your pin to make the transfer: ")
    for contact in contacts:
        if(pin == contacts[3]):
            contacts[5] -= amount
            print("Amount successful to transfered to" + person_name)

def deposit(account_number,pin,amount):
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin to deposit: ")
    amount = input("Enter the amount you want to deposit: ")
    for contact in contacts:
        if(pin == contacts[3] and account_number == contacts[4]):
            contacts[5] += amount
            return contacts[5]

def check_account():
    for contact in contacts:
        print(contacts[0],contact[1],contact[2],contact[3],contact[4],contact[5])


