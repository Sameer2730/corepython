arr=[10,20,30,40,50]
for i in arr:
    print(i,end=" ")
#########################
arr=[10,20,30,40,50]
for i in range(1,5,2):
    print(arr[i])
####################3333
arr=[10,20,30,40,50]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
################################33
arr=[10,20,30,40,50]
sum=0
for i in arr:
    sum+=i
    print(sum)
print(sum)
arr=[10,20,30,40,50]
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end="  ")
########################3333
nums=[1,2,3,2,4,2]
freq={}
target=2
for i in nums:
    if i in freq:
            freq[i]+=1
    else:
        freq[i]=1
print(freq)
########################
#####################################333
###################################################33

arr=[10,20,30,40,50,60,70]
for i in range(0,len(arr),2):
     print(arr[i])
arr=[10,20,10,30,10,40]
arr2=[50,60,20,30]
for i in arr:
     if i in arr2:
          print(i)
############################################3
arr=[10,20,10,30,10,40]
result=set()
for i in arr:
     result.add(i)
print(result)
##########################3333

i=10
while i<21:
     print(i)
     i+=1
######################3333
arr=[10,22,33,45,46,57,66,78,99]
even=[]
odd=[]
for i in arr:
     if i%2==0:
          even.append(i)
     else:
          odd.append(i)
print("even =",even)
print("odd =",odd)

######################333
arr=[10,20,30,40,50,60,70]
for i in range(1,len(arr),2):
     print(arr[i])

#####################33
arr=[10,11,22,33,44,55,66,77,88,99,102]
for i in range(0,len(arr),2):
    print(arr[i])