empty_element_tuple= ()
single_element_tuple=("Alex",)
mixed_tuple = (1,"Hello Python",3.14,True)

print(mixed_tuple[0])
print(mixed_tuple[-1])

tuple1 =(1,2,3)

tuple2 =(4,5,6)

combined = tuple1 + tuple2

print(combined)

repeated = tuple1 * 4  # This should be tuple1, not tuple
print(repeated)


sliced = combined[1:5]
print(sliced)


a,b,c = tuple1
print(a,b,c)


print(tuple1.count(2))
print(tuple1.index(3))




