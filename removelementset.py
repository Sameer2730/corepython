a={10,20,30}
a.remove(20)
print(a)
balance = 1000

print("ATM Menu")
print("1. Withdraw")
print("2. Deposit")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful!")
    print("Updated balance:", balance)

else:
    print("Invalid choice!")