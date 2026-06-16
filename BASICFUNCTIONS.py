#1)PRINHELLO WORLD USING A FUNCTION
def greet():
    print("hello world")
greet()
# 2)PRINT YOUR NAME
def my_name():
    print("sameer")
my_name()
# 3)PRINTS CLG NAME 
def clg_name():
    print("sri vasavi institute of engineering and technology")
clg_name()
# 4) PRINT CITY
def city():
    print("machilipatnam")
city()
# 4) function calls multiple times
def greet():
    print("hello sameer")
greet()
greet()
greet()
greet()
greet()
greet()
#5)FUNCTION WITH ONE PARAMETER
def student(name):
    print("student name:",name)
student("sameer")
#6)ADD TWO NUMBERS
def add(a,b):
    print(a+b)
add(10,20)
# 7)RETURN VALUE 
def add(a,b):
    return a+b
result=add(10,20)
print(result)
# 8) square number
def square(number):
    return number*number
result=square(2)
print(result)
#9)DIFFERENCE BTW PRINT AND RETURN
def square(number):
    return number*number
result=square(5)
print(result)
#10)default parametres
def greet(name="sameer"):
    print("welcome",name)
greet()
###########################################################################
#############################################################################
###########################################################################
#############################################################################

###########################################################################
#############################################################################
# 1)CREATE A FUNCTION TO PRINT HELLO WORLD
def greet():
    return "hello world"
print(greet())
# with return
def hello_world():
    return "hello world"
print(hello_world)
# 2)create a function to print  your name 
def my_name():
    print("mohammad sameer")
my_name()
############################################################2)
def my_name():
    return "sameer"
print(my_name())
#3)add two numbers
def add(a,b):
    result=a+b
    print(result)
add(10,20)
############################################3)
def add(a,b):
    return a+b
print(add(5,3))
#4)function to subtracty two numbers
def subtract(a,b):
    result=a-b
    print(result)
subtract(10,20)
####################################################
def subtract(a,b):
    return a-b
print(subtract(5,3))
#5)MULTIPLY TWO NUMBERS
def multiply(a,b):
    result=a*b
    print(result)
multiply(2,2)
#####################################################
def multiply(a,b):
    return a*b
print(multiply(2,2))
#6)DIVIDE TWO NUMBERS
def divide(a,b):
    result=a//b
    print(result)
divide(4,2)
####################################
def divide(a,b):
    return a/b
print(divide(4,2))
#7)FIND SQUARE OF A NUMBER
def square(number):
    result=number*number
    print(result)
square(2)
##########################################
def square(number):
    return number*number
print(square(5))
#8)FIND CUBE OF A NUMBER
def cube(number):
    result=number*number*number
    print(result)
cube(2)
##############################
def cube(number):
    return number*number*number
print(cube(2))
#9)FIND REMAINDER OF TWO NUMBERS
def remainder(a,b):
    result=a%b
    print(result)
remainder(6,2)
###################################################
def remainder(a,b):
    return a%b
print(remainder(10,3))
#10)check evven or odd
def check_even_odd(number):
    if number%2==0:
        print("even")
    else:
        print("odd")
check_even_odd(2)
############################################################
def check_even_odd(number):
    if number%2==0:
        return("even")
    else:
        return("odd")
print(check_even_odd(2))
# 11)FIND LARGEST OF TRWO NUMBERS
def largest(a,b):
    if a>b:
        print("largest of ",a)
    else:
        print("largest of",b)
largest(10,20)
########################################################
def largest(a,b):
    if a>b:
        return "largest is",a
    else:
        return "largest is",b
print(largest(2,3))
#12 FIND SMALLEST OF TWO NUMBERS
def smallest(a,b):
    if a<b:
        print("smallest number is",a)
    else:
        print("smallest nunmber is",b)
smallest(10,20)
####################################33
def smallest(a,b):
    if a>b:
        return "smallest number is",a
    else:
        return "smallest number is",b
print(smallest(2,3))

#13)calculate simp]le intrest
def simple_intrest(p,r,t):
    result=(p*r*t)/100
    print(result)
simple_intrest(10000,5,2)
###############################
def simple_intrest(p,r,t):
    return (p*r*t)/100
print(simple_intrest(10000,5,2))
#14)AREA OF RECTANGLE9
def area_of_rectangle(length,width):
    area=length*width
    print(area)
area_of_rectangle(5,3)
#######################333
def area_of_rectangle(length,breadth):
    return length*breadth
print(area_of_rectangle(10,5))
#15)perimeter of rectangle
def perimeter_of_rectangle(length,width):
    perimeter=2*(length+width)
    print(perimeter)
perimeter_of_rectangle(10,5)
####################################
def perimeter_of_rectangle(length,width):
    return  2*length+width
print(perimeter_of_rectangle(10,5))
#)area of circle
def area_of_circle(radius):
    area=3.14*radius*radius
    print(area)
area_of_circle(1)
######################333
def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(2))
# 17)print numbers  sum from 1 to n
def sum_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
print(sum_numbers(3))


#18)print even numbers from 1 to n
def even_numbers(n):
    for i in range(2,n+1,2):
        print(i)
even_numbers(10)
################
def even_numbers(n):
    result=[]
    for i in range(1,n+1):
        if i%2==0:
            result.append(i)
    return result
print(even_numbers(10))
################## return usingh
def even_numbers(n):
    result=[]
    for i in range(2,n+1):
        if i%2==0:
            result.append(i)
    return result
print(even_numbers(10))
#19)PRINT ODD NUMBERS FROM 1 TO N
def odd_numbers(n):
    result=[]
    for i in range(1,n+1,):
        if i%2!=0: 
            result.append(i)
    return result
print(odd_numbers(10))
#########################
def odd_numbers(n):
    result=[]
    for i in range(1,n+1):
        if i%2!=0:
            result.append(i)
    return result
print(odd_numbers(10))
#20)sum of first n numgers
def sum_of_n_numbers(n):
    result=[]
    total=0
    for i in range(1,n+1):
        result.append(i)
        total+=i
    return total
print(sum_of_n_numbers(3))

# 21)FACTORIAL OF A NUMBER 
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
factorial(3)
######################
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))

# 22)COUNT DIGITS IN A numbber
def count_digits(number):
    count=0
    while number>0:
        count+=1
        number=number//10
        print(count)
count_digits(12345)
####################333333
def count_digits(n):
    count=0
    for i in str(n):
        count+=1
    return count
print(count_digits(12345))
# 23)reverse a number 
def reverse_number(n):
    n=str(n)
    result=""
    for i in n:
        result=i+result
    return int(result)
print(reverse_number(4321))
#24)SUM OF DIGITS
def sum_of_digits(n):
    total=0
    n=abs(n)
    for i in str(n):
        total=total+int(i)
    return total
print(sum_of_digits(1234))
#25)PALINDROME NUMBER
def palindrome_number(n):
    original=str(n)
    reverse=""
    for i in original:
        reverse=i+reverse
    return original==reverse
print(palindrome_number(111))
# 26) leap year
def leap_year(year):
    if year%4==0 and year%2==0:
        return True
    else:
        return False
print(leap_year(2024))
#27)MAX OF THREE NUMBERS
def max_three_numbers(a,b,c):
    max_value=a
    for i in [b,c]:
        if i>max_value:
            max_value=i
    return max_value
print(max_three_numbers(10,25,15))
#####################
def add(a,b):
    return a+b
print(add(3,4))

def greet():
    return "sameer"
print(greet())
############################################################333
###################################################333
# MONDAY PRACTICE
def greet():
    print("sameer")
greet()
###########
def greet():
    return "sameer"
print(greet())
###################################
# function with parametres
def add(a,b):
    print(a+b)
add(2,3)
####################
def add(a,b):
    return a+b
print(add(2,3))
##############
# defaukt argumebts
# def function_name(parametre=value):
def greet(name="sameer"):
    print("hello",name)
greet()
greet("ali")
################################## default arguments and keyword arguments
def reverse_ar