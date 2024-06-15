
# define a func to show the balance
def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

# define a func to deposit (add) to your balance
def deposit():
    print("*********************")
    # local var
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount

# define a func to withdeaw (sub)
def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount

# define a main function
def main():
    # set the balance value and the running con for the program
    balance = 0
    is_running = True

    while is_running:
        # show the user a list of functionalitys
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")

        # ask the user to choose one
        choice = input("Enter your choice (1-4): ")

        # if statment for the chosin func
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            # we add our balance (0) to the balance in the deposit func
            balance += deposit()
        elif choice == '3':
            # we sub our balance from the amount we choosed in the withdraw func
            balance -= withdraw(balance)
        elif choice == '4':
            # braek condition
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

# Good practice (code is modular, helps readability, leaves no global variables, avoids unintended execution)

# Ex. library = Import library for functionality. When running library directly, display a help page
                     
if __name__ == '__main__':
    main()

