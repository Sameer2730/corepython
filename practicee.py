for i in range(5):
    print("hello world")
#########1 to n numbers
n=5
for i in range(1,n+1):
    print(i)
# nto 1 numbers 
n=5
for i in range(n,0,-1):
    print(i)
#print even numbers from 1 to n
n=10
for i in range(2,n+1):
    if i%2==0:
        print(i)
# odd numbers
n=10
for i in range(1,n+1):
    if i%2!=0:
        print(i)
#sum of first n numebrs
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
#multiplication table
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)
# factorial of a number
num=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
# count digits in a number
n=12345678
count=0
while n>0:
    count+=1
    n=n//10
print(count)
#reverse a number
n=1234
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
# 11)sum of digits
numbers=1234567
sum=0
while numbers>0:
    digit=numbers%10
    sum+=digit
    numbers=numbers//10
print(sum)
# 12)product of digits
n=1234
product=1
while n>0:
    digit=n%10
    product*=digit
    n=n//10
print(product)
# 13)largest digit 
numbers=[10,20,30,40,50]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print(largest)
# 14) smallest digit 
numbers=[10,20,30,40,50]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print(smallest)
#15)count even digits in a number
numbers=123456
count=0
while numbers>0:
    digit=numbers%10
    if digit%2==0:
        count+=1
    numbers=numbers//10
print(count)
#count odd digits in a number
numbers=12345678
count=0
while numbers>0:
    digit=numbers%10
    if digit%2!=0:
        count+=1
    numbers=numbers//10
print(count)
#count zeroes
numbers=1020304050
count=0
while numbers>0:
    digit=numbers%10
    if digit==0:
        count+=1
    numbers=numbers//10
print(count)
#count multiples of three
n=10
count=0
for i in range(1,n+1):
    if i%3==0:
        count+=1
print(count)
# print squares of a numebrs
n=3
for i in range(1,n+1):
    print(i**3)
# average of numbers 1 to n
n=5
total=0
for i in range(1,n+1):
    total+=i
avg=total/n
print(avg)
#strings based
name="sameer"
result=name[::-1]
print(result)
# palindrome string 
name="sameer"
original=str(name)
reverse=original[::-1]
if original==reverse:
    print("palindrome")
else:
    print("not a palindrome")
# count vowels
name="sameer"
count=0
for ch in name:
    if ch in "aeiou":
        count+=1
print(count)
# count consonents
name="python programming"
count=0
for ch in name:
    if ch not in "aeiou":
        count+=1
print(count)
#count spaces
name="python programming"
count=0
for ch in name:
    if ch==" ":
        count+=1
print(count)
#count words
name="i love python"
words=name.split()
print(len(words))
#count upper case
name="python PROGRAMMING"
count=0
for ch in name:
    if ch.isupper():
        count+=1
print(count)
#count lowercase
name="sameer"
count=0
for ch in name:
    if ch.islower():
        count+=1
print(count)
# count special characters
name="@#$%&"
count=0
for ch in name:
    if not ch.isalnum():
        count+=1
print(count)
#removing duplicates values
name="python programming"
result=""
for ch in name:
    if ch not in result:
        result+=ch
print(result)




#######################################lets  start functions
def greet():
    print("hello")
greet()
greet()
greet()
############# my name
def greet():
    print("sameer")
greet()
############### add two numbers
def add(a,b):
    print(a+b)
add(2,3)
################subtract two numbers
# def sub(a,b):
#     print(a-b)
# sub(3,2)
# ########### multiply two numbers
# def multiply(a,b):
#     print(a*b)
# multiply(2,3)
# #find maximum of trwo numbers
# def max(a,b):
#     if a>b:
#         print(a)
#     if b>a:
#         print(b)
# max(3,2)
# # minimum values
# def minimum(a,b):
#     if a<b:
#         print(a)
#     if b<a:
#         print(b)
# minimum(10,20)
# # check even or odd
# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(3)
# # multiple parametres
# def info(name,age,city,clg,section,identity):
#     print("name=",name)
#     print("age=",age)
#     print("city",city)
#     print("section=",section)
#     print("identity=",identity)
# info("sameer",20,"machilipatnam","sri vasavi institye of technology","CSE-AIML","Indian")
# ##############POSITIONAL ARGUMENTRS
# def add(a,b):
#     print("sum=",a+b)
# add(10,20)
# ######3 student details
# def student_info(name,age,section):
#     print("name=",name)
#     print("age=",age)
#     print("section=",section)
# student_info("sameer",20,"CSE-AIML")
# ########################multiply
# def multiply(a,b):
#     print(a*b)
# multiply(2,10)
# ########################area of rectangle
# def area_rectangle(length,breadth):
#     print("area of rectangle=",length*breadth)
# area_rectangle(10,3)
# #clg information
# def clg_information(name,age,city,id):
#     print("name=",name)
#     print("age=",age)
#     print("city=",city)
#     print("id=",id)
# clg_information("sameer",20,"machilipatnam","23mq1a4248")
# ####### swap values
# def swap_values(a,b):
#     print("a=",b)
#     print("b=",a)
# swap_values(2,3)
# ########### calc
# def calc(a,b):
#     print(a+b)
#     print(a-b)
# calc(3,2)
# ############DEFault PARAMETRES
# def greet(name="guest"):
#     print("name=",name)
# greet("sameer")
# #student age
# def info(name="guest",age=20):
#     print("name=",name)
#     print("age=",age)
# info("sameer",20)
# #city default
# def greet(name,city="machilipatnam"):
#     print("name=",name)
#     print("city=",city)
# greet("sameer")
# # clg
# def clg_info(name="guest",age="nil",section="nil"):
#     print("name=",name)
#     print("age=",age)
#     print("section=",section)
# clg_info("sameer",20,"CSE-AIML")
# ##score
# def greet(score=35):
#     print("score=",score)
# greet(20)
# # login
# def login(user_name="sameer"):
#     print("user_name=",user_name)
# login("praveen")
# ############3key word arguments
# def info(name,age,marks):
#     print("name=",name)
#     print("age=",age)
#     print("marks=",marks)
# info(age=20,marks=30,name="sameer")
# #args
# def add(a,b,c):
#     print(a+b+c)
# add(2,2,2)
# # args using
# def show(*args):
#     print(args)
# show(10,20,30,40,50,60)
# # sum of all values 

# ###############
# def largest(*nums):
#     print(max(nums))
# largest(10,50,70)
# ######
# def maximum(a,b,c):
#     if a>b and a>c:
#         print("maximum",a)
#     if b>a and b>c:
#         print("maximum",b)
#     else:
#         print("maximum",c)
# maximum(30,20,10)
# ##############kwargs
# def info(**data):
#     print(data)
# info(name="sameer",age=20,city="machilipatnam",working="software developer")

# def student(**details):
#     for key,value in details.items():
#         print(key,"=",value)
# student()

# # recurssion
# def hello(n):
#     if n==0:
#         return
#     print("hello")
#     hello(n-1)
# hello(5)

# # print  1 to n 
# def print_num(n):
#     if n==0:
#         return
#     print_num(n-1)
#     print(n)
# print_num(5)
# # reverse
# def reverse(n):
#     if n==0:
#         return
#     print(n)
#     reverse(n-1)
# reverse(5)
# # sum of first n numbers
# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# print(sum(5))
################################################################3333
####################################################3
##############################################
###########################################
###################################333
#################################3333333
# RECCURSSION
# print 1 to n 
def f(n):
    if n==0:
        return
    f(n-1)
    print(n)
f(5)
###### sum_of _digits
def sum_digits(n):
    if n==0:
        return 0
    return(n%10)+sum_digits(n//10)
print(sum_digits(1234656))
#COUNGT DIGITS
def count_digits(n):
    if n==0:
        return 0
    return 1+count_digits(n//10)
print(count_digits(123456789))
# revese number
def reverse(n,rev=0):
    if n==0:
        return rev
    return reverse(n//10,rev*10 +n % 10)
print(reverse(1234))