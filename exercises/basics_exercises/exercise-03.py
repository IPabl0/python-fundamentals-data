#Calculate average of a list of numbers
def calculate_average(list_of_numbers):
    total = sum(list_of_numbers)
    
    count = len(list_of_numbers)
    average = total / count
    return average

list_of_numbers = [82, 2, 65, 4, 50, 102, 67, 88]
total = calculate_average(list_of_numbers)
print(f"The average of the list {list_of_numbers} is: {total}")