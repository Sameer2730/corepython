# arr=[10,20,30,40,50]
# for i in arr:
#     print(i,end=" ")
# #########################
# arr=[10,20,30,40,50]
# for i in range(1,5,2):
#     print(arr[i])
# ####################3333
# arr=[10,20,30,40,50]
# largest=arr[0]
# for i in arr:
#     if i>largest:
#         largest=i
# print(largest)
# ################################33
# arr=[10,20,30,40,50]
# sum=0
# for i in arr:
#     sum+=i
#     print(sum)
# print(sum)
# arr=[10,20,30,40,50]
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i],end="  ")
# ########################3333
# nums=[1,2,3,2,4,2]
# freq={}
# target=2
# for i in nums:
#     if i in freq:
#             freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)
# ########################
# #####################################333
# ###################################################33

# arr=[10,20,30,40,50,60,70]
# for i in range(0,len(arr),2):
#      print(arr[i])
# arr=[10,20,10,30,10,40]
# arr2=[50,60,20,30]
# for i in arr:
#      if i in arr2:
#           print(i)
# ############################################3
# arr=[10,20,10,30,10,40]
# result=set()
# for i in arr:
#      result.add(i)
# print(result)
# ##########################3333

# i=10
# while i<21:
#      print(i)
#      i+=1
# ######################3333
# arr=[10,22,33,45,46,57,66,78,99]
# even=[]
# odd=[]
# for i in arr:
#      if i%2==0:
#           even.append(i)
#      else:
#           odd.append(i)
# print("even =",even)
# print("odd =",odd)

# ######################333
# arr=[10,20,30,40,50,60,70]
# for i in range(1,len(arr),2):
#      print(arr[i])

# #####################33
# arr=[10,11,22,33,44,55,66,77,88,99,102]
# for i in range(0,len(arr),2):
#     print(arr[i])
#     ############################################################33
# # \####################################################/
# # ##
# arr=[10,20,30,40,50,60,70]
# for i in range(0,7,2):
#      print(arr[i])
# ################################3
# arr=[10,11,22,33,44,55,66,77,88,99,102]
# for i in range(len(arr)):
#     if arr[i]%2!=0:
#          print(arr[i])
# #######################333
# arr=[10,20,10,30,10,40]
# result=list()
# for i in arr:
#      result.append(i)
# print(result)

# ###########################################
# # arr=[10,22,33,45,46,57,66,78,99]
# # even=[]
# # odd=[]
# # for i in arr:
# #      if i%2==0:
# #           even.append(i)
# #      else:
# #           odd.append(i)
# # print("even=",even)
# print("odd=",odd)
#######################3
# arr=[10,20,10,30,10,40]
# arr2=[50,60,20,30]
# result=[]
# for i in arr:
#      if i in arr2:
#           result.append(i)
# print(result)
#################33
nums=[1,2,3,2,4,2]
freq={}
for i in nums:
     if i in freq:
          freq[i]+=1
     else:
          freq[i]=1
print(freq)
############################33
arr=[10,11,12,13,14]
even=0
odd=0
for i in arr:
     if i%2==0:
          even+=1
     else:
          odd+=1
print(even)
print(odd)
###########################3333
arr=[1,2,2,3,4,4,5]
result=[]
for i in arr:
     if i not in result:
          result.append(i)
print(result)
##########################33
arr=[10,20,30,40]
result=[]
for i in range(len(arr)-1,-1,-1):
     result.append(arr[i])
print(result)
###################################################3
arr=[10,20,30,40,50]
for i in range(0,len(arr),2):
     print(arr[i])

#####################3
arr=[1,2,2,3,3,3]
freq={}
for i in arr:
     if i in freq:
          freq[i]+=1
     else:
          freq[i]=1
print(freq)
################
arr=[1,2,3,4]
for i in arr:
     print(i*i,end=" ")
####################33333
i=0
while i<=11:
     print(i)
     i+=1
#############################3
i=0
while i<21:
     if i%2==0:
          print(i)
     i+=1
######################
arr=[10,20,30]
for i in range(len(arr)):
     print(i,arr[i])
##############3
arr=[10,25,30,15,40]
for i in arr:
     if i>20:
          print(i)
#############3
arr=[1,2,3,4,5,6]
sum=0
for i in range(len(arr)):
     if arr[i]%2==0:
          sum+=arr[i]
print(sum)
######################333
arr=[3,6,7,9,10,12]
count=0
for i in range(len(arr)):
     if arr[i]%3==0:
          count+=1
print(count)
###################333
arr=[10,20,30,40,50,60]
for i in range(0,len(arr),2):
     print(arr[i])
########################3
arr=[8,3,9,1,6]
print(arr[-2])
##############################3
arr=[1,2,3,4,5]
for i in range(len(arr)-1,-1,-1):
     print(arr[i],end=" ")
#############
arr=[1,2,3,4,5]
i=len(arr)-1
while i>0:
     print(arr[i])
     i-=1
#################################33
arr=[1,2,2,3]
for i in arr:
     if arr.count(i)==1:
          print(i)
#################################33
arr=[10,20,30]
for i in range(len(arr)):
     print(i,arr[i])
############33
name="hello"
print(name[::-1])