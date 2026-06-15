#CFEATE A VARIABLES FOR NAME AGE MARKS CITY
name="sameer"
age=20
marks=30
city="machilipatnam"
print(name)
print(age)
print(marks)
print(city)
#2PRIT DATA TYPES OF DIFFERENT VARIABLES

print('##################################################################################')
name="sameer"
age=20
marks=25.5
print(type(name))
print(type(age))
print(type(marks))

print('##################################################################################')
#3)CONVERT INTEGER TO FLOAT
num=10
result=float(num)
print(result)
print(type(result))

print('##################################################################################')
#4)CONVERTING FLOAT TO INTEGER
num=20.0
result=int(num)
print(result)
print(type(result))

print('##################################################################################')
#5)CONVERT INTEGER TO STRING
num=100
result=str(num)
print(result)
print(type(num))

print('##################################################################################')
#6)CREATEW A LIST OF 5 NUMBERS AND PRINT THE FIRST ELEMENT
numbers=[1,2,3,4,5]
print(numbers[0])

print('##################################################################################')
#7) CREATE A TUPLE OF 4 COLORS AND PRINT THE LAST ELEMENT
name=("red","green","orange","blue")
print(name[3])

print('##################################################################################')
#8)CREATE A DICTIONARY WITH STUDENT DETAILS
student={"name":"sameer","age":21,"marks":100}
print(student)

print('##################################################################################')
#9)CREATE A SET WITH DUPLICATES VALUES AND PRINT IT
numbers={1,2,3,2,1,4,5,5,4,6,7}
print(numbers)

print('##################################################################################')
#10)FIND LENGTH OF STRING
name="sameer"
print(len(name))

print('##################################################################################')
#11)ACCESS CHARACTERS USING INDEX
word="python"
print(word[2])

print('##################################################################################')
#12)ADD ITEM TO LIST
list_items=["apple","banana","mango"]
list_items.append("pineapple")
print(list_items)

print('##################################################################################')

#13)REMOVE ITEM FROM LIST
name=["sameer","prashanth","rohan"]
name.remove("rohan")
print(name)

print('##################################################################################')

#14)UPDATE VALUE INTO DICTIONARY
student={"name":"sameer","age":20}
student["age"]=22
print(student)

print('##################################################################################')
#15)CHECK ITEM EXITS INTO LIST
num=[10,20,30,50]
print(20 in num)

print('##################################################################################')
#INTERMEDIATE DATA TYPES QUESTIONS
#16)SWAP TWO VARIABLES WITHOUT THIRD VARIABLES
a=10
b=20
a,b=b,a
print(a)
print(b)

print('##################################################################################')
#17)COUNT TOTAL WORDS IN SENTENSES
text="i like coding and iam currently practising programs"
words=text.split()
print(len(words))

print('##################################################################################')
#18)REVERSE A STRING
text="python"
print(text[::-1])

print('##################################################################################')
#19)FIND MAXIMUM VALUE IN LIST
numbers=[1,10,100,1000,10000]
print(max(numbers))

print('##################################################################################')
#20)FIND MINIMUM VALUE IN TUPLE
numbers=(1,2,3,4,5,6,7,8,9)
print(min(numbers))

print('##################################################################################')
#21)MERGE LISTS
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

print('##################################################################################')
#22)REMOVE DUPLICATES FROM LIST
numbers=[1,2,2,3,3,4,4,5,6,7]
result=list(set(numbers))
print(result)

print('##################################################################################')
#23)COUNT FREQUENCY CHARACTER
name="banana"
print(name.count("a"))

print('##################################################################################')
#24)CREATE A NESTED DICTIONARY  FOR STUDENT DETAILS AND ACCESSES MARKS
student={"s1": {"name":"sameer","marks":100,"age":21}}
print(student["s1"]["marks"])

print('##################################################################################')
#25)SORT LIST WITH OUT USING SORT()
numbers=[50,40,30,20,10]
print(sorted(numbers))

print('##################################################################################')
#26)FIND SUM OF LIST
numbers=[1,2,3,4,5]
print(sum(numbers))

print('##################################################################################')
#28)FIND COMMON ELEMENTS INTO IT
list1=[1,2,3,4]
list2=[3,4,5,6]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("common elements=",common)

#29)CONVERT LIST INTO TUPLE
numbers=[1,2,3,4,5]
result=tuple(numbers)
print(result)
# CONVERT TUPLE INTO LIST
numbers=(1,2,3,4,5)
result=list(numbers)
print(result)
#CREATING DICTIONARY USINHG KEYS AND VALUES
student={"name":"sameer","age":21}
print(student)
print('##################################################################################')
print('##################################################################################')
print('##################################################################################')
#OPERATORS IN PYTHON 
#31)ADDITION OF TWO NUMBERS
a=20
b=30
print(a+b)

print('##################################################################################')
#32)subtraction of two numbers
a=50
b=20
print(a-b)

print('##################################################################################')
#33)MULTIPLICATION OF TWO NUMBERS
a=30
b=2
print(a*b)

print('##################################################################################')
#34)DIVISION OF TRWO NUMBERS
a=10
b=10
print(a/b)

print('##################################################################################')
#35)MODULUS OPERATOR
a=20
b=10
print(a%b)

print('##################################################################################')
#36)SquaRE OF NUMBERS
a=3
b=3
print(a**b)

print('##################################################################################')
#37)CHECK EQUAL NUMBERS
a=10
b=10
print(a==b)

print('##################################################################################')
#38) check different  NUMBERS
a=20
b=30
print(a!=b)

print('##################################################################################')
#39)CHECK GREATER THAN using if else
a=10
b=20
if a>=b:
    print("a is greater than b")
else:
    print("b is greater than a")
#40)LESS THAN
a=10
b=20
print(a<b)
#41)FIND REMAINDER WHEN DIVIDED BY 4
a=20
b=4
print(a%b)
#42)check wheather 75>50
a=75
b=50
print(a>b)
#43)check weather 20<10
a=20
b=10
print(a<b)
#43 check and
a=2
b=3
print(a!=b and a==b)
#44 CHECK WEATHER APPLE EXITS IN FRUITS OR NOT
fruits=["apple","banana","mango"]
print("apple" in fruits)
#45 check identity
a=10
b=10
print(a is b)
print('##################################################################################')
print('##################################################################################')
print('##################################################################################')
#IF CONDITIONS
#POSITIVE OR NEGETIVE
a=10
b=20
if a>b:
    print("negetive")
else:
    print("positive")

print('##################################################################################')
#46)POSITIVE OR NEGETIVE
num=15
if num>=0:
    print("positive")
else:
    print("negetive")

print('##################################################################################')
#47)EVEN OR ODD
num=20
if num %2==0:
    print("it is a even number")
else:
    print("it is a odd number")

print('##################################################################################')
#48)ELIGIBLE TO VOTE
age=18
if age>=18:
    print("he is eligible to vote")
else:
    print("he is not eligible to vote")

print('##################################################################################')
#49)PASS OR FAIL
marks=30
if marks >35:
    print("he passed exam")
else:
    print("he failed exam")

print('##################################################################################')
#50)GREATER AMONG TWO NUMBERS
a=20
b=30
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

print('##################################################################################')
#51)CHECK WHEATHER AGE 20 ELIGIBLE TO VOTE
age=20
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


print('##################################################################################')

#52)check wheatheer marks 33 FAIL OR NOT
marks=30
if marks>=30:
    print("he passed exam")
else:
    print("he failed exam")

print('##################################################################################')
#53)CHECK WHEATHER 55 DIVISIBLE BY 5
number=55
if number%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

print('##################################################################################')

#54)CHEACK WHEATHER 2024 IS A LEAP YEAR OR NOT
year=2024
if year%6==0:
    print("leap year")
else:
    print("not a leap year")

print('##################################################################################')

#55)CHECK WHEATHER "E" VOWELS AND CONSONENTS
ch="e"
if ch in "aeiou":
    print("vowel")
else:
    print("consonents")

print('##################################################################################')
#56)check wheather 0 is zero or not
number=int(input("enter a number here:"))
if number==0:
    print("zero")
else:
    print("non zero")

print('##################################################################################')

#57)DAYS COUNT
day=3
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
else:
    print("invalid")

print('##################################################################################')
#INTERMEDIATE
#58)FIND LARGEST AMONG 10,50,30
a=10
b=50
c=30
if a>b and a>c:
    print("largest")
elif b>a and b>c:
    print("largest value")
else:
    print("smallest")

print('##################################################################################')
#59)FIND SMALLEST AMONG 5,2,8
a=5
b=2
c=8
if a>8 and b>8:
    print(a)
elif b<8:
    print(b)
else:
    print(c)

print('##################################################################################')

#60)CREATE GRADE SYSTEM FOR MARKS 85
marks=85
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=70:
    print("C grade")
else:
    print("fail")

print('##################################################################################')

#61)CREATE CALCULATOR USING 20 AND 10
a=20
b=10
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("modulus:",a%b)

print('##################################################################################')
########################################3
a=10
b=5
op="+"
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print(completed)



print('##################################################################################')

#62)#CHECK WHEATHER SIDES IS A VALID TRIANGLE OR NOT 3,4,5
a=3
b=4
c=5
if a+b>c and b+c>a and a+c>b:
    print("valid triangle")
else:
    print("invalid triangle")


print('##################################################################################')
#63)CK PASSWORD "PYTHON123 STRONG OR WEAK PASSWORD"
password="python123"
if len(password)>=8:
    print("strong password")
else:
    print("weak password")

print('##################################################################################')

#64)check wheather a uppercase or lowercase
ch="A"
if ch.isupper():
    print("uppercase")
else:
    print("lowercase")

print('##################################################################################')
#65)ATM WITHDRAW BALANCE=5000,WITHDRAW=2000
total_balance=5000
withdraw=2000
if withdraw<=total_balance:
    print("withdraw sucesfull")
else:
    print("withdraw unsuccesfull")

print('##################################################################################')
#66)CHECK CLASS FOR DISTINCTION MARKS78
marks=78
if marks>=75:
    print("distinction")
elif marks>=65:
    print("A grade")
elif marks>=60:
    print("b grade")
else:
    print("fail")
#67)CREATE TRAFFIC SIGNAL PROGRAM
signal="yellow"
if signal=="red":
    print("stop")
elif signal=="orange":
    print("get ready")
elif signal=="green":
    print("go")
else:
    print("nothing")

print('##################################################################################')
#68)TICKET PRICE CHECKER
age=17
if age<15:
    print("child ticket")
elif age<20:
    print("adult")
else:
    print("old aged persons")

print('##################################################################################')

###########################
age=10
if age<5:
    print("free ticket")
elif age<=18:
    print("ticket price=50")
else:
    print("ticket price =100")

print('##################################################################################')

#69)CHECK WHEATHER A NUMBER IS PALINDROME OR NOT
num=121
original=str(num)
reverse=original[::-1]
if original==reverse:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

print('##################################################################################')
#70)FACTORIAL OF 5
num=5
fact=1
for i in range(1,6):
    fact=fact*i
print("factorial=",fact)

print('##################################################################################')

#71)REVERSE A NUMBER
num=123
reverse=str(num)[::-1]
print("reversed number=",reverse)

print('##################################################################################')
#72)COUNT DIGITS IN A NUMBER
num=1234567
count=len(str(num))
print("total digits=",count)

#73)UM OF DIGITS OF NUMBER
num=123
total=0
for i in str(num):
    total=total+int(i)
    print("sum of digits=",total)

print('##################################################################################')
numbers=[1,2,3,4,5]
total=sum(numbers)
print(total)

print('##################################################################################')
#74)
# CHECK WHEATHER STRING IS PALINDROME OR NOT
#FIND LARGEST ELEMENT
#SECOND LARGEST ELEMENT IN LIST
#COUNT VOWELS IN STRING
# FIND COMMON ELEMENTS IN TWO LIST
print('##################################################################################')
print('##################################################################################')
print('##################################################################################')
print('##################################################################################')
name="madam"
reverse=name[::-1]
if name==reverse:
    print("palindrome")
else:
    print("not a paliondrome")

print('##################################################################################')
number=2002
reverse=str(number)[::-1]
if str(number)==reverse:
    print("palindrome")
else:
    print("not a palindrome")

print('##################################################################################')
print('##################################################################################')
# find largest number
number=[1,2,3,4,5]
print(numbers[3])
# count vowels in string'
ch='A'
if ch in "AEIOU":
    print("vowels")
else:
    print("consonents")
#common elements
list1=[1,2,3,4,5]
list2=[3,4,5,6]
for i in list1:
    if i in list2:
        print(i)

print('##################################################################################')
