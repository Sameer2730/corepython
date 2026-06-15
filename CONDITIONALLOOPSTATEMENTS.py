values = "12345"
# print(list(values))
# print(tuple(values))

v = [(1,2,3),4,5,6,[7,8,9],10] #[[1,2,3],4,5,6,[7,8,9],10]
# v[4] = tuple(v[4])
v = tuple(v)
v[4] = tuple(v[4])
print(v)
# v = list(v)
# v[0] = list(v[0])
# v[4] = list(v[4])
# print(v)
# v[0] = list(v[0])
# v(0) = tuple(v(0))
# print(v)
