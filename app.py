from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")



while True:
    name = (input("Enter name to register: ")).lower()
    if len(name) > 10:
        print("The maximum lenght is 10 characters")
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) > 4 or len(pin) < 4:
        print("Pin must contain 4 numbers.")
    else:
        break
balance = 0.0
print(name,"has been registered with a balance of $" + str(balance))
while True:
    print("LOGIN")
    login_name = input("Enter name: ")
    login_pin = input("Enter PIN: ")
    if (login_name == name) and (login_pin == pin):
        print("Login successful")
        break
    else:
        print("Invalid credentials")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        balance = account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout(name)
        break