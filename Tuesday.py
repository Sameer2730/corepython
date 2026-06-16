for i in range(1,11):
    print(i)
# 2)1 TO 10 USING WHILE 
i=1
while i<=10:
    print(i)
    i+=1
# 3)print 10 to i using for 
for i in range(10,0,-1):
    print(i)
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