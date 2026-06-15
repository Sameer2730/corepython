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
print('##############################################################################################')




# s={10,20,10,20,30,40}
# result=s.split()

# print(result)
# name={"sameeer,reemas", [1,2]}
# name.set(name)
# print(name)
# # name={"sameer","reemas"}
# name=tuple(name)
# print(name)
name=[0,20,30,40,{20,30,40,50,}]
user_input = int(input('give your value only below 100:'))
print(user_input)
name[4] = list(name[4])
if user_input <= 100 and user_input>=1:
    name[4][1] = user_input
    name[3]=400
    name[4] = set(name[4])
    print(name)
else:
    print('only above 100 and zero also not accepts')

#[0,20,30,40,{20,20,40,50,100,200}]