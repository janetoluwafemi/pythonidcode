contacts = []

def display_options():
    options = """
    1 >>> create account
    2 >>> remove account
    3 >>> transfer
    4 >>> deposit
    5 >>> check accounts
    6 >>> withdraw
    """
    print(options)
    number = int(input("Enter an option: "))
    match (number):
        case 1:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            phone_number = input("Enter your phone number: ")
            pin = input("Enter your pin: ")
            balance = 0.0
            account_number = phone_number[1:]
            print("your account number is ", account_number)
            contacts.append([first_name, last_name, pin, phone_number, account_number, balance])
            print("Account saved successful")
            display_options()
        case 2:
            phone_number = input("Enter your phone number")
            account_number = phone_number[1:]
            for contact in contacts:
                if account_number:
                    contacts.remove(contact)
                    print(f"{phone_number} has been removed")
            display_options()
        case 3:
            person_account_number = input("Enter person's account number: ")
            name_of_bank = input("Which name of bank are you transfering to: ")
            amount = float(input("Enter the amount you want to transfer: "))
            pin = input("Enter your pin to make transfer")
            for contact in contacts:
                if (person_account_number.__eq__(contact[4])):
                    amount = input(int("Enter the amount you want to deposit: "))
                    pin = input(str("Enter your pin: "))
                    if (amount < 0):
                        contact[5] += amount
                        return amount[5]
            display_options()
        case 4:
            account_number = input("Enter your account number: ")
            amount = float(input("Enter the amount you want to deposit: "))
            pin = input("Enter your pin")
            for contact in contacts:
                if account_number == contact[4] and pin == contact[2]:
                    contact[5] += amount
                    print("successful...")
            display_options()

        case 5:
            for contact in contacts:
                print(f'{contact[0]}, {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]}, {contact[5]}')
            display_options()
        case 6:
            account = input("Enter your account number")
            amount = float(input("Enter the amount you want to redraw: "))
            pin = input("Enter your pin: ")
            for contact in contacts:
                if(account == contact[4] and pin == contact[3]):
                    if(amount >= contact[5]):
                        contact[5] -= amount
                        return contact[5]
                elif(amount < contact[5] and account != contact[4] and pin != account[3]):
                    return "Are you a thief"
            display_options()




display_options()

