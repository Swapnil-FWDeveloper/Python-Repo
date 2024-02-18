balance = 10000  # Default balance

def check_balance():
    print("Your balance is Rs.", balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance is Rs.", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposit successful. Current balance is Rs.", balance)

def exit():
    print("Thank you for using the ATM. Have a nice day!")


def main():
    pin = input("***** Welcome To ATM Machine Simulator *****\nEnter Your Pin: ")
    while True:
        print("\nOptions you can Exercise are:")
        print("1) Balance")
        print("2) Withdraw")
        print("3) Deposit")
        print("4) Exit")
        option = input("\nSelect Your Transaction from the above options: ")
        
        if option == '1':
            check_balance()
        elif option == '2':
            amount = float(input("Enter Amount: "))
            withdraw(amount)
        elif option == '3':
            amount = float(input("Enter Amount: "))
            deposit(amount)
        elif option == '4':
            exit()
            break
        else:
            print("Invalid option. Please select again.")


if __name__ == "__main__":
    main()
