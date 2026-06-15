#atm
balance=[5000]
print("1:balance","2:deposit","3:withdrawal")
choice=int(input("enter choice here:"))
if choice==1:
    print(balance[0])
    print("balance succesfully")
elif choice==2:
    deposit=int(input("enter deposit here:"))
    dep_amount=balance[0]+deposit
    balance[0] = dep_amount
    # balance = balance
    print("deposit succesfully")
    print("updated balance=",balance)
elif choice==3:
    withdrawal=int(input("enter withdrawal amount here:"))
    if balance[0]>withdrawal:
        balance=balance[0]-withdrawal
        print("withdrawal succesfully")
    print("remaining balance",balance)
else:
    print("invalid choice")