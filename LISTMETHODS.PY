#append string
print('This is a *append* list Built in function')
fruits= ["apple","banana"]
fruits.append("mango")
print(fruits)
print(len(fruits))
print('######################################')
#--------------------------------------------------------------------------------------------------
#2append number
numbers=[10,20,30,40]
numbers.append(50)
print(numbers)
print('###############################################################################')
#3append bool
data=[True,False]
data.append(True)
print(data)
print('######################################################################################')
#4append float
numbers=[10.5,15.5,30.5]
numbers.append(50.5)
print(numbers)
print('###############################################################################')
#5append username
students=["sameer","nazeer"]
new_student="kiran"
students.append(new_student)
print(students)
print('#####################################################################################')
#6 append inside loop
numbers=[]
for i in range(2,6):
    numbers.append(i)
print(numbers)
print('####################################################################################')
#
#------------------------------------------

#insert
numbers=[10,20,30,40]
numbers.insert(4,50)
print(numbers)
print('##################################################################################')
#2 insert at last position
name=["sameer","nazeer"]
name.insert(2,"pandu")
print(name)
#3 insert at middle position
numbers=[10,20,40,50,60]
numbers.insert(2,30)
print(numbers)
print('######################################################################')
#4 insert using negetive indexing
numbers=['a','b','d']
numbers.insert(-1,'c')
print(numbers)
print('##################################################################################')
#5 


#---------------------------------------------------
#remove
colors=["red","blue","green"]
colors.remove("blue")
print(colors)
print(len(colors))

#----------------------------------------------------
#pop
marks=[50,60,70,80]
marks.pop(1)
print(marks)
print(marks[1])

#------------------------------------------------------
#sort
data=[90,20,70,10]
data.sort()
print(data)
print(data[0])
print('######################################################################3')
#desending order
name=[90,450,50,20]
name.sort(reverse=True)
print(name)
print('#####################################################################')
#--------------------------------------------------------
#reverse
nums=[1,2,3,4]
nums.reverse()
print(nums)
print(nums[0])
print('############################################################################33')
#---------------------------------------------------------------
#count
items=[1,2,2,3,2]
x=items.count(2)
print(x)
print(items)
print('#################################################################################')

#---------------------------------------------------------------
#index
cars=["bmw","audi","tesla"]
x=cars.index("tesla")
print(x)
print(cars[x])
############################################################################################
#------------------------------------------------------------------------------------------------