### Dictionary ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name":"Pablo", "Surname":"Ortega", "Age":35, 1:"Python"}

my_dict ={
    "Name":"Pablo",
    "Surname":"Ortega",
    "Age":35,
    "Language":{"Python", "c#", "c++", "Java"},
    1: 1.85
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Name"])

my_dict["Name"] = "Antonio"
print(my_dict["Name"])

print(my_dict[1])

my_dict["Street"] = "Fidias"
print(my_dict)

del my_dict["Street"]
print(my_dict)

#Search on key not valor
print ("Pablo" in my_dict)
print ("Name" in my_dict)

print(my_dict.items())
print("\n")
print(my_dict.keys())
print("\n")
print(my_dict.values())
print("\n")

#create a new dict with key other dict 
#in this case of my_dict for late add values
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

#Transform
print(tuple(my_dict))
print(list(my_dict.values()))

print("\n")




