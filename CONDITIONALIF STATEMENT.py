age=18
if age >=18:
    print("eligible for vote")
# another if 
x=20
if x > 5:
    print("greater")
    # another if 
num=25
if num % 5==0:
    print("divisible by five")
print('################################################################################')
# check password using if
password="Sameer123"
if password=="sameer123":
    print("correct password")
else:
    print("incorrect password")
    print('############################################################################')
 #number equality
num=0
if num==0:
    print("this both are same numbers")   
else:
    print("they are different nuombers")
    print('###################################################################')
    # useername check
username="sameer123"
if username=="sameer123":
    print("username is correct")
else:
    print("unsername is incorrect")
    print('##############################################################')
    # elif statement with if else  
number=-7
if number>7:
    print("the number is greater than seven")
elif number<7:
    print("the number is less than seven")
else:
    print("the number is equal")
    print('##########################################################')
# another example using these student grade system
marks=50
if marks >=70:
    print("he  is topper")
elif marks >=90:
    print("he is super")
elif marks >=85:
    print("he is good")
elif marks >=80:
    print("nearest good")
elif marks >=70:
    print("average")
else:
    print("he is fail")
print('#########################################################################')
#days example
day=7
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day ==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("tomorrow is a working day")
print('##################################################################################')
print('#############################################################################################')
print('#####################################################################################################')
# LOOPING STATEMENTS(FOR LOOP)
for i in range(5):
    print(i)
    print('#####################################################################################################')
# for using list values
names=["sameer","pandu","arsha",]
for names in names:
    print(names)
    print('#####################################################################################################')
# sum of numbers
total=0
for i in range(1,6):
    total=total+i
    print(total)
    print('#####################################################################################################')
# print squares
for i in range(1,6):
    print(i*i)
    print('#####################################################################################################')
    # print list items
fruits=["apple","banana","pineapple"]
for fruits in fruits:
    print(fruits)

print('#####################################################################')
# for even numbers
for i in range(0,11):
    if i %2==0:
        print(i)


print('##############################################################')
# for odd numbers
for i in range(1,11,2):
    print(i)

print('##################################################################')
# we have 2 methods to write even and odd
# WHILE LOOPS
i=1
while i<=5:
    print(i)
    i=i+1


print('###################################################################################')

# even numbers
i=0
while i<=10:
    print(i)
    i=i+2

print('######################################################################')    
# infinity loop
while True:
    print("hello sameer")
    break

print('#############################################################################')
# reversed loop
i=5
while i>=1:
    print(i)
    i=i-1


print('################################################################################')
    
#BREAK STATEMRNT
for i in range(1,11):
    if i==6:
        break
    print(i)


print('#############################################################################')

for i in range(1,6):
    if i==4:
        break
    print(i)


print('############################################################################')
# list using break
names=["sameer","nazeer","arsha"]
for name in names:
    if name =="sameer":
        break
    print(name)

print('########################################################################################')

#
i=1
while i<=10:
    print(5 * i)
    i+=1

print('#######################################################################################################')
# continue
i=0
while i<=5:
    i+=1
    if i==3:
        continue
    print(i)


print('##########################################################################################')

#factorial
num=5
fact=1
while num >0:
    fact=fact*num
    num-=1
    print(fact)

    
