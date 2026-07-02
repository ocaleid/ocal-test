balance = 1000

while True:
    print(20*"*")
    print("1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit\n")
    choice = int(input("Enter your choice: "))
    print(20*"*")

    if choice == 1:
        print("Your balance is: ", balance)
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
    elif choice == 4:
        print("Thank you!")
        break
    else:   
        print("wrong choice, try again")