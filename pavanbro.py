<<<<<<< HEAD
# marks=28
# if marks<=25:
#     print("student passed exam")
# else:
#     print("student failed exam")
# ###########3
# print('##################################################################################')
# # number=int(input("enter number here:"))
# # if number%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5")
# print('##################################################################################')
# age=16
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# print('##################################################################################')
# a=5
# b=6
# c=7
# if a<b and 
# =5
# b=6
# c=7
# if a>b:
#     print("a is amaller")
# elif b>c:
#     print("b is smaller")
# elif a<b:
#     print("a is smaller")
# =5
# b=6
# c=7
# if a>b:
#     print("a is amaller")
# elif b>c:
#     print("b is smaller")
# elif a<b:
#     print("a is smaller")
# print('#####################################################')
# #login system
# username=input("enter username here:")
# password=input("enter password here:")
# if username=="sameer123" and password=="pandu2730":
#     print("login succesfull")
# else:
#     print("login unsuccesfull")      
##########################
#checkb wheather one number is greater than another
# REVERSE A NUMBER
# number=1234
# original=str(number)
# reverse=original[::-1]
# print(reverse)
#PRIME Number
# num=int(input("enter a number:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
# if count==2:
#         print("its a prime no")
# else:
#         print("its not a prime no")
#palindrome factorial
# num=2002
# original=str(num)
# reverse=original[::-1]
# if original==reverse:
#     print("palindrome")
# else:
#     print("its not a palindrome")
#factoriAL
# number=5
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
# print("factorial=",fact)
#print numbers frok 1 to n
n=5
for i in range(1,n+1):
    print(i)
#print numbers from nto i
number=5
for i in range(number,0,-1):
    print(i)
# even numbers from 1 to n
n=6
for i in range(1,n+1):
    if i %2==0:
        print(i)
# print odd  numbers from 1 to n
number=6
for i in range(1,n+1):
    if i%2!=0:
        print(i)
# sum of first n numberw
numbers=6
sum=0
for i in range(1,numbers+1):
    sum+=i
print(sum)
# sum of even n umbers
numbers=10
sum=0
for i in range(1,numbers+1):
    if i%2==0:
        sum+=i
print(sum)
#sum of odd numbers
numbers=6
sum=0
for i in range(1,numbers+1):
    if i%2!=0:
        sum+=i
print(sum)
# multiplicaation table
number=5
for i in range(1,11):
    print(number,"x",i,"=",number*i)
#squares from 1 to n
n=3
for i in range(1,n+1):
    print(i*i,end=" ")
#cubes from 1 to n
n=3
for i in range(1,n+1):
    print(i**3,end=" ")
###############################################################
#factorial
number=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
#count digits
number=12345
count=0
while number>0:
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
#product of digits
numbers=12345
product=1
while numbers>0:
    digit=numbers%10
    product=product*digit
    numbers=numbers//10
print(product)
#reverse a number
numbers=1234
rev=0
while numbers>0:
    digit=numbers%10
    rev=rev*10+digit
    numbers=numbers//10
print(rev)
#fibonacci series
n=10
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    a,b=b,a+b
# prime numbers 
# largest element in list 
numbers=[10,20,30,40,50]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("largest value in list is",largest)
#smallest element in a list
smallest=[10,20,30,40,50]
smallest=numbers[0]
for i in numbers:
    if i <smallest:
        smallest=i
print("smallest numbers is ",smallest)
######3 star triangle
n=5
for i in range(1,n+1):
    print("*"*i)
#inverted star pattern
n=5
for i in range(n,0,-1):
    print("*"*i)
#number pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#count even numbers
num=123456
count=0
while num>0:
    digit=num%10
    if digit%2==0:
        count+=1
    num=num//10
print(count)
# count odd digits
numbers=123456
count=0
while numbers>0:
    digit=numbers%10
    if digit%2!=0:
        count+=1
    numbers=numbers//10
print(count)
###reverse a string
name="sameer"
rev=""
for ch in name:
    rev=ch+rev
print(rev)
#count vowels
name="sameer"
count=0
for ch in name:
    if ch in "aeiou":
        count+=1
        print(count)
#count consonents
name="sameer"
count=0
for ch in name:
    if ch not in "aeiou":
        count+=1
        print(count)
# count spaces
name="python prograamming"
count=0
for ch in name:
    if ch ==" ":
        count+=1
        print(count)
#count characters
name="sameer"
count=0
for ch in name:
    count+=1
    print(count,end=" ")
    ########################################################3
############################################

#print your name
def your_name():
    return "sameer"
print(your_name())
##########################
# add two numbers
def add(a,b):
    return a+b
add(10,20)
#square of a njumber
def square_of_number(n):
    return n*n
print(square_of_number(3))
# remainder of 2 numbers 
def remainder(a,b):
    return a%b
print(remainder(3,4))
#check even or odd
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(7))
#largest of two numbers
def largest(a,b):
    return max(a,b)
print(largest(10,220))
#smallest of two numbers
def smallest(a,b):
    return min(a,b)
print(smallest(10,220))
#simple imtrest
def simple_intrest(p,r,t):
    return (p*r*t)/100
print(simple_intrest(1000,5,2))
#area of rectangle
def area_of_rectangle(length,breadth):
    return length*breadth
print(area_of_rectangle(5,2))
#perimeter of rectangle
def perimeter(length,width):
    return 2*(length+width)
print(area_of_rectangle(4,2))
#area of circle
def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(2))
# print numbers from 1 to n
def print_numbers(n):
    result=[]
    for i in range(1,n+1):
        result.append(i)
    return result
print(print_numbers(3))
#print even numbers from 1 to n 
def even_numbers(n):
    result=[]
    for i in range(1,n+1):
        if i%2==0:
            result.append(i)
    return result
print(even_numbers(10))
#print 0dd numbers
def odd_numbers(n):
    result=[]
    for i in range(1,n+1):
        if i%2!=0:
            result.append(i)
    return result
print(odd_numbers(10))
# sum of first n numbers 
def sum_of_first_n_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
print(sum_of_first_n_numbers(5))
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))
#count digits in a number
def count_digits(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print(count_digits(12345))
#reverse a number
def reverse_number(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
print(reverse_number(1234))
#sum of digits
def sum_of_digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
print(sum_of_digits(12345))
#palindrome
def palindrome(n):
    rev=0
    temp=n
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return temp==rev
print(palindrome(2002))
#leap year
def leap(year):
    return year%4==0
print(leap(2024))
# maximun of three nu b
def largest(a,b,c):
    return max(a,b,c)
print(largest(10,20,30))
# table numbers
def table(n):
    result=[]
    for i in range(1,11):
        result.append(n*i)
    return result
print(table(10))
#find largest digit
def largest(number):
    max=0
    while number>0:
        digit=number%10
        if digit>max:
            max=digit
        number=number//10
    return max
print(largest(12345678913))
#find smallest digit
def smallest(n):
    min=9
    while n>0:
        digit=n%10
        if digit<min:
            min=digit
        n=n//10
    return min
print(smallest(5345))
###########3prime no
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2
print(prime(7))
###############################################################################3
##############################################################################
###########################################################################3
###############################################################################33
##########################################################################################3
#########################################################################################33
    # INTERMEDIATE PROBLEMS STARTED 
#palindrome mber
def palindrome(n):
    original=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return original==rev
print(palindrome(2002))

# prime number
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "prime number"
    else:
        return "not a prime number"
print(prime(5))
#check prime numbers from 1 to n
def check_prime(n):
    result=[]
    for num in range(2,n+1):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            result.append(i)
    return result
print(check_prime(15))
#fibonacci series
def fibonacci(n):
    a=0
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        c=a+b
        a=b
        b=c
    return result
print(fibonacci(7))
#COUNT VOWELS IN A STRING
def count_vowels(name):
    count=0
    for i in name:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels("sameer"))
# count consonents
def count_consonents(name):
    count=0
    for i in name:
        if i not in "aeiouAEIOU":
            count+=1
    return count
print(count_consonents("python"))
#reverse a string
def reverse_string(name):
    rev=""
    for ch in name:
        rev=ch+rev
    return rev
print(reverse_string("sameer"))
#palindrome string
def palindrome_string(name):
    original=str(name)
    reverse=original[::-1]
    if original==reverse:
        return "palindrome"
    else:
        return "not a palindrome"
print(palindrome_string("sameer"))
#count letters
def count_words(name):
    count=0
    for ch in name:
        count+=1
    return count
print(count_words("sameer"))
#count words
def count_words(name):
    words=name.split()
    return len(words)
print(count_words("i love python programming lannguage"))
#largest words
def biggest(*num):
    print(max(num))
biggest(10,20,30,40,50)

def count(*nums):
    print(len(nums))
count(1,2,3,4,5,6,7,8)
####################
def even_sum(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
            print(sum)
even_sum(10)
###########3
def odd_num(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    print(sum)
odd_num(10)

#############
def clg(*sections):
    print(sections)
clg("cse","ece","mech","civil")
# kwargs
def students(**data):
    print(data)
students(name="sameer",age=21,city="machilipatnam")

#####posiy=tional arguments
def order(item,quantity):
    print(item,quantity)
order("burger",2)
##########keyword argumennnnnts
def order(item,quantity):
    print(item,quantity)
order(quantity=2,item="Burger")
#reccursive function
def fact(n):
    if n==0 and n==1:
        return 1
    return n*fact(n-1)


#####################################33
##################################333
# OOPS CONCEPTS ON CLASS AND OBJECT 
class student:
    name="sameeer"
    age=20
print("name=",student.name)
print("age=",student.age)
# 2)object creation
class student:
    name="sameer"
    age=20
s1=student()
print(s1.name)
print(s1.age)
##3OBJECT OVERRIDE IMPORTANT
class student:
    name="sameer"
    age=20
s1=student()
s2=student()
s1.name="ali"
print(s1.name)
print(s2.name)
#####class and objectrt
class car:
    pass
###############
class car:
    pass
c1=car()
print(c1)
###########3 add variables inside class
class car:
    brand="BMW"
    brand="AUDI"
c2=car()
c1=car()
print(c2.brand)
#add simple value
class car:
    brand="bmw"
c1=car()
print(c1.brand)
#easy function inside class
class car:
    def show(self):
        print("hello car")
c1=car()
c1.show()
# usingh constructor in it
class car:
    def init(self,brand):
        self.brand=brand
c1=car()
print(c1.brand)
# functiom inside class:
class car:
    def init(self,brand):
        self.brand=brand
    def show(self):
        print(self.brand)
c1=car()
c1.show()



#########################333
nums=12345
rev=""
for ch in nums:
    if ch in rev:
        rev=ch+rev
print(rev)
=======
# marks=28
# if marks<=25:
#     print("student passed exam")
# else:
#     print("student failed exam")
# ###########3
# print('##################################################################################')
# # number=int(input("enter number here:"))
# # if number%5==0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5")
# print('##################################################################################')
# age=16
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# print('##################################################################################')
# a=5
# b=6
# c=7
# if a<b and 
# =5
# b=6
# c=7
# if a>b:
#     print("a is amaller")
# elif b>c:
#     print("b is smaller")
# elif a<b:
#     print("a is smaller")
# =5
# b=6
# c=7
# if a>b:
#     print("a is amaller")
# elif b>c:
#     print("b is smaller")
# elif a<b:
#     print("a is smaller")
# print('#####################################################')
# #login system
# username=input("enter username here:")
# password=input("enter password here:")
# if username=="sameer123" and password=="pandu2730":
#     print("login succesfull")
# else:
#     print("login unsuccesfull")      
##########################
#checkb wheather one number is greater than another
# REVERSE A NUMBER
# number=1234
# original=str(number)
# reverse=original[::-1]
# print(reverse)
#PRIME Number
# num=int(input("enter a number:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
# if count==2:
#         print("its a prime no")
# else:
#         print("its not a prime no")
#palindrome factorial
# num=2002
# original=str(num)
# reverse=original[::-1]
# if original==reverse:
#     print("palindrome")
# else:
#     print("its not a palindrome")
#factoriAL
# number=5
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
# print("factorial=",fact)
#print numbers frok 1 to n
n=5
for i in range(1,n+1):
    print(i)
#print numbers from nto i
number=5
for i in range(number,0,-1):
    print(i)
# even numbers from 1 to n
n=6
for i in range(1,n+1):
    if i %2==0:
        print(i)
# print odd  numbers from 1 to n
number=6
for i in range(1,n+1):
    if i%2!=0:
        print(i)
# sum of first n numberw
numbers=6
sum=0
for i in range(1,numbers+1):
    sum+=i
print(sum)
# sum of even n umbers
numbers=10
sum=0
for i in range(1,numbers+1):
    if i%2==0:
        sum+=i
print(sum)
#sum of odd numbers
numbers=6
sum=0
for i in range(1,numbers+1):
    if i%2!=0:
        sum+=i
print(sum)
# multiplicaation table
number=5
for i in range(1,11):
    print(number,"x",i,"=",number*i)
#squares from 1 to n
n=3
for i in range(1,n+1):
    print(i*i,end=" ")
#cubes from 1 to n
n=3
for i in range(1,n+1):
    print(i**3,end=" ")
###############################################################
#factorial
number=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
#count digits
number=12345
count=0
while number>0:
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
#product of digits
numbers=12345
product=1
while numbers>0:
    digit=numbers%10
    product=product*digit
    numbers=numbers//10
print(product)
#reverse a number
numbers=1234
rev=0
while numbers>0:
    digit=numbers%10
    rev=rev*10+digit
    numbers=numbers//10
print(rev)
#fibonacci series
n=10
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    a,b=b,a+b
# prime numbers 
# largest element in list 
numbers=[10,20,30,40,50]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("largest value in list is",largest)
#smallest element in a list
smallest=[10,20,30,40,50]
smallest=numbers[0]
for i in numbers:
    if i <smallest:
        smallest=i
print("smallest numbers is ",smallest)
######3 star triangle
n=5
for i in range(1,n+1):
    print("*"*i)
#inverted star pattern
n=5
for i in range(n,0,-1):
    print("*"*i)
#number pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#count even numbers
num=123456
count=0
while num>0:
    digit=num%10
    if digit%2==0:
        count+=1
    num=num//10
print(count)
# count odd digits
numbers=123456
count=0
while numbers>0:
    digit=numbers%10
    if digit%2!=0:
        count+=1
    numbers=numbers//10
print(count)
###reverse a string
name="sameer"
rev=""
for ch in name:
    rev=ch+rev
print(rev)
#count vowels
name="sameer"
count=0
for ch in name:
    if ch in "aeiou":
        count+=1
        print(count)
#count consonents
name="sameer"
count=0
for ch in name:
    if ch not in "aeiou":
        count+=1
        print(count)
# count spaces
name="python prograamming"
count=0
for ch in name:
    if ch ==" ":
        count+=1
        print(count)
#count characters
name="sameer"
count=0
for ch in name:
    count+=1
    print(count,end=" ")
    ########################################################3
############################################

#print your name
def your_name():
    return "sameer"
print(your_name())
##########################
# add two numbers
def add(a,b):
    return a+b
add(10,20)
#square of a njumber
def square_of_number(n):
    return n*n
print(square_of_number(3))
# remainder of 2 numbers 
def remainder(a,b):
    return a%b
print(remainder(3,4))
#check even or odd
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(7))
#largest of two numbers
def largest(a,b):
    return max(a,b)
print(largest(10,220))
#smallest of two numbers
def smallest(a,b):
    return min(a,b)
print(smallest(10,220))
#simple imtrest
def simple_intrest(p,r,t):
    return (p*r*t)/100
print(simple_intrest(1000,5,2))
#area of rectangle
def area_of_rectangle(length,breadth):
    return length*breadth
print(area_of_rectangle(5,2))
#perimeter of rectangle
def perimeter(length,width):
    return 2*(length+width)
print(area_of_rectangle(4,2))
#area of circle
def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(2))
# print numbers from 1 to n
def print_numbers(n):
    result=[]
    for i in range(1,n+1):
        result.append(i)
    return result
print(print_numbers(3))
#print even numbers from 1 to n 
def even_numbers(n):
    result=[]
    for i in range(1,n+1):
        if i%2==0:
            result.append(i)
    return result
print(even_numbers(10))
#print 0dd numbers
def odd_numbers(n):
    result=[]
    for i in range(1,n+1):
        if i%2!=0:
            result.append(i)
    return result
print(odd_numbers(10))
# sum of first n numbers 
def sum_of_first_n_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
print(sum_of_first_n_numbers(5))
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))
#count digits in a number
def count_digits(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print(count_digits(12345))
#reverse a number
def reverse_number(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
print(reverse_number(1234))
#sum of digits
def sum_of_digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
print(sum_of_digits(12345))
#palindrome
def palindrome(n):
    rev=0
    temp=n
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return temp==rev
print(palindrome(2002))
#leap year
def leap(year):
    return year%4==0
print(leap(2024))
# maximun of three nu b
def largest(a,b,c):
    return max(a,b,c)
print(largest(10,20,30))
# table numbers
def table(n):
    result=[]
    for i in range(1,11):
        result.append(n*i)
    return result
print(table(10))
#find largest digit
def largest(number):
    max=0
    while number>0:
        digit=number%10
        if digit>max:
            max=digit
        number=number//10
    return max
print(largest(12345678913))
#find smallest digit
def smallest(n):
    min=9
    while n>0:
        digit=n%10
        if digit<min:
            min=digit
        n=n//10
    return min
print(smallest(5345))
###########3prime no
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2
print(prime(7))
###############################################################################3
##############################################################################
###########################################################################3
###############################################################################33
##########################################################################################3
#########################################################################################33
    # INTERMEDIATE PROBLEMS STARTED 
#palindrome mber
def palindrome(n):
    original=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return original==rev
print(palindrome(2002))

# prime number
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "prime number"
    else:
        return "not a prime number"
print(prime(5))
#check prime numbers from 1 to n
def check_prime(n):
    result=[]
    for num in range(2,n+1):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            result.append(i)
    return result
print(check_prime(15))
#fibonacci series
def fibonacci(n):
    a=0
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        c=a+b
        a=b
        b=c
    return result
print(fibonacci(7))
#COUNT VOWELS IN A STRING
def count_vowels(name):
    count=0
    for i in name:
        if i in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels("sameer"))
# count consonents
def count_consonents(name):
    count=0
    for i in name:
        if i not in "aeiouAEIOU":
            count+=1
    return count
print(count_consonents("python"))
#reverse a string
def reverse_string(name):
    rev=""
    for ch in name:
        rev=ch+rev
    return rev
print(reverse_string("sameer"))
#palindrome string
def palindrome_string(name):
    original=str(name)
    reverse=original[::-1]
    if original==reverse:
        return "palindrome"
    else:
        return "not a palindrome"
print(palindrome_string("sameer"))
#count letters
def count_words(name):
    count=0
    for ch in name:
        count+=1
    return count
print(count_words("sameer"))
#count words
def count_words(name):
    words=name.split()
    return len(words)
print(count_words("i love python programming lannguage"))
#largest words
def biggest(*num):
    print(max(num))
biggest(10,20,30,40,50)

def count(*nums):
    print(len(nums))
count(1,2,3,4,5,6,7,8)
####################
def even_sum(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
            print(sum)
even_sum(10)
###########3
def odd_num(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    print(sum)
odd_num(10)

#############
def clg(*sections):
    print(sections)
clg("cse","ece","mech","civil")
# kwargs
def students(**data):
    print(data)
students(name="sameer",age=21,city="machilipatnam")

#####posiy=tional arguments
def order(item,quantity):
    print(item,quantity)
order("burger",2)
##########keyword argumennnnnts
def order(item,quantity):
    print(item,quantity)
order(quantity=2,item="Burger")
#reccursive function
def fact(n):
    if n==0 and n==1:
        return 1
    return n*fact(n-1)
#LOOPS AGAIN IAM PRACTICING STart
for i in range(5):
    print("hello world")
>>>>>>> 31262b1a61a71eaee2b2cf2719f1b7d1c4bdbdb0
