# num=[3,1,5,4,2,7,9,8,6,10,12,11]
# i=0
# while i<len(num):
#     print(num[i],end=" ")
#     i+=2


    # 3 5 2 9 6 12

####################################### PROBLEM 1
arr=[10,20,30,40]
for i in arr:
    print(i)
#####in while
arr=[10,20,30,40]
i=0
while i<len(arr):
    print(arr[i])
    i+=1

print('#########################################################')
# problem 2 REVERSE PRINT LIST
arr=[10,20,30,40]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
##########3 while
arr=[10,20,30,40]
i=len(arr)-1
while i>0:
    print(arr[i])
    i-=1

print('######################################################')
#SUM OF ALL NUMBERS IN LIST PROLEM 3
arr=[10,20,30,40]
sum=0
for i in arr:
    sum+=i
print(sum)
############ while
arr=[10,20,30,40]
i=0
sum=0
while i<len(arr):
    sum=sum+arr[i]
    i+=1
print(sum)
###########
print('################################################')
# AVERAGE OF LIST 
arr=[10,20,30,40]
sum=0
for i in arr:
    sum+=i
avg=sum/len(arr)
print(avg)
###################
# while/
nums=[10,20,30,40]
i=0
sum=0
while i<len(arr):
    sum+=arr[i]
    i+=1
avg=sum/len(arr)
print(avg)

print('################################################################')
# problem 4 count total elements in list
arr=[10,20,30,40]
count=0
for i in arr:
    count+=1
print(count)
########## while
arr=[10,20,30,40]
i=0
count=0
while i<len(arr):
    count+=1
    i+=1
print(count)

print('#############################################')
# problem 5 LARGEST ELEMENT IN LIST 
arr=[10,50,20,80,30]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
########### while
arr=[10,50,20,80,30]
i=0
largest=arr[0]
while i<len(arr):
    if arr[i]>largest:
        largest=arr[i]
    i+=1
print(largest)

print('########################################################3')

# problem 6
# smallest list 
arr=[10,50,20,80,30]
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print(smallest)
#############################3
# while
arr=[10,50,20,80,30]
i=0
smallest=arr[0]
while i>len(arr):
    if arr[i]>smallest:
        smallest=arr[i]
    i+=1
print(smallest)

print('########################################################################')

###########PROBLEM 7
#COUNT EVEN NUMBERS
arr=[10,15,20,25,30]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
############ while
arr=[10,15,20,25,30]
i=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)

print('##############################################################')
# count odd numbers
#problem 8
arr=[10,15,20,25,30]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)
#while
arr=[10,15,20,25,30]
i=0
count=0
while i<len(arr):
    if arr[i]%2!=0:
        count+=1
    i+=1
print(count)

########
# problem 9
# search element in list 
arr=[10,20,30,40,50]
find=40
found=False
for i in arr:
    if i==find:
        found=True
if found:
    print("found")
else:
    print("not found")

# while
arr=[10,20,30,40,50]
find=40
i=0
found=False
while i<len(arr):
    if arr[i]==find:
        found=True
    i+=1
if found:
    print("found")
else:
    print("not found")

print('#######################################################################')
# REVERSE AN ARRAY 
nums=[10,20,30,40]
reverse=[]
for i in range(len(nums)-1,-1,-1):
    reverse.append(nums[i])
print(reverse)
#while loop
nums=[10,20,30,40]
reverse=[]
i=len(nums)-1
while i>=0:
    reverse.append(nums[i])
    i-=1
print(reverse)
###############################
# SECOND LARGEST NUMBER IN AN ARRAY
nums=[10,50,20,90,70]
largest=nums[0]
secondlargest=nums[0]
thirdlargest=nums[0]
for i in nums:
    if i>=largest:
        largest=i
print("largest=",largest)
secondlargest=nums[0]
for i in nums:
    if i!=largest and i>=secondlargest:
        secondlargest=i
print("secondlargest=",secondlargest)
thirdlargest=i
for i in nums:
    if i!=largest and i!=secondlargest and i>thirdlargest:
        thirdlargest=i
print(thirdlargest)
#############################
# while
arr=[10,50,20,90,70]
i=0
largest=arr[0]
while i<len(arr):
    if arr[i]>largest:
        largest=arr[i]
    i+=1
print("largest=",largest)
i=0
secondlargest=arr[0]
while i<len(arr):
    if arr[i]!=largest and arr[i]>secondlargest:
        secondlargest=arr[i]
    i+=1
print("secondlargest=",secondlargest)
i=0
thirdlargest=arr[0]
while i<len(arr):
    if i!=largest and i!=secondlargest and i<=thirdlargest:
        thirdlargest=arr[i]
    i+=1
print("thirdlargest=",thirdlargest)
################################3
# # SMALLEST NUMBER
# arr=[10,50,20,90,70]
# smallest=arr[0]
# for i in arr:
#     if i<smallest:
#         smallest=i
# print("smallest=",smallest)
# secondsmallest=arr[0]
# for i in arr:
#     if i!=smallest and i<second smallest:
#         secondsmallest=i
# print("second smallest=",second smallest)
#  SMALLEST NUMBER
# arr=[10,50,20,90,70]
# smallest=arr[0]
# for i in arr:
#     if i<smallest:
#         smallest=i
# print("smallest=",smallest)
# secondsmallest=arr[0]
# for i in arr:
#     if i!=smallest and i<second smallest:
#         secondsmallest=i
# print("second smallest=",second smallest)
# # 

#  SMALLEST NUMBER
# arr=[10,50,20,90,70]
# smallest=arr[0]
# for i in arr:
#     if i<smallest:
#         smallest=i
# print("smallest=",smallest)
# secondsmallest=arr[0]
# for i in arr:
#     if i!=smallest and i<second smallest:
#         secondsmallest=i
# print("second smallest=",second smallest)
#COUNT FREQUENCY I NEED
arr=[10,20,10,30,10,50]
search=10
count=0
for i in arr:
    if i==search:
        count+=1
print("frequency=",count)

#####################
# while
arr=[10,20,10,30,10,50]
search=10
count=0
i=0
while i<len(arr):
    if arr[i]==search:
        count+=1
    i+=1
print(count)

# revserse
arr=[10,20,30,40,50]
for i in range(4,-1,-1):
    print(arr[i])
# while
arr=[10,20,30,40,50]
i=len(arr)-1
while i>=0:
    print(arr[i])
    i-=1
# search an elemen
arr=[10,20,30,40,50,50,50,50,50]
target=50
count=0
for i in arr:
    if i==target:
        count+=1
print(count)
#################
# while
arr=[10,20,30,40,50,50,50,50,50]
target=50
count=0
i=0
while i<len(arr):
    if arr[i]==target:
        count+=1
    i+=1
print(count)
#################COUNT EVEN NUMBERS
arr=[10,21,30,45,50,67,89,90,60,36]
for i in range(len(arr)):
    if arr[i]%2==0:
        print(arr[i])

############333 in while
arr=[10,21,30,45,50,67,89,90,60,36]
i=0
while i<len(arr):
    if arr[i]%2==0:
        print(arr[i])
    i+=1
#################33 odd  numbers
arr=[10,21,30,45,50,67,89,90,60,36]
for i in range(len(arr)):
    if arr[i]%2!=0:
        print(arr[i])
##############
arr=[10,21,30,45,50,67,89,90,60,36]
i=0
while i<len(arr):
    if arr[i]%2!=0:
        print(arr[i])
    i+=1
######333 count even numbvers
arr=[10,21,30,45,50,67,89,90,60,36]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
print(count)
#################33 WHILE
arr=[10,21,30,45,50,67,89,90,60,36]
i=0
count=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    i+=1
print(count)

##################COUNT ODD NUMBERS EVEN/ODD
arr=[10,21,30,45,50,67,89,90,60,36]
count=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        count+=1
print(count)
####################333
arr=[10,21,30,45,50,67,89,90,60,36]
i=0
count=0
while i<len(arr):
    if arr[i]%2!=0:
        count+=1
    i+=1
print(count)
#################
# COUNT POSITIVE NUMBERS AND COUNT NEGETIVE NUMBERS
arr=[10,-5,20,-8,30,-2]
positive=0
negetive=0
for i in range(len(arr)):
    if arr[i]>0:
        positive+=1
    elif arr[i]<0:
        negetive+=1
print("positive=",positive)
print("negetive",negetive)
#######################################
arr=[10,-5,20,-8,30,-2]
positive=0
negetive=0
i=0
while i<len(arr):
    if arr[i]>0:
        positive+=1
    elif arr[i]<0:
        negetive+=1
    i+=1
print("positive=",positive)
print("negetive=",negetive)

########3 FIND INDEX
arr=[10,20,30,40,50,60]
target=60
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
############# 
arr=[10,20,30,40,50,60]
i=0
target=60
while i<len(arr):
    if arr[i]==target:
        print(i)
    i+=1
#######################33
# COUNT MULTIPLES OF 5
arr=[10,12,15,18,20,25]
count=0
for i in range(len(arr)):
    if arr[i]%5==0:
        count+=1
print(count)
####################################
arr=[10,12,15,18,20,25]
i=0
count=0
while i<len(arr):
    if arr[i]%5==0:
        count+=1
    i+=1
print(count)

############################
#SUM OF EVEN NUMBERS
arr=[1,2,3,4,5]
sum=0
for i in range(len(arr)):
    if i%2==0:
        sum+=i
print(sum)
##########################3 while
arr=[1,2,3,4,5]
i=0
sum=0
while i<len(arr):
    if arr[i]%2==0:
        sum+=arr[i]
    i+=1
print(sum)

#############ODD
arr=[1,2,3,4,5]
sum=0
for i in arr:
    if i%2!=0:
        sum+=i
print(sum)
############### while
arr=[1,2,3,4,5]
sum=0
i=0
while i<len(arr):
    if arr[i]%2!=0:
        sum+=arr[i]
    i+=1
print(sum)
# FIND LARGEST EVEN NUMBER
arr=[10,20,30,40,50,60,70]
largest=arr[0]
for i in arr:
    if i%2==0:
        if i>largest:
            largest=i
            print(largest)

###########3 odd numbers
arr=[10,20,30,40,50,99,100,110,120]
largest=arr[0]
for i in arr:
    if i%2!=0:
        if i>largest:
            largest=i
        print(largest)      
#####################
# in while 
arr=[10,20,30,40,50,99,100,110,120]
i=0
largest=arr[0]
while i<len(arr):
    if arr[i]%2==0 and arr[i]>largest:
        largest=arr[i]
    i+=1
    print(largest)

##########################################
# remove duplicate values
arr=[1,2,2,3,4,4,4,5,1]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
##############arr=[1,2,2,3,4,4,4,5,1]#33
# while 
arr=[1,2,2,3,4,4,4,5,1]
i=0
result=[]
while i<len(arr):
    if arr[i] not in result:
        result.append(arr[i])
    i+=1
print(result)
################
# frequency
arr=[1,2,2,3,4,4,4,5,1]
result={}
count=0
for i in arr:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)
############################
arr=[10,10,20,10,10,30,10,10]
target=10
count=0
for i in arr:
    if i==target:
        count+=1
print(count)
###########
arr=[10,20,30,40,50]
for i in arr:
    print(i,end=" ")
############
arr=[11,22,33,44,55,66]
for i in arr:
    if i%2==0:
        print(i)
############
arr=[11,22,33,44,55,66]
for i in arr:
    if i%2!=0:
        print(i)
###########
arr=[2,7,4,9,10]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
#################3
arr=[1,3,6,8,11]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)
#####################33
arr=[10,20,30]
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)
################3
arr=[15,88,20,66]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
###########3
arr=[4,5,6,7]
count=0
for i in arr:
    count+=1
print(count)
############################3
# second largest
arr=[10,50,20,40]
largest=0
for i in arr:
    if i>largest:
        largest=i
print('largest=',largest)
secondlargest=arr[0]
for i in arr:
    if i!=largest and i>secondlargest:
        secondlargest=i
print("secondlargest=",secondlargest)
###################################################333
arr=[5,10,80,20,3]
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print("smallest=",smallest)
secondsmallest=arr[0]
for i in arr:
    if i<secondsmallest and i!=smallest:
        secondsmallest=i
print("secondsmallest=",secondsmallest)
#######################33
arr=[1,2,2,3,1,4]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
#######################333
arr=[1,2,1,3,2,1]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)