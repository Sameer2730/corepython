# 
# prime nos
# number=8
# count=0
# for i in range(1,number+1):
#     if number%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")
# arr=[10,20,30,40,50,99,100,110,120]
# i=0
# largest=arr[0]
# while i<len(arr):
#     if arr[i]%2==0:
#         if arr[i]>largest:
#             largest=arr[i]
#         i+=1
#         print(largest)
        
arr=[10,20,30,40,50,99,100,110,120]
i=0
largest=arr[0]
while i<len(arr):
    if arr[i]%2==0 and arr[i]>largest:
            largest=arr[i]
    i+=1
    print(largest)
        