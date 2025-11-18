pin = "06061"
balance = 2000
attempts = 3

# Step 1: Login
while attempts > 0:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == pin:
        print("\nAccess Granted!\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempts left.")

if attempts == 0:
    print("Too many incorrect attempts. Card blocked.")
    exit()

# Step 2: ATM Menu
while True:
    print("----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Deposit successful! New balance:", balance)
        except ValueError:
            print("Invalid amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print("Withdrawal successful! New balance:", balance)
        except ValueError:
            print("Invalid amount.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")