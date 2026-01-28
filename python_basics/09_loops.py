### Loops ####

my_list = [35, 12, 544, 65, 31, 12]
my_tupla = ('Pablo', 'Ortega', 35, 1988)
my_set = {'Santiago','Maipu', 'Villa el Abrazo', 16544}
my_dict = {'Comuna':'Maipu', 'Ciudad':'Santiago', 'Zip':9280287}

my_condition = 0

#While

while my_condition <= 10:
    print(my_condition)
    my_condition += 1
else: #its optional
    print('The value > 10')

print('Program continue')

#For
for element in my_list, my_tupla, my_set, my_dict.values():
    print(element)

