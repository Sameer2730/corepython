for i in range(1,11):
    print(i)
# 2)1 TO 10 USING WHILE 
i=1
while i<=10:
    print(i)
    i+=1
# 3)print 10 to i using for 
    # 3) using while 
i=10
while i>=1:
    print(i)
    i-=1
####4)PRINT EVEN NOS FROM 1 TO 100
for i in range(1,101):
    if i%2==0:
        print(i)
# 4) in while 
i=2
while i<=100:
    if i%2==0:
        print(i)
        i+=2
##############################3333
# 5) print odd numbers 1 to 100
for i in range(1,101):
    print(i)
# 5 in while/ 
i=1
while i<=100:
    if i%2!=0:
        print(i)
    i+=1
###6)SUM OF NUMBERS
sum=0
for i in range(1,101):
    sum+=i
print(sum)

#33333 while 6
i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)
###7)product of numbers from 1 to 10
product=1
for i in range(1,11):
    product*=i
print(product)
########33 while
product=1
i=1
while i<10:
    product*=i
    i+=1
print(product)
###########ge8)
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)
########################################
# 8)
n=5
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1
##############################################333
#9)COUNT DIGITS IN A NUMBER
arr=[1,2,3,4,5,6,7]
count=0
for i in arr:
    count+=1
print(count)
########## in while
# 9)
arr=[1,2,3,4,5,6,7]
count=0
i=0
while i<len(arr):
    count+=1
    i+=1
print(count)
###############################333
# 10)REVERSE A NUMBER
arr=[1,2,3,4,5,6,7]
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")
########### while reverse a number
arr=[1,2,3,4,5,6,7]
i=len(arr)-1
while i>=0:
    print(arr[i],end=" ")
    i-=1
############################
# 11)SUM OF DIGITS
arr=[1,2,3,4,5]
sum=0
for i in arr:
    sum+=i
print(sum)
# 11)while 
arr=[1,2,3,4,5]
sum=0
i=0
while i<len(arr):
    sum+=arr[i]
    i+=1
print(sum)
# 12)PRODUCT OF DIGITS
arr=[1,2,3,4,5]
product=1
for i in arr:
    product*=i
print(product)
############3 in while
arr=[1,2,3,4,5]
product=1
i=0
while i<len(arr):
    product*=arr[i]
    i+=1
print(product)
#########13)largest digit
arr=[1,2,3,4,5]
largest=arr[0]
for i in arr:
    if i>largest:
        largerst=i
print(largerst)
##################### in while
arr=[1,2,3,4,5]
largest=arr[0]
i=0
while i<len(arr):
    if arr[i]>largest:
        largest=arr[i]
    i+=1
print(largest)
############################33
# 14)SMALLEST DIGIT 
arr=[1,2,3,4,5,6]
smallest=arr[0]
for i in arr:
    if i<=smallest:
        smallest=i
print(smallest)
######################333
# in while
arr=[1,2,3,4,5,6]
smallest=arr[0]
i=0
while i<len(arr):
    if arr[i]<smallest:
        smallest=arr[i]
    i+=1
print(smallest)
#################################333
# 15)
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
print(count)
######################3 in while
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
i=0
count=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)
################################33
# 16)
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)
########################33
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
count=0
i=0
while i<len(arr):
    if i%2!=0:
        count+=1
    i+=1
print(count)
#################3333
# PRINT AVERAGE OF N NUMBERS
arr=[1,2,3,4,5]
sum=0
for i in arr:
    sum+=i
average=sum/i
print(average)
##################### in while
arr=[1,2,3,4,5]
i=0
sum=0
while i<len(arr):
    sum+=arr[i]
    i+=1
average=sum/5
print(average)
#############################
# 18)print squares of 1 to 20
for i in range(1,21):
    print(i*i,end=" ")
##################
# in while
i=1
while i<=20:
    print(i,i*i,end=" ")
    i+=1

print('###################################################################')

########################3333
# print cubes
for i in range(1,21):
    print(i**3,end=" ")

print('###################################################################')
########################333
i=0
while i<=10:
    print(i,i**i,end="    ")
    i+=1

print('##################################################')

################################
# 20)factorial
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
################# in while
n=5
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)

###########################################################################3333
##########################################################################33
########################################################################################33
# section 2 if else:
# 1)EVEN OR ODD
n=100
if n%2==0:
    print("even")
else:
    print("odd")
############################33
# positive or negetive or Zero
n=11
if n>10:
    print("positive")
elif n<10:
    print("negetive")
else:
    print("zero")
################3)LARGEST OF 2 NUMBERS
n=20
n1=25
if 20>25:
    print("n1 is largest")
else:
    print("more n2 is largest")
    ######################3
# 4)largest of three numbers
a=50
b=60
c=30
if a>b and a>c:
    print("largest")
elif b>a and b>c:
    print("second largest")
else:
    print("c is largest")
#######################################3
# smallest of three numbers
a=30
b=20
c=1
if a<b and a<c:
    print("smallest")
elif b<a and b<c:
    print("second smallest")
else:
    print("third smallest")
########################################3
# 6)DIVISIBLE BY 3 AND 5
n=15
if n%3==0 and n%5==0:
    print("dividsible by 3 and 5")
else:
    print("not divisible by 5 and 3")
#############################
#LEAP YEAR
year=2024
if year%400==0 or year%4==0 and year%100!=0:
    print("leapyear")
else:
    print("not a leap year")
########################3
# GRADE CALCULATOR
marks=78
if marks>=90:
    print("top performence")
elif marks>=80:
    print("good performence")
elif marks>=70:
    print("average good performence")
elif marks>=60:
    print("average marks")
else:
    print("fail")
###########################33
# VOTING +SENIOR CITIZEN
age=65
if age>=18:
    if age>=60:
        print("vote+senior citizen")
    else:
        print("vote allowed")
else:
    print("not elligible")
#################################33
num=456
if num>10 and num<=100:
    print("2 digit numbeer")
elif  num>100 and num<500:
    print("3 digit number")
else:
    print("single digit number")
############## CHARACTER TYPE
ch="a"
if ch.isdigit():
    print("digit")
elif ch.isalpha():
    print("alphabet")
else:
    print("isalnum")

############3VOWEL OR CONSONENT
character="e"
if ch in "aeiou":
    print("vowels")
else:
    print("consonents")
##################333
# TRIANGLE VALID
a=3
b=4
c=5
if a+b>c and b+c>a and c+a>b:
    print("valid triangle")
else:
    print("ivalid triangle")
###############
pin=1234
balance=5000
if pin==1234:
    if balance>=100:
        print("withdrawal allowed")
    else:
        print("low balance")
else:
    print("wrong pin")
################
a=20
b=10
op="+"
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
else:
    print("invalid operator")

#############################
num=1234
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
###############PAINDROME NUMBER
num=121
temp=num
rev=0
while num>0:
    digit=n%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")

#################
# PRIME NO 
num=7
count=0
i=1
while i<num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print("not a prime no")
################# 1 to 100
num=4
while num<=100:
    count=0
    i+=1
    while i<=num:
        if num%i==0:
            count+=1
        i+=1
    if count==2:
        print(num)
    num+=1

arr=[10,20,30,40,50]
i=len(arr)-1
while i>=0:
    print(arr[i])
    i=i-1
###############3333
# freq
arr=[1,1,1,2,2,4,4,4,3,3,3,3,3]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
###############3
arr=[1,2,3,4,5,6,7,8]
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
################3
# common elements
arr=[1,2,3,4]
arr2=[3,4,5,6]
common=[]
for i in arr:
    if i in arr2:
        common.append(i)
print(common)
#################333
n=5
for i in range(n):
    for j in range(n):
        print('*',end="")
    print()
# $##################3
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end=" ")
    print()
n=5
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
# ###########
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# ##########
n=5
for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()
################################################################################
###############################################################################################
###########################################################################################################33333
# sum of even numbers
arr=[5,8,10,3,2]
sum=0
for i in arr:
    if i%2==0:
        sum+=i
print(sum)
##############3
arr=[12,7,6,9,14]
sum=0
for i in arr:
    if i%2==0:
        sum+=i
print(sum)
###################333
name="sameer"
count=0
for i in name:
    if i in "aeiou":
        count+=1
        print(count)
################
text="education"
count=0
for i in text:
    if i in "aeiou":
        count+=1
print(count)
##################333
arr=[2,3,2,4,3,2]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
#########3
arr=[1,1,2,3,2,1]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
##################
arr=[5,20,8,30,25]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
secondlargest=arr[0]
for i in arr:
    if i!=largest and i>secondlargest:
        secondlargest=i
print(secondlargest)
#####
num=537
rev=int(str(num)[::-1])
print(rev)
###############3333
num=537
rev=""
for i in str(num):
    rev=i+rev
print(rev)
#####################33
num=543
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
###################################333
# num=454
# tenp=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if temp==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")
#################################3333
########################################33
num=121
rev=int(str(num)[::-1])
if num==rev:
    print("palindrome")
else:
    print("not a palindrome")
###########################################33
num=121
rev=""
for i in str(num):
    rev=i+rev
if str(num)==rev:
    print("palindrome")
else:
    print("not a palindrome")
#############33
num=153
temp=num
total=0
while num>0:
    digit=num%10
    total=total+digit**3
    num=num//10
if total==temp:
    print("armstrong number")
else:
    print("not a armstrong number")
#############################################33
num=153
total=0
for i in str(num):
    total=total+int(i)**3
if total==num:
    print("armstrong number")
else:
    print("not a armstrong number")
##################33
num=13
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")
##########3
num=13
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print("not a prime")
##############################33
num=15
i=1
count=0
while i<num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print("not a prime")
#################33
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
##############3
num=5
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)
####################333333
num=2345
sum=0
for i in str(num):
    sum+=int(i)
print(sum)
####################3
num=5
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
print(sum)