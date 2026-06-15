#odd numbers
num=10
for i in range(2,num+1):
    if i%2==0:
        print(i)
#even numbers
num=20
for i in range(1,20):
    if i%2!=0:
        print(i)
#multiplication table
num=5
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#count even digits
# num=1234567891011
# count=0
# for digit in str(num):
#     if int(digit)%2==0:
#         print(digit,end=" ")
# num=123456
# for digit in str(num):
#     if int(digit)%2!=0:
#         print(digit)
# @##################################even
# num=123456
# while num>0:
#     digit=num%10
#     if digit%2==0:
#         print(digit,end=" ")
#     num//=10
# ###################3odd
# num=123456
# while num>0:
#     digit=num%10
#     if digit%2!=0:
#         print(digit,end=" ")
#     num=num//10
num=12345   
product=1
while num>0:
    digit=num%10
    product*=digit
    num=num//10
    print(product)

################################
balance = 1000
withdraw=2000
choice=int(input("enter  your choice here:"))
if choice==1:
    
        print("withdraw ")
elif choice==2:
    print("deposit")
else:
    print("transaction failed or account nill")
