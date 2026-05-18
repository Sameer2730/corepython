#get method
print('this is a *dictionary* get method')
student={"name":"sameer", "age":21, "city":"machilipatnam","studying": "btech final year"}
result=student.get("name")
print (result)
print('##################################################################################')
#items method
print('this is a *dictionary* items method')
car={"brand":"BMW", "year":2026}
result=car.items()
print(result)
print('##################################################################################')
#update method
print('this is a *dictionary* update method')
person={"name":"john","age":25}
person.update({"city":"hyderabad"})
print(person)
print('###############################################################################')
#delete method
print('this is a *dictionary* delete method')
employeee={"name":"sameer","salary":50000}
del employeee["salary"]
print("employeee")
print('##################################################################################')
#copy method
print('this is a *dictionary* copy method')
original={"name":"sameer","age":20}
new_data=original.copy()
print(new_data)
print('##########################################################################3')