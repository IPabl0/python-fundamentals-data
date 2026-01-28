###Lists###
#List != Array

#They are used to add elements.

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 12, 544, 65, 31, 12]
print(len(my_list))
print(my_list)

my_other_list = [1, 5, 32.3, 'Pablo', 'Ortega']
print(len(my_other_list))
print(type(my_other_list))
print(my_other_list)

#Access elements of a list
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[-1])

print(my_other_list.count('Pablo'))
print(my_list.count(12))

#Unpack list
#Unpacking a list must have the same number of variables as elements 
# in the list
my_other_list2 = [35, 1.85, 'Pablo', 'Ortega']
age, height, name, surname = my_other_list2
print(age)
print(height)
print(name)
print(surname)

#operation with list
my_other_list2.append('verde')
print(my_other_list2)

my_other_list2.remove('verde')
print(my_other_list2)

my_other_list2.remove(my_other_list2[-1])
print(my_other_list2)

#Keep element
my_pop_element = my_other_list2.pop(1)
print(my_other_list2)
print(my_pop_element)

#Delete element
del my_other_list2[1]
print(my_other_list2)

#Clean list
my_other_list2.clear()
print(my_other_list2)

my_other_list2 = [35, 1.85, 'Pablo', 'Ortega']
print(my_other_list2)
my_other_list2.insert(1, 1988)
print(my_other_list2)

my_other_list3 = my_other_list2.copy()
my_other_list3.append('verde')
print(my_other_list3)
my_other_list3.reverse()
print(my_other_list3)

#my_other_list4 = list()
my_other_list4 = [1,4,2,8,2,6]
print(my_other_list4)
#sort can be manipulated
my_other_list4.sort()
print(my_other_list4)

#SubList
print(my_other_list3[2:4])





