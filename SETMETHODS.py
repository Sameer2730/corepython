#  set add method
print('this is a *set* add method')
numbers={1,2,3}
numbers.add(4)
print(numbers)
print('#################################################################################')
# set add string methods
print("this is set string method")
names={"sameer","nazeer","pandu"}
names.add("arsha")
print(names)
print('######################################################################')

#------------------------------------------------------------------------------------------
#remove method
print('this is a *set* remove method')
fruits={"orange","grapes","pineapple"}
fruits.remove("orange")
print(fruits)
print('#################################################################################')




#-------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#clear method
print('this is a *set* clear method')
data={10,20,30}
data.clear()
print(data)
print('######################################################################################')




#union method
print('this is a *set* union method')
a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print('####################################################################################')




#intersection method
print('this is a *set* intersection method')
x={1,2,3}
y={2,3,4}
print(x.intersection(y))
print('#####################################################################################')



#pop method
print('this is a *set* pop method')
colors={"red","blue","yiolet"}
x=colors.pop()
print(x)
print(colors)
print('#######################################################################################')
# remove
print("this is a remove method")
a={1,2,3,4}
a.remove(3)
print(a)
print('#############################################################################')
# set difference
a={1,2,3}
b={2}
print(a.difference(b))
print('###############################################################################################')
# same method
a={1,2,3,4}
b={3,4,5,6}
print(a.difference(b))
print('#############################################################################################33')
# symmetric difference
a={1,2,3,4}
b={3,4,5,6}
print(a.symmetric_difference(b))
print('##############################################################################################3')