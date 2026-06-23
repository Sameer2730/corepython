list1=[1,2,3,4,5,6]
list1.insert(4,10)
print(list1)
##################
list2=[1,2,3,4,5]
list2.remove(3)
print(list2)
##########
l1=[1,2,3,4,5]
l1.pop(4)
print(l1)
#################
# sort 
l1=[1,5,7,9,2,4,5]
l1.sort()
print(l1)
####################
l1=[1,2,3,4,5]
l1.reverse()
print(l1)
##############################
arr=[1,2,3,4,5,6,7]
result=[]
for i in range(len(arr)-1,-1,-1):
    result.append(arr[i])
print(result,end=" ")
#######################################333
arr=[1,2,3,4,5,6,7]
result=[]
i=len(arr)-1
while i>=0:
    result.append(arr[i])
    i-=1
print(result)
#######################33
arr=[10,20,30,40,50]
result=[]
for i in range(len(arr)-1,-1,-1):
    result.append(arr[i])
print(result)
##################33 in while
arr=[10,20,30,40,50]
result=[]
i=len(arr)-1
while i>=0:
    result.append(arr[i])
    i-=1
print(result)
###################################
# sum of list of elements
arr=[5,10,15,20]
sum=0
for i in arr:
    sum+=i
print(sum)
############################
arr=[5,10,15,20]
sum=0
i=0
while i<len(arr):
    sum+=arr[i]
    i+=1
print(sum)
########################################
arr=[2,5,8,11,14,17,20]
for i in arr:
    if i%2==0:
        print(i)
####################3
arr=[2,5,8,11,14,17,20]
i=0
while i<len(arr):
    if arr[i]%2==0:
        print(arr[i])
    i+=1
#####################33
arr=[3,6,9,12,15,18,21]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
print(count)
#####################33
arr=[3,6,9,12,15,18,21]
count=0
i=0
while i<len(arr):
    if arr[i]%2==0:
        count+=1
    print(count)
    i+=1
a=[7,2,15,9,21,4,18]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
########################3
ararr=[7,2,15,9,21,4,18]
largest=arr[0]
i=0
while i<len(arr):
    if arr[i]>largest:
        largest=arr[i]
    i+=1
print(largest)
############
arr=[12,5,18,3,27,9,1,14]
smallest=arr[0]
for i in arr:
    if i<=smallest:
        smallest=i
print(smallest)
############
arr=[12,5,18,3,27,9,1,14]
smallest=arr[0]
i=0
while i<len(arr):
    if arr[i]<smallest:
        smallest=arr[i]
    i+=1
print(smallest)
###############
# 7)sum of even numbers
arr=[4,7,2,9,6,11,8]
sum=0
for i in range(len(arr)):
    if arr[i]%2==0:
        sum+=arr[i]
print(sum)
###############################333
arr=[4,7,2,9,6,11,8]
sum=0
i=0
while i<len(arr):
    if arr[i]%2==0:
        sum+=arr[i]
    i+=1
print(sum)
# 8)count odd numbers
arr=[4,7,2,9,6,11,8]
sum=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        sum+=arr[i]
print(sum)
###############################333
arr=[4,7,2,9,6,11,8]
sum=0
i=1
while i<len(arr):
    if arr[i]%2!=0:
        sum+=arr[i]
    i+=1
print(sum)
################################3
# SQUARES OF EACGH NUMBER
arr=[2,4,6,8,10]
for i in arr:
    print(i*i,end=" ")
# in while
arr=[2,4,6,8,10]
i=0
while i<len(arr):
    print(arr[i]*arr[i],end=" ")
    i+=1

print("######################################")
############
arr=[1,2,3,4,5]
result=[]
for i in range(len(arr)):
    result.append(arr[i])
print(result)
#########################
arr=[1,2,3,4,5]
result=[]
i=0
while i<len(arr):
    result.append(arr[i])
    i+=1
print(result)
##########33
arr=[1,2,3,4,5]
rev=[]
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev)
#############
arr=[1,2,3,4,5]
rev=[]
i=len(arr)-1
while i>=0:
    rev.append(arr[i])
    i-=1
print(rev)
#####################
arr=[1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)
###############################
# frequency
arr=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
###############3
name="sameer"
freq={}
for i in name:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
#################################
arr=[1,2,2,3,3,3,4,4,5,5]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
maximumvalue=0
answer=0
for i in arr:
    if freq[i]>maximumvalue:
        maximumvalue=freq[i]
        answer=i
print(answer)
#################333
arr=[10,20,30,40,50]
for i in arr:
    print(i,end=" ")
############### sum of aray elements
arr=[10,20,30,40,50]
sum=0
for i in arr:
    sum+=i
print(sum)
##########################33
arr=[5,2,9,1,7]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
#########################3
arr=[5,2,9,1,7]
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print(smallest)
########################33
arr=[10,20,30,40,50]
count=0
for i in arr:
    count+=1
print(count)
##################3
arr=[1,2,3,4,5,6]
for i in arr:
    if i%2==0:
        print(i,end=" ")
######################################33333
arr=[1,2,3,4,5,6]
for i in arr:
    if i%2!=0:
        print(i,end=" ")
#########################################
arr=[1,2,3,4,5,6,7,8]
result=[]
for i in range(len(arr)-1,-1,-1):
    result.append(arr[i])
print(result)
########################333
# average
arr=[10,20,30,40,50]
sum=0
for i in arr:
    sum+=i
average=sum/len(arr)
print(average)
##################################3
arr=[1,-1,2,3,-4,5,-6,-7]
count=0
for i in arr:
    if i<0:
        count+=1
print(count)
##########################3
arr=[1,2,3,4,5,6]
print(arr[0])
################
arr=[1,2,3,4,5,6]
print(arr[-1])