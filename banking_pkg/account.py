def show_balance(balance):
    print("Current balance $" + str(balance))
    return balance

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    print("Current balance :$" + str(balance + amount))
    return balance + amount

def withdraw(balance):
    while True:
        withdrawal = float(input("Enter amount to withdraw: "))
        if withdrawal > balance:
            print("You can only withdraw a maximum of $" + str(balance))
        else:
            break
    print("Current balance :$" + str(balance - withdrawal))
    return balance - withdrawal

def logout(name):
    print("Goodbye",name)