# print odd nos
for i in range(11):
    if i % 2!=0:
        print(i)
#########################
for i in range(0,11,2):
    print(i)
    ################################################################
total=0
for i in range(1,6):
    total+=i
    print(total)
    ############################3333333
num=2
for i in range(11):
    print(num, "*", i, "=", num*i)
    #########################33333
i=5
while i>=1:
    print(i)
    i-=1
#################################333
i=1
total=0
while i<=5:
    total+=i
    i+=1
    print(total)
##############################3
#nested for loop
for i in range(3):
    for j in range(3):
        print("*", end="  ")
    print()
##############################
#right triangle pattern
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
########################3333
#number triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(i)
#break
for i in range(1,11):
    if i==6:
        break
    print(i)
#continue
for i in range(1,11):
    if i==4:
        continue
    print(i)
#prime number logic
num=2
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==num:
    print("number is a prime number")
else:
    print("not a prime number")
########### PATTERNS 
for i in range(4):
    for j in range(4):
        print("#", end=" ")
    print(i)
#right angle triangle
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print(i)
# number triangle
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
# reverse triangle
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("##########################################################################")
print("##########################################################################")

print("##########################################################################")
print("##########################################################################")
print("##########################################################################")
# #loopss  
# num=6
# for i in range(1,num+1):
#     print(i)

# print("##########################################################################")

# #2)print even no s from 1 tro 100
# for i in range(2,101):
#     if i%2==0:
#         print(i)

# print("##########################################################################")
# #3)print odd numbers
# for i in range(1,100):
#     if i %2!=0:
#         print(i)

# print("##########################################################################")
# #4)MULTIPLICATION TRABLE OF A NUMBER
# num=5
# for i in range(1,11):
#     print(num,"x",i, "=",num*i)

# print("##########################################################################")

# #5)find sum of first n numbers
# num=5
# sum=0
# for i in range(1,num+1):
#     sum+=i
#     print(sum)

# print("##########################################################################")
# #5)FIND FACTORIAL OF A NUMBER
# n=5
# fact=1
# for i in range(1,num+1):
#     fact*=i
#     print(fact)

# print("##########################################################################")
# #6)find reverse of a number
# num=1234
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print("total=",rev)

# print("##########################################################################")
# #7)count digits in a number
# number=12345
# count=0
# while number>0:
#     count+=1
#     number=number//10
# print(count)

# print("##########################################################################")
# #8)find sum of digits
# number=12345
# total=0
# while number>0:
#     digit=number%10
#     total+=digit
#     number=number//10
# print(total)
    
# print("##########################################################################")
# #9)PRINT FIBONACCI SERIES
# n=10
# a=0
# b=1
# for i in range(n):
#     print(a, end=" ")
#     c=a+b
#     a=b
#     b=c



# print("######################################################")
# # 10)prime nos from 1 to n
# number=10
# for num in range(2,number+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#         else:
#             print(num)

# print("######################################################")
# #11)find largest element in a list
# numbers=[10,25,8,45,32]
# largest=numbers[0]
# for i in numbers:
#     if i >largest:
#         largest=i
# print(largest)

# print("######################################################")
# #12)find smallest element in a list
# numbers=[10,20,30,40,50]
# smallest=numbers[0]
# for i in numbers:
#     if i<smallest:
#         smallest=i
# print(smallest)

# print("######################################################")
# #13)PRINT PATTERNS OF STARS TRIANGLE
# n=5
# for i in range(1,n+1):
#     print("*" * i)

# print("######################################################")
# # 14)print inverted star pattern
# n=5
# for i in range(n,0,-1):
#     print("*"*i)

# print("######################################################")
# #15)PRINT NUMBR POPATTERN FROM 1 12 123
# n=3
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# print("######################################################")

# # 16)sum of even numbers upto  n
# n=10
# sum=0
# for i in range(2,n+1,2):
#         sum+=i
# print(sum)

# print("######################################################")
# #17)sum of odd numbers
# n=10
# for i in range(1,n+1,2):
#     sum+=i
# print(sum)

# print("######################################################")
# #!8)count number of even digits in anumber
# # 19)count number of odd digits in number
# n=24879
# count=0
# while n>0:
#     digit =n%10
#     if digit %2==0:
#         count+=1
#     n=n//10
# print(count)

# print("######################################################")
# n=123456789
# count=0
# while n>0:
#     digit=n%10
#     if digit %2!=0:
#         count+=1
#     n=n//10
# print(count)

# print("######################################################")
# # 20)squares of numbers from 1 to n
# n=5
# for i in range(1,n+1):
#     print(i*i)

# print("######################################################")

# #21)#print cubes of numbers from 1to n
# num=3
# for i in range(1,num+1):
#     print(i,"cube is=",i*i*i)

# print("######################################################")
# #22)FIND PRODUCT OF DIGITS OF NUMBER
# n=234
# product=1
# while n>0:
#     digit=n%10
#     product=product*digit
#     n=n//10
# print(product)
# #23 REVERSE A STRING USING LOOP
# name="sameer"
# reverse=name[::-1]
# print(reverse)
# #24)PRINT MULTIPLICATION TABLE OF 10 NUMBERS
# number=10
# for i in range(1,number+1):
#     print(number,"x",i,"=",number*i)
# #25)check wheater a number is palindrome or not
# number=2002
# original=str(num)
# reverse=original[::-1]
# if original==reverse:
#     print("palindrome number")
# else:
#     print("not a palindrome number")


# print("######################################################")
# numbers=[10,20,30,40,50]
# largest=numbers[0]
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)
n=10
for i in range(1,n+1):
    print(i)
# print even numbers from1  to 100
n=100
for i in range(1,n+1):
    if i %2==0:
        print(i)
###33 numbers from 1 to 100
# numbers=100
# for i in range(1,numbers+1):
#     print(i)
# ########### multipkic  of number
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)
#sum of first n numbers
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
###################3
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
#reverse a number
number=4321
rev=0
while number>0:
    digit=number%10
    rev=rev*10+digit
    number//=10
print(rev)
######count digits in a number
number=12345
count=0
while number>0:
    digit=number%10
    count+=1
    number=number//10
print(count)
#sum of digits
numbers=12345
sum=0
while numbers>0:
    digit=numbers%10
    sum+=digit
    numbers=numbers//10
print(sum)
#### prime numbers
number=11
count=0
for i in range(1,number+1):
    if number%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")
###########largest element in a list
numbers=[10,20,30,40,50]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print(largest)
#############3 smallest
numbers=[10,20,30,40,50]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print(smallest)
################ star triangle
n=5
for i in range(1,n+1):
    print("*"*i)

########33 inverted
n=5
for i in range(5,0,-1):
    print("@"*i)
############3 number patterb
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
######3 sum of even numbers upton
n=10
sum=0
for i in range(2,n+1,2):
    sum+=i
print(sum)
########## odd numbers upto n
n=10
sum=0
for i in range(1,n+1,2):
    sum+=i
print(sum)
########### count even difgits in a number
number=123456
count=0
while number>0:
    digit=number%10
    if digit%2==0:
        count+=1
    number=number//10
print(count)
####### count odd digits in a numbre
number=123456
count=0
while number>0:
    digit=number%10
    if digit%2!=0:
        count+=1
    number=number//10
print(count)
#######3squares from 1 to n
n=5
for i in range(1,n+1):
    print(i*i,end=" ")
#########cubes from 1 to n
n=5
for i in range(1,n+1):
    print(i**3,end=" ")
# product
numbers=123
product=1
while numbers>1:
    digit=numbers%10
    product*=digit
    numbers=numbers//10
print(product)
########## reverse a string using loop
name="sameer"
rev=""
for ch in name:
    rev=ch+rev
print(rev)

number=4
count=0
for i in range(1,number+1):
    digit=number%10
    if digit%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")
number=5005
temp=number
rev=0
while number>0:
    digit=number%10
    rev=rev*10+digit
    number=number//10
# if temp==rev:
#     print("palindrome")
# else:
#     print("not a palindrom")
ch="e"
count=0
if ch in "aeiou":
    count+=1
print(count)

def add(a,b):
    print(a+b)
add(2,3)
def user_name():
    print("sameer")
user_name()
##############
# empty functions
def function_name():
    pass
print("python programming")

###########################3
def show():
    print("python")
show()
######################333
def square(n):
    print(n*n)
square(2)
##############3
def demo():
    pass
    ##################
def greet(name):
    print("sameer")
greet(name)
#############
def add(a,b):
    print(a+b)
add(10,20)
###############3
def name(name,age):
    print(name,age)
name(20,"sameer")
#######33 keyword parametres
def key_word(name,age):
    print(name,age)
key_word(age=21,name="sameer")
# default parametres
def greet(name="guest"):
    print(name)
greet()
greet("sameer")
# variable length parametres args 
def numbers(*num):
    print(num)
numbers(10,20,30)
#####################
# $##################################

def add(a,b):
    print(a+b)
add(1,20)

####args
def total(*num):
    print(sum(num))
total(1,2,3,4,5)