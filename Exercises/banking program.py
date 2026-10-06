
def show_balance(balance):
    print(f"The Balance is: Rs.{balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be Deposited: "))

    if amount < 0:
        print(f"Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))

    if amount > balance:
        print(f"Insufficient amount")
        return 0
    elif amount < 0:
        print(f"Amount must be greater than 0")
        return 0
    else:
        return amount





def main():
    balance = 0
    is_running = True



    while is_running:

        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print(f"This is not a valid choice")


    print(f"Thank You! Have a Nice Day!")


if __name__ == "__main__":
    main()