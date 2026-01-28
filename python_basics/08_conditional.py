### Conditional ###

my_condition = True

if my_condition:
    print ("im here!")


my_condition = False

if my_condition:
    print("im here")

print("im out")

my_condition2 = 5*3

if my_condition2 == 10:
    print("im here")

my_condition2 = 0   

if my_condition2 >= 10 and my_condition2 <= 20:
    print("my_condition is 10 and  <= 20")
elif my_condition2 <= 10 and my_condition2 >= 5:
    print("my_condition2 between 5 and 10")
elif my_condition2 == 0 or my_condition2 == 1:
    print("my_condition es 1")
else:
    print("my_condition It does not meet the requirements.")