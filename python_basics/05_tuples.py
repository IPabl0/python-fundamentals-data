###Tuples###

my_tuple = tuple ()
my_other_tuple = ()

my_tuple = (35, 1.88, 'Pablo', 'Ortega')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

#print(my_tuple[-5]) INDEX ERROR
#print(my_tuple[4])  INDEX ERROR

print(my_tuple.count('Pablo'))
print(my_tuple.index('Pablo'))

#my_tuple[1] = 1.90 TUPLE IS IMMUTABLE
print(my_tuple)

my_other_tuple = (12,13,12,44,67,77)

my_concat_tuple = my_tuple + my_other_tuple
print(my_concat_tuple)

print(my_concat_tuple[5:9])

my_tuple = list(my_tuple)
print(type(my_tuple))
print(my_tuple)

my_tuple[3] = 'Maipu'
my_tuple.insert(3, 'El Abrazo')
my_tuple.insert(3, 'Ortega')


my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

my_other_tuple2 = my_tuple

#del destroy variable
del my_tuple
#del my_tuple[2] 'tuple' object doesn't support item deletion
#print(my_tuple) name 'my_tuple' is not defined

my_tuple = my_other_tuple2
print(my_tuple)


