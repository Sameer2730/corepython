#append
print('This is a *append* list Built in function')
fruits= ["apple","banana"]
fruits.append("mango")
print(fruits)
print(len(fruits))
print('######################################')

#------------------------------------------
#insert
numbers=[10,20,40]
numbers.insert(2,30)
print(numbers)
print(numbers[2])

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

#--------------------------------------------------------
#reverse
nums=[1,2,3,4]
nums.reverse()
print(nums)
print(nums[0])

#---------------------------------------------------------------
#count
items=[1,2,2,3,2]
x=items.count(2)
print(x)
print(items)

#---------------------------------------------------------------
#index
cars=["bmw","audi","tesla"]
x=cars.index("tesla")
print(x)
print(cars[x])
