### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Initially, it is a dictionary.

my_other_set = {'Pablo', 'Ortega', 35, 1988}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Maipu')
print(my_other_set) #it is not an ordered structure

my_other_set.add('Maipu')
print(my_other_set) #it does not allow duplicate elements

print ('Pablo' in my_other_set) #We can perform searches
print ('pablo' in my_other_set)

my_other_set.remove('Maipu')
print(my_other_set)

my_other_set2 = {}
my_other_set2 = my_other_set.copy()

my_other_set.clear()
print(my_other_set)
print(my_other_set2)

my_other_set = my_other_set2
del my_other_set2

my_set = {'Santiago', 'Chile'}
print(my_set)

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_other_set.union({'Ingeniero Civil Informatico', 
                                           'Ingeniero Informatico'})))

my_new_set2 = {'Santiago', 'Slamdunk', 5, 6, 7}
print(my_new_set2.difference(my_set))


