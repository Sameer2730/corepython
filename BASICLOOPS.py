n=10
for i in range(1,n+1):
    print(i)

##########################
# in while 
n=10
i=1
while i<=n:
    print(i)
    i+=1
###################
for i in range(1,101):
    if i%2==0:
        print(i)
################### while
n=100
i=0
while i<=n:
    if i%2==0:
        print(i)
    i+=1
#######################
n=100
for i in range(1,n+1):
    if i%2!=0:
        print(i)
####################3 while
n=100
i=0
while i<=n:
    if i%2!=0:
        print(i)
    i+=1
######33333
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)

###############
n=5
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1
####### find sum of n numbers
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
################ while
n=5
i=0
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

#############
# reverse a number
n=1234567
n=str(n)
rev=""
for i in n:
    rev=i+rev
print(rev)
###############33 while
n=1234567
rev=0
while n >0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
############3 count digits
n=12345
n=str(n)
count=0
for i in n:
    count+=1
print(count)
#######################33
n=12345
count=0
while n>0:
    count+=1
    n=n//10
print(count)

# sum of digits
n=12345
n=str(n)
sum=0
for i in n:
    sum+=int(i)
print(sum)
#####################333333
n=12345
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)

#############product of digits
n=12345
n=str(n)
product=1
for i in n:
    product*=int(i)
    print(product)
############## while
n=12345
product=1
while n>0:
    digit=n%10
    product*=digit
    n=n//10
print(product)
###############
# palindrome
n=2003
n=str(n)
rev=""
for i in n:
    rev=i+rev
if n==rev:
    print("palindrome")
else:
    print("not a palindrome")

######3 while
n=2004
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")

###########3 prime
n=10
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")
#################
#  while 
n=3
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print("not prime")
################3
# print all prime nos 1 to 100
for n in range(2,101):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print(n)
#################
# while loop 
n=2
while n<=100:
    i=1
    count=0
    while i<=n:
        if n%i==0:
            count+=1
        i+=1
    if count==2:
        print(n)
    n+=1
# 3fibonacci
n=10
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

######### while
n=10
a=0
b=1
count=0
while count<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1

# square pattern
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
##########3 while
i=1
while i<=4:
    j=1
    while j<=4:
        print('*',end=" ")
        j+=1
    print()
    i+=1
# right angle triangle
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

###############33
arr=[10,20,30,40]
for i in arr:
    print(i)
####################
arr=[10,20,30,40]
i=0
while i<len(arr):
    print(arr[i])
    i+=1
############3 sum of array
arr=[10,20,30,40]
sum=0
for i in arr:
    sum+=i
print(sum)
####################### while
arr=[10,20,30,40]
i=0
sum=0
while i<len(arr):
    sum+=arr[i]
    i+=1
print(sum)
######################## largest element
arr=[10,20,30,40]
largest=arr[0]
for i in arr:
    if i>=largest:
        largest=i
print(largest)
############ while\
arr=[10,20,30,40,50]
i=0
largest=arr[0]
while i<len(arr):
    if arr[i]>=largest:
        largest=arr[i]
    i+=1
print(largest)

##########################################################3333 40 questions 
arr=[1,2,2,3,3,5]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
###################
arr=[10,20,30,40,50,60]
smallest=arr[0]
for i in arr:
    if i<=smallest:
        smallest=i
print(smallest)

################
n=100
for i in range(1,n+1):
    if i%2!=0:
        print(i)
###########
n=100
i=0
while i<=n:
    if i%2!=0:
        print(i)
    i+=1

n=123456789
rev=0

while i<=n:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
##################################################################
# start 40 PROBLEMS
arr=[10,21,33,44,51,60]
for i in arr:
    if i%2==0:
        print(i)

##############
arr=[10,21,33,44,51,60]
i=0
while i<len(arr):
    if arr[i]%2==0:
        print(arr[i])
    i+=1
########################################COUNT ODD NUMBERS 2)
# COUNT ODD NUMBERS
arr=[10,21,33,44,51]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)

###############
arr=[10,21,33,44,51]
i=0
count=0
while i<len(arr):
    if arr[i]%2!=0:
        count+=1
    i+=1
print(count)

###### count even numbers
arr=[10,21,33,44,51,60]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
######################
arr=[10,21,33,44,51,60]
i=0
count=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)
###########################3 SUM OF ODD NUMBERS
arr=[10,21,33,44,51,60]
sum=0
for i in arr:
    if i%2!=0:
        sum+=i
print(sum)
##################
arr=[10,21,33,44,51,60]
sum=0
i=0
while i<len(arr):
    if arr[i]%2!=0:
        sum+=arr[i]
    i+=1
print(sum)
################# sum of even numbers
arr=[10,21,33,44,51,60]
sum=0
for i in arr:
    if i%2==0:
        sum+=i
print(sum)
#########################################
arr=[10,21,33,44,51,60]
sum=0
i=0
while i<len(arr):
    if arr[i]%2==0:
        sum+=arr[i]
    i+=1
print(sum)
#############3 LARGEST ODD NUMBER
arr=[10,21,33,44,51,99]
largest=-1
for i in range(len(arr)):
    num=arr[i]
    if num%2!=0:
        if num>=largest:
            largest=num
print(largest)
#####################################
arr=[10,21,33,44,51,60,99,101]
i=0
largest=arr[0]
while i<len(arr):
    if arr[i]%2!=0:
        if arr[i]>=largest:
            largest=arr[i]
    i+=1
print(largest)
# #SECOND LARGEST EVEN NUMBER
# arr=[10,21,33,44,51,60]
# largest=-1
# secondlargest=-1
# for i in range(len(arr)):
#     num=arr[i]
#     if num%2==0:
#         if num>largest:
#             secondlargest=largest
#             largest=num
#         elif num>secondlargest:
#             secondlargest=num
# print(secondlargest)
# #########################################
# arr=[10,15,20,25,30]
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         print(arr[i])
# #####################
# arr=[10,15,20,25,30]
# i=0
# while i<len(arr):
#     if arr[i]%2==0:
#         print(arr[i])
#     i+=1
# #########################ODD NUMBERS
# arr=[10,15,20,25,30]
# for i in range(len(arr)):
#     if arr[i]%2!=0:
#         print(arr[i])
# ############## while
# arr=[10,15,20,25,30]
# i=0
# while i<len(arr):
#     if arr[i]%2!=0:
#         print(arr[i])
############## REPLACE EVEN NUMBERS WITH 0  
arr=[10,15,20,25,30]
for i in range(len(arr)):
    if arr[i]%2==0:
        print(arr[i])
#############
arr=[10,15,20,25,30]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
############################3333
arr=[11,10,23,44,55,60,72,81,90,100]
for i in range(len (arr)):
    if arr[i]%2==0:
        print(arr[i],end=" ")
#########################
arr=[11,10,23,44,55,60,72,81,90,100]
result=[]
i=0
while i<len(arr):
    if arr[i]%2==0:
        result.append(arr[i])
    i+=1
print(result)
########################################3 now odd
arr=[11,10,23,44,55,60,72,81,90,100]
result=[]
for i in range(len(arr)):
    if arr[i]%2!=0:
        result.append(arr[i])
print(result)
#####################3
arr=[11,10,23,44,55,60,72,81,90,100,100,10,23,44,55]
i=0
result=[]
while i<len(arr):
    if arr[i]%2!=0:
        result.append(arr[i])
    i+=1
print(result)

arr=[11,10,23,44,55,60,72,81,90,100,100,10,23,44,55]
rev=[]
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev)
##################33
arr=[11,10,23,44,55,60,72,81,90,100,100,10,23,44,55]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
#######################333
arr=[11,10,23,44,55,60,72,81,90,100,100,10,23,44,55]
i=0
result=[]
while i<len(arr):
    if arr[i] not in result:
        result.append(arr[i])
    i+=1
print(result)
#####################3
arr=[11,10,23,44,55,60]
sum=0
for i in arr:
    sum+=i
print(sum)
###################33
arr=[11,10,23,44,55,60]
sum=0
i=0
while i<len(arr):
    sum+=arr[i]
    i+=1
print(sum)
###############################
arr=[11,10,23,44,55,60]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>=largest:
        largest=arr[i]
print(largest)
######################333
arr=[11,10,23,44,55,60]
largest=arr[0]
i=0
while i<len(arr):
    if arr[i]>=largest:
        largest=arr[i]
    i+=1
print(largest)
#######################
arr=[11,10,23,44,55,60]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
print(count)
##################33
arr=[11,10,23,44,55,60]
i=0
count=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)
#############33 largest
arr=[10,20,30,40,50,60]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("firstlargest=",largest)
secondlargest=arr[0]
for i in arr:
    if i!=largest and i>secondlargest:
        secondlargest=i
print("secondlargest=",secondlargest)
thirdlargest=arr[0]
for i in arr:
    if i!=largest and i!=secondlargest and i>=thirdlargest:
        thirdlargest=i
print("thirdlargest=",thirdlargest)
##############################################################################33
arr=[11,10,23,44,55,60]
largest=arr[0]
i=0
while i<len(arr):
    if arr[i]>largest:
        largest=arr[i]
    i+=1
print("largest=",largest)
secondlargest=arr[0]
i=0
while i<len(arr):
    if arr[i]!=largest and arr[i]>=secondlargest:
        secondlargest=arr[i]
    i+=1
print("secondlargest=",secondlargest)

#########################################################3
arr=[11,10,23,44,55,60,72,81,90,100,100,10,23,44,55]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
###################################
arr=[20,20,10,30,10,40]
target=10
count=0
for i in arr:
    if i==target:
        count+=1
print(count)