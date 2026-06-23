# PRINT NUMBER FROM 1 TO 10
for i in range(1,11):
    print(i)
####### while
i=1
while i<=10:
    print(i)
    i+=1
#######2)sum of 1 to 5
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
###################3
n=5
sum=0
i=0
while i<=5:
    sum+=i
    i+=1
print(sum)
###############
# 3)even numbers 1 to 10
n=10
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
####################33
n=10
i=0
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1
####################3333
for i in range(1,12):
    if i%2!=0:
        print(i,end=" ")
#################333
print("################################################################")

i=0
while i<=11:
    if i%2!=0:
        print(i,end=" ")
    i+=1

print("################################################################")

#####################33
n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#####################################
i=1
sum=0
while i<=20:
    sum+=i
    i+=1
print(sum)

print("################################################################")

###########
for i in range(1,21):
    print(i)
#######
i=20
while i>=0:
    print(i)
    i-=1

print("################################################################")

for i in range(20,0,-1):
    print(i)
#######3
sum=0
for i in range(1,21):
    sum+=i
print(sum)
##############3
i=0
while i<=10:
    if i%2!=0:
        print(i)
    i+=1

##############3
for i in range(10,0,-1):
    print(i,end=" ")
##############################33
i=11
while i>=2:
    i-=1
    print(i,end=" ")
######333
# sum 1 to 10
sum=0
for i in range(1,11):
    sum+=i
print(sum)
########################33
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)
################333
for i in range(1,6):
    print(i*i,end=" ")
############33
i=1
while i<=5:
    print(i*i,end=" ")
    i+=1
##################3
i=5
while i>=1:
    i-=1
    print(i*i,end=" ")
###########################3333
a=0
b=1
for i in range(11):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
##########################3
a=0
b=1
i=1
while i<=10:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1
########333
for i in range(1,6):
    print(i*i*i)
#########################
for i in range(1,21):
    print(i,end=" ")
####33
i=1
while i<=20:
    print(i)
    i+=1
##########3
for i in range(10,0,-1):
    print(i,end=" ")
#######
i=10
while i>=1:
    print(i)
    i-=1
#######
# 4)
for i in range(1,21):
    if i%2==0:
        print(i)
##################333
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1
#############33
for i in range(1,20):
    if i%2!=0:
        print(i,end=" ")
#######
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

print('##################################')

############
sum=0
for i in range(1,11):
    sum+=i
print(sum)
############
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)
#7)
sum=0
for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
######3
i=1
sum=0
while i<=20:
    if i%2==0:
        print(i,end=" ")
    i+=1
############3
sum=0
for i in range(1,20):
    if i%2!=0:
        print(i,end=" ")

#########33
i=1
sum=0
while i<=20:
    if i%2!=0:
        print(i,end=" ")
    i+=1
###############33
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)
##########
n=5
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1
#######################333
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
##########3
n=5
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)
######################
for i in range(1,11):
    print(i*i,end=" ")
##########33
i=1
while i<=10:
    print(i*i,end=" ")
    i+=1
################################333
for i in range(1,11):
    print(i*i*i,end=" ")
############
i=1
while i<=10:
    print(i*i*i,end=" ")
    i+=1
###############33
#reverse a number
n=1234
rev=0
for i in str(n):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
###########################3
n=1234
rev=0
i=1
while i<=n:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
#########################
# num=431
# temp=num
# rev=0
# for _ in str(num):
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# if num==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

##############33
num=2003
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")
#########33
num=12345
n=str(num)
rev=""
for i in n:
    rev=i+rev
if n==rev:
    print("palindrome")
else:
    print("not a palindrome")

##############
name="madam"
rev=""
for i in name:
    rev=i+rev
if name==rev:
    print("palindrome")
else:
    print("not a palindrome")
######################################
name="sameer"
temp=name
rev=""
i=len(name)-1
while i>=0:
    rev=rev+name[i]
    i-=1
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")
#####################################33
num=2002
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")
    
#########
n=10
count=0
for i in range(1,n+1):
    temp=i
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if i==rev:
        count+=1
print(count)
########3
n=15
sum=0
for i in range(1,n+1):
    temp=i
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if i==rev:
        sum+=i
print(sum)
######################333
n=50
largest=0
for i in range(1,n+1):
    temp=i
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if i==rev:
        largest=i
        print(largest)

##############3
numbers=12345
sum=0
for i in str(numbers):
    sum+=int(i)
print(sum)
##################33
numbers=12345
sum=0
i=1
while numbers>0:
    digit=numbers%10
    sum+=digit
    numbers=numbers//10
print(sum)
########################33333
numbers=123456
sum=0
for i in str(numbers):
    sum+=int(i)
print(sum)
###########################333
numbers=123456
sum=0
i=1
while numbers>0:
    digit=numbers%10
    sum+=digit
    numbers=numbers//10
print(sum)
#######################################333
numbers=123456789
count=0
for i in str(numbers):
    count+=1
print(count,end=" ")
###############################3
#######
numbers=12345
count=0
while numbers>0:
    digit=numbers%10
    count+=1
    numbers=numbers//10
print(count)
#######################333
numbers=123456
rev=""
for i in str(numbers):
    rev=i+rev
print(rev)
#############33
numbers=1234567
rev=0
while numbers>0:
    digit=numbers%10
    rev=rev*10+digit
    numbers=numbers//10
print(rev)
###################################33
numbers=12345
rev=""
for i in str(numbers):
    rev=i+rev
result=int(numbers)+int(rev)
print(result)
##########################
# armstrong number
numbers=136
temp=numbers
n=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp=temp//10
if sum==numbers:
    print("armstrong number")
else:
    print("non armstrong number")
#####################3333
nums=[1,2,3,4,5]
result=[]
for i in nums:
    result.append(i)
print(result)
#####################33
nums=[1,2,3,4,5]
result=[]
i=1
while i<len(nums):
    print(nums[i])
    i+=1
#####################33333
arr=[1,2,3,4,5]
sum=0
for i in arr:
    sum+=i
print(sum)
############
arr=[1,2,3,4,5]
sum=0
i=0
while i<len(arr):
    sum+=arr[i]
    i+=1
print(sum)

###########
arr=[5,15,25]
sum=0
for i in arr:
    sum+=i
print(sum)
######################33
arr=[1,2,3,4,5,6,7]
sum=0
i=1
while i<len(arr):
    sum+=arr[i]
    i+=1
print(sum)
######################33
arr=[1,2,3,4,5]
result=len(arr)
print(result)
##############3
arr=[1,2,3,4,5,6,7,8]
count=0
for i in arr:
    count+=1
print(count)
############
arr=[1,2,3,4,5,6,7,8]
count=0
i=1
while i<len(arr):
    count+=arr[i]
    i+=1
print(count)
##############3333
arr=[7,8,9]
count=0
for i in arr:
    count+=1
print(count)
############################3
arr=[10,45,23,89,12]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
#######################3
arr=[10,45,23,89,12]
largest=arr[0]
i=0
while i<len(arr):
    if arr[i]>largest:
        largest=arr[i]
    i+=1
print(largest)
#########################
arr=[10,45,23,89,12]
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print(smallest)
#############################3
arr=[10,45,23,89,12]
smallest=arr[0]
i=0
while i>len(arr):
    if arr[i]<smallest:
        smallest=arr[i]
    i+=1
print(smallest)
##################
arr=[1,2,3,4,5,6,7,8]
for i in arr:
    if i%2==0:
        print(i,end=" ")
################
arr=[1,2,3,4,5,6,7,8]
i=0
while i<len(arr):
    if arr[i]%2==0:
        print(arr[i],end=" ")
    i+=1

########################33
arr=[1,2,3,4,5,6,7,8]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
###########################3
arr=[1,2,3,4,5,6,7,8]
count=0
i=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)
###################################
arr=[1,2,3,4,5,6,7,8,9,10,11,12]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)
############################
arr=[1,2,3,4,5,6,7,8,9,10,11,12]
count=0
i=0
while i<len(arr):
    if arr[i]%2!=0:
        count+=1
    i+=1
print(count)
#######################3
arr=[10,20,30,40,50]
rev=[]
for i in arr:
    rev=[i]+rev
print(rev)
#######################3
arr=[10,20,30,40,50]
reverse=[]
i=len(arr)-1
while i>=0:
    reverse.append(arr[i])
    i-=1
print(reverse)
#######################33
arr=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in arr:
    if i%2==0:
        sum+=i
print(sum)
#####################3
arr=[1,2,3,4,5,6,7,8,9,10]
sum=0
i=0
while i<len(arr):
    if arr[i]%2==0:
        sum+=arr[i]
    i+=1
print(sum)
#####################
arr=[1,2,3,4,5,6]
sum=0
for i in arr:
    if i%2!=0:
        sum+=i
print(sum)
#########################3
arr=[1,2,3,4,5,6]
sum=0
i=0
while i<len(arr):
    if arr[i]%2!=0:
        sum+=arr[i]
    i+=1
print(sum)
#############
arr=[2,5,8,11,14]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
###############################
arr=[2,5,8,11,14]
count=0
i=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)
###############################333
numbers=[12,45,7,89,23]
largest=arr[0]
secondlargest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
for i in arr:
    if i!=largest and i>secondlargest:
        secondlargest=i
print("secondlargest",secondlargest)

#33333333333333333333
text="education"
count=0
for i in text:
    if i in "aeiou":
        count+=1
print(count)
########################3
text="education"
count=0
i=0
while i<len(text):
    if text[i] in "aeiou":
        count+=1
    i+=1
print(count)
##################3
text="sameer"
count=0
for i in text:
    if i not in "aeiou":
        count+=1
print(count)
##################
text="education"
count=0
for i in text:
    if i not in "aeiou":
        count+=1
print(count)
##########33
text="PyThOn"
count=0
for ch in text:
    if ch.isupper():
        count+=1
print(count)
######################33
text="PyThOn"
count=0
for ch in text:
    if ch.islower():
        count+=1
print(count)
##########
text="ab12c345"
count=0
for ch in text:
    if ch.isdigit():
        count+=1
print(count)
#########3
number=12345
numbers=str(number)
sum=0
for i in numbers:
    sum+=int(i)
print(sum)
##############33
# reverse a number/
number=12345
numbers=str(number)
rev=""
for i in numbers:
    rev=i+rev
print(rev)
#############3
number="12345"
rev=""
i=0
while i<len(number):
    rev=number[i]+rev
    i+=1
print(rev)
#################33
number="2002"
rev=""
for i in number:
    rev=i+rev
    if rev==number:
        print("palindrome")
    else:
        print("not a palindrome")
##################################3
number=2003
temp=number
rev=0
while number>0:
    digit=number%10
    rev=rev*10+digit
    number=number//10
if temp==rev:
    print("palindrome")
else:
    print("not a palindrome")

########################333
n=153
n=str(n)
count=len(n)
sum=0
for i in n:
    sum+=int(i)**count
if sum==int(n):
    print("armstrongnumber")
else:
    print("non armstrong numbeer")
#############################################33
number=5
fact=1
for i in range(1,number+1):
    fact=fact*i
print(fact)
#############3
number=5
fact=1
i=1
while i<=number:
    fact=fact*i
    i+=1
print(fact)
###################
name="sameer"
rev=""
for i in name:
    rev=i+rev
print(rev)
#######################3333
n=5
for i in range(1,n+1):
    for j in range(n):
        print('*',end=" ")
    print()
##############
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
#############
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)
######################333
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print("* "*i)
######################
# diamond pattern
n=5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("* "*i)
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print("* "*i)
###################3
# mumber pattern
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
####
n=12345
rev=0
i=0 
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
#######3
nums=[10,20,30,40]
nums[0]=99
print(nums)
########33
d={"name":"sameer","age":20}
print(d.keys())
print(d.values())
print(d.items())
######################3
# d={"x":10}
# print(d["y"])
##########
d={"a":1,"b":2}
d["a"]=d["a"]+1
print(d)
####################33
d={"a":1,"b":2,"c":3}
print(len(d))
##############3
d={"a":1}
d.clear()
print(d)
######################
d={"a":1,"b":2}
print(d.pop("a"))
print(d)
###########
d={"a":1,"b":2}
print("a" in d)
####3
d={"a":1}
d.update({"b":2})
print(d)
#################33
a={"a":1,"b":2}
print(list(d.keys()))
##########3
data={"name":"sameer","age":20}
print(data)
################
user={1:{"name":"sameer","age":20},2:{"name":"prashanth","age":21}}
print(user[1])
print(user[2])
#################33
def get_user(user_id):
    return user.get(user_id,"user not found")
get_user("sameer_123")

print("#####################################")

#############33
def greet():
    print("hello")
#########
def greet(name):
    print("hello",name)
greet("sameer")
##################3
def add(a,b):
    return a+b
result=add(5,6)
print(result)
############
def greet(name="sameer"):
    print("hello",name)
greet()
greet("sameer")
##########3
def calculate(a,b):
    return a+b,a-b
print(calculate(10,5))
##################333
def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(check(10))
######3
add=lambda a,b:a+b
print(add(2,3))
#########################33333
for i in range(1,51):
    print(i)
###############################333
i=1
while i<=50:
    print(i)
    i+=1
#########3
for i in range(1,11):
    if i %2==0:
        print(i,end=" ")
#####3
i=1
while i<=10:
    if i%2==0:
        print(i,end=" ")
    i+=1
##############3
n="123"
sum=0
for i in n:
    sum+=int(i)
print(sum)
#######################3
n=123
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)
##################3
num="12345678"
rev=""
for i in num:
    rev=i+rev
print(rev)
##################3
num=1234567889
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)
#############333
num="12345"
rev=""
for i in num:
    rev=i+rev
print(rev)
###############33
num="123456"
rev=""
i=len(num)-1
while i>=0:
    rev=rev+num[i]
    i-=1
print(rev)
################
name="sameer"
if name==name[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
####################################
name="sameer"
count=0
for ch in name:
    if ch in "aeiou":
        count+=1
print(count)
###########################333
name="sameer"
count=0
for ch in name:
    if ch not in "aeiou":
        count+=1
print(count)
###################3
# name="i love python programming"

# for word in name.split():
#     count+=1
# print(count)
# ###########
# text="i love python programming"
# words=text.split()
# count=0
# i=0
# while i<len(words):
#     count+=1
#     i+=1
# print(count)
# #########################33
# text="hello ai world from india"
# words=text.split()
# i=0
# count=0
# while i<len(words):
#     count+=1
#     i+=1
# print(count)
# ###########33
# text="python"
# rev=""
# for ch in text:
#     rev=ch+rev 
# print(rev)
# ##############
# text="python"
# rev=""
# i=len(text)-1
# while i>=0:
#     rev+=text[i]
#     i-=1
# print(rev)
# ######################33
# name="madam"
# rev=""
# for i in name:
#     rev=i+rev
# if rev==name:
#     print("palindrome")
# else:
#     print("nota palindrome")
# #################3
# name="madam"
# rev=""
# i=len(name)-1
# while i>=0:
#     rev=name[i]+rev
#     i-=1
# if name==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")
# #################################3
# name="banana"
# freq={}
# for ch in name:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)
# ########################
# name="banana"
# freq={}
# i=0
# while i<len(name):
#     ch=text[i]
#     if ch in freq:
#         freq[i]+1
#     else:
#         freq[i]=1
# print(freq)

##########################
nums=[10,20,30,40]
sum=0
for i in nums:
    sum+=i
print(sum)
################33
nums=[10,20,30,40,50]
i=0
sum=0
while i<len(nums):
    sum+=nums[i]
    i+=1
print(sum)
####################3
nums=[5,10,15,20]
sum=0
for i in nums:
    sum+=i
print(sum)
###########

############333
numbers=[12,45,7,89,23]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
for i in numbers:
    if i!=largest and i>secondlargest:
        secondlargest=i
print(secondlargest)
##################################################33
numbers=[12,45,7,89,23]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print("smallest", smallest)
for i in numbers:
    secondsmallest=numbers[0]
if i<secondsmallest and i!=smallest:
    secondsmallest=i
print("seondsmallest", secondsmallest)
######################33
numbers=[1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9,10,10]
result=[]
for i in numbers:
    if i not in result:
        result.append(i)
print(result)
##########
arr=[10,20,10,30,20,40]
result=[]
i=0
while i<len(arr):
    if arr[i] not in result:
        result.append(arr[i])
    i+=1
print(result)
################3
numbers=[1,2,3,4,5,2,3,4,5,2,1,1,4]
freq={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
########
# list1=[1,2,3]
# list2=[3,4,5]
# for i in list2:
#     list1.append(i)
# print(list1)
###########3
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
#############3
list1=[1,2,3,4,5]
list2=[3,5,7,8]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print(common)
#####
list1=[1,2,3,4,5]
list2=[3,5,7,8]
print(list(set(list1)& set(list2)))
##############################################3
numbers=[20,30,40,50,60,70]
result=numbers[1:]+[numbers[0]]
print(result)
############################33
numbers=[10,20,30,40,50]
reverse=[]
for i in numbers:
    reverse=[i]+reverse
print(reverse)

##############
numners=[1,2,3,4,5]
if numbers==numbers[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
######################################33
numbers=[40,10,30,20]
print(sorted(numbers))
###############
numbers=[70,20,50,10]
print(sorted(numbers))
###############3
numbers=[1,0,2,0,3,0,4,0,5,0]
result=[]
for i in numbers:
    if i!=0:
        result.append(i)
zeros=numbers.count(0)
for i in range(zeros):
    result.append(0)
print(result)
###################3
list1=[1,2,3,4]
list2=[3,4,5,6]
union=[]
for i in list1:
    if i not in union:
        union.append(i)
for i in list2:
    if i not in union:
        union.append(i)
print(union)
########################33
numbers=[10,20,30,40,50,60]
find=30
found=False
for i in numbers:
    if i==find:
        found=True
        break
if found:
    print(found)
else:
    print(not found)
#################
numbers=[10,20,30,40,50]
find=30
if find in numbers:
    print("found")
else:
    print("not found")
##############
numbers=[10,20,30,40,50]
find=30
for i in range(len(numbers)):
    if numbers[i]==find:
        print(i)
        break
########################################33
numbers=[15,25,35,45]
find=35
found=False
for i in numbers:
    if i==find:
        found=True
if found:
    print("found")
else:
    print("not found")
##########################3333
numbers=[10,20,10,30,10,40]
find=10
count=0
for i in numbers:
    if i==find:
        count+=1
print(count)
###############
numbers=[5,5,8,9]
find=5
count=0
for i in numbers:
    if i==find:
        count+=1
print(count)
#######
numbers=[1,2,1,1,3]
find=1
found=False
for i in numbers:
    if i==find:
        found=True
if found:
    print("found")
else:
    print("not found")

#################33
numbers=[1,2,2,3,3,4,4,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8]
freq={}
for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
#################33
nums=[10,20,30,40]
find=40
for i in range(len(nums)):
    if nums[i]==find:
        print("index=",i)
nums=[10,20,30,40,50]
target=60
for i in nums:
    if i==target:
        print("found")
    else:
        print("not found")
        break
#####################333
nums=[10,20,30,40,50,60]
target=30
found=False
for i in nums:
    if i==target:
        found=True
if found:
    print("found")
else:
    print("not found")
##############
nums=[1,2,3,4,5]
target=5
for i in range(len(nums)):
    if nums[i]==target:
        print("found")
###########################3
number="12345678"
rev=""
for i in number:
    rev=i+rev
print(rev)
##############3
nums=[10,20,30,40,50]
target=30
count=0
for i in nums:
    if i==target:
        count+=1
print(count)
##############################33
nums=[1,2,2,2,5]
target=2
count=0
for i in nums:
    if i==target:
        count+=1
print(count)
#################
nums=[1,2,2,2,5]
target=2
result=[]
for i in nums:
    if i==target:
        result.append(i)
print(result)