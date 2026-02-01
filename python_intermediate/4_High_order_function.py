## Higher function ##

def sum_one(value):
    return value +1

def sum_five(value):
    return value +5

def sum_two_values_and_add_value(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_value(5, 2)) #Print 8

def sum_two_values_and_add_value(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one)) # 5 + 2 +2 Print 8
print(sum_two_values_and_add_value(5, 2, sum_five)) # 5 + 2 + 5 Print 12


###CLOSURES ####

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### BUILT-IN HIGHER ORDER FUNCTION ###

list_number = [2, 5, 10, 21, 3, 30]

#Map
def multiply_two(number):
    return number * 2

print (map(multiply_two, list_number)) # Print object
print (list(map(multiply_two, list_number))) # Easier to understand to human
print (list(map(lambda number: number * 2, list_number))) # Easier to understand to human

### FILTER
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(filter(filter_greater_than_ten,list_number)) #Print object
print(list(filter(filter_greater_than_ten,list_number))) 
print(list(filter(lambda number: number > 10, list_number))) 

### REDUCE
from functools import reduce

def sum_two_values (first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, list_number))
