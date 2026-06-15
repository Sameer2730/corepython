# tup= (1,2,4,[10,20],4,5)
# #
 
# # print(tup)
# l = []
# for i in tup:
#     if i not in l:
#         l.append(i)
# print(tuple(l))



# o/p [1,2,4,[10,20],4,5]
# result=list(tup)
# print(result)
# result=list(tup)
# print(result)
# result=tup[3]
# print(result)
# result=list(tup)
# result[3] = tuple(result[3])
# result=tuple(result)
# result=list(result)
# result=tup(result)
# print(result)


# result[3] = tuple(result[3])
# result=tuple(result)


# ([1,2],4,[10,20],[4,5])
# result=[]
# for i in tup:
# name="i love python programming language"
# # count=name.split()
# print(len(count))
# result=name.strip()
# print(len(name))
# replace vowels in a String
# name="sameer"
# result=" "
# for ch in name:
#     if ch in "aeiou":
#         result+="*"
#     else:
#         result+=ch
#         print(result)
# # count digits in a string
# name="sameer12345"
# count=0
# for ch in name:
#     if ch.isalnum():
#         count+=1
# print(count)
# #count special characters
# name="sameer@$"
# count=0
# for ch in name:
#     if not ch.isalnum() and ch!="":
#         count+=1
# print(count)
# #check wheather a strin g contains only alphabets
# name="sameer"
# count=0
# for ch in name:
#     if ch.isalpha():
#         count+=1
# print(count)
# # check string contains only digits
# name="123456789"
# count=0
# for i in name:
#     if i.isdigit():
#         count+=1
# print(count)
# BASIC STRING PROBLEMS
# 1)REVERSE A STRING
# 2)CHECK PALINDROME STRING
# 3)COUNT VOWELS IN STRING
# 4)COUNT CONSONENTS IN STRINGS
# 5)COUNT DIGITS IN A STRING
# 6)COUNT SPACES IN A STRING
# 7)FIND LENGTH OF STRING 
# 8)CONVERT UPPERCASE TTO LOWER CASE
# 9)CONVERT LOWER CASE TO UPPER CASE
# 10) REMOVE DUPLICATE CHARACTERS IN STRINg
#  1)REVERSE A STRING
#############################################################################
###############################################################33
##########################################################3
#################################################
#STRING PROBLEMS START
name="sameer"
reverse=name[::-1]
print(reverse)

##########################3
name="madam"
reverse=name[::-1]
if name==reverse:
    print("palindrome")
else:
    print("not a paliondrome")
#####################
ch="sameer"
count=0
for ch in ch:
    if ch in "aeiouAEIOU":
        count+=1
        print(ch,count)
######################################
ch="sameer"
count=0
for ch in name:
    if ch not in "aeiouAEIOU":
        count+=1
        print(ch,count)
#################################
name="sameer123"
count=0
for ch in name:
    if ch.isdigit():
        count+=1
print(count)
########################################
name="i like python"
count=0
for ch in name:
    if ch==" ":
        count+=1
print(count)
############################################
name="sameer"
count=0
for ch in name:
    count+=1
print(count)
###################################33
name="sameer"
result=name.upper()
print(result)
#remove duplicate characyers in a string
name="sameerrrrrrrrr"
result=""
for ch in name:
    if ch not in result:
        result+=ch

#find longest word
name="i like python"
words=name.split()
longest=max(words,key=len)
print("longest word is =",longest)
#shortest word 
name="i like python"
word=name.split()
smallest=min(words,key=len)
print("smallest word is",smallest)
# replace vowels
name="sameer"
result=""
for ch in name:
    if ch.lower() in "aeiou":
        result+="*"
    else:
        result+=ch
print(result)
#count uppercase letters
name="sameerSAM"
count=0
for ch in name:
    if ch.isupper():
        count+=1
print(count)
##############lower case leters
name="sameerSAMEER"
count=0
for ch in name:
    if ch.islower():
        count+=1
print(count)
# count digits
name="sameer123"
count=0
for ch in name:
    if ch.isdigit():
        count+=1
print(count)
############3count special characters
name="sameer@#$" 
count=0
for ch in name:
        if not ch.isalnum() and ch!=" ":
            count+=1
print(count)
# count spaces
name="i like python" 
count=0
for ch in name:
    if ch==" ":
        count+=1
print(count)
# remove duplicate chaeracters
name="programming"
result=""
for ch in name:
    if ch not in result:
        result+=ch
print(result)
# check substring
name="python programming"
sub="programming"
if sub in name:
    print("found")
else:
    print("not found")
# first non repeating characters
name="sameer"
for ch in name:
    if name.count(ch)==1:
        print(ch)
# first repeating chaeracters
name="sameer"
for ch in name:
    if name.count(ch)>1:
        print(ch)
# remove all digits
name="sameer123"
for ch in name:
    if ch.isalpha():
        print(ch)
        ##############################################################################################
        ###################################################################################################
        ###############################################################################################3
        #############################################################################################333
        ###########################################################################################
#LIST PROBLENMS START
# 1)find largest element
lst=[10,20,5,40,30]
largest=lst[0]
for num in lst:
    if num>largest:
        largest=num
print(largest)
# 2)smallest
lst=[10,20,5,40,30]
smallest=lst[0]
for num in lst:
    if num<smallest:
        smallest=num
print(smallest)

lst=[1,2,3]
lst.append(4)
print(lst)
lst=[1,2]
lst.extend([3,4])
print(lst)
lst=[1,3]
lst.insert(1,2)
lst.insert(3,4)
print(lst)
lst=[1,2,3]
lst.remove(3)
print(lst)
lst=[20,10,30,40]
lst.sort()
print(lst)
lst=[1,2,3]
result=lst[::-1]
print(result)
n=10
for i in range(1,n):
    print(i)
############
num=10
for i in range(1,101):
    if i %2==0:
        print(i)
num=10
for i in range(1,100):
    if i%2!=0:
        print(i)
num=5
for i in range(1,11):
    print(num,"x",i,"=",num*i)
print(result)
# sum of natural numbrs
n=5
total=0
for i in range(1,num+1):
    total+=i
print(total)
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
#squares from 1 to n
num=3
for i in range(1,num+1):
    print(i*i)
# cubes
num=3
for i in range(1,num+1):
    print(i**3)
# count digits in a number
number=5
count=0
for i in range(1,num+1):
