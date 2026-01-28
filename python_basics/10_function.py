### Function ###

def my_function ():
    print("This is a functions")

my_function()
my_function()
my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(5234235, 7235235)
sum_two_values("5", "7")#Problema del tipado dinamico
sum_two_values(5.3, 7)

def sum_two_values_with_return(first_number, second_number):
    return(first_number + second_number)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Ortega", name = "Pablo")

def print_name2 (name, surname, alias = "Sin Alias"): #Value by default
    print(f"{name} {surname} y mi alias es: {alias}")

print_name2(surname = "Ortega", name = "Pablo")
print_name2(surname = "Ortega", name = "Pablo", alias = "Mojo")

def print_texts (*text):
    print(text)

print_texts("Hi!", "bye", 15446, 32468823, 'goodbye')
print_texts('2')

