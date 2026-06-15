# 1 means withdrawal
# 2 depositbalance
# balance = 1000
# withdraw=2000
# pin=1234
# checkpin=int(input("enter your pin here:"))
# # print(type(choice))
# if choice==1:
# if pin==checkpin:
#     print("pin matched")
#     options = {1:"Withdrwal",2:"Depsoit"}
#     choice=int(input("select your option and enter value:"))

#     if choice==1:
#         print("withdrawl")
#     elif choice == 2:
#         print('Depos')
#     else:
#         print('wrong option selected')

# else:
#     print("pin wrong")
        
# elif choice==2:
#     print("deposit")
# else:
#     print("transaction failed or account nill")
#atm
# balance=[5000]
# print("1:balance","2:deposit","3:withdrawal")
# choice=int(input("enter choice here:"))
# if choice==1:
#     print(balance[0])
#     print("balance succesfully")
# elif choice==2:
#     deposit=int(input("enter deposit here:"))
#     dep_amount=balance[0]+deposit
#     balance[0] = dep_amount
#     # balance = balance
#     print("deposit succesfully")
#     print("updated balance=",balance)
# elif choice==3:
#     withdrawal=int(input("enter withdrawal amount here:"))
#     if balance[0]>withdrawal:
#         balance=balance[0]-withdrawal
#         print("withdrawal succesfully")
#     print("remaining balance",balance)
# else:
#     print("invalid choice")

# s={1,2,3}
# s.add(4)
# print(s)

# s={1,2,3,4}
# s.update([10,20,30,40,50])
# print(s)

# s={1,2,3,4}
# l=tuple(s)
# print(l)

# print(result)
# name={"sameeer,reemas", [1,2]}
# name.set(name)
# print(name)
# # name={"sameer","reemas"}
# name=tuple(name)
# print(name)
# name=[0,20,30,40,{20,30,40,50,}]
# user_input = int(input('give your value only below 100:'))
# print(user_input)
# name[4] = list(name[4])
# if user_input <= 100 and user_input>=1:
#     name[4][1] = user_input
#     name[3]=400
#     name[4] = set(name[4])
#     print(name)
# else:
#     print('only above 100 and zero also not accepts')

#[0,20,30,40,{20,20,40,50,100,200}]
# name=[123,[123]]
# result=name
# print(name)
# name={name:{"123":21}}
# print(name["123"])

# values=[1,2,2,3,3,4,4,5,6]
# # output: {1:1,2:2,3:2,4:2,5:1,6:1}
# count={}
# for ch in values:
#     if ch in count:
#         count[ch]+1
#     else:
#         count[ch]=1
# print(count)
# result=values.count(5)
# print(result)

# for v in values:
#     count[v] = values.count(v)
# print(count)

# dup = []
# for x in values:
#     if x not in dup:
#         dup.append(x)
# for y in dup:
#     count[y] = values.count(y)
# print(count)

# freq = {v: values.count(v) for v in set(values)}
# print(freq)

      ###########smeerpractice
values=[1,2,2,3,3,4,4,5,6]
# output: {1:1,2:2,3:2,4:2,5:1,6:1}
count={}
for v in values:
    count[v]=values.count(v)
print(count)

    