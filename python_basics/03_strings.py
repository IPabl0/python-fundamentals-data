#Strings text in python

#Single quotation marks or double quotation marks work in the same way.
my_string = "this is a string text random"
my_other_string = 'This is a string text that used single quotation marks'

#Size string
print (len(my_string))
print (len(my_other_string))

#join string
print(my_string + " + " + my_other_string)

#Special character
my_string_new_line = "This is a new String\nwhit a newline"
print(my_string_new_line)
my_tab_string = "\tThis is string whit tab"
print(my_tab_string)

#Format
name, surname, age = 'Pablo', 'Ortega', 35
print("My name is {} {} y mi edad es: {}".format(name, surname, age))
#The safest way
print("My name is %s %s y mi edad es: %d"%(name,surname, age))
#Whit data inference best way
print(f"My name is {name} {surname} and my age is: {age}")

#Character unpacking
language = "Python"
a, b, c, d, e, f = language
print(c)
print(f)

#Slice
language_slice = language[1:3]
print(language_slice)
print("\n")
language_slice = language[1:]
print(language_slice)
print("\n")
language_slice = language[-2]
print(language_slice)

#Reverse
language_slice = language[::-1]
print(language_slice)

#Some function  system
print(language.capitalize())
print(language.count('P'))
print(language.upper())
print(language.lower())
print(language.isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))




