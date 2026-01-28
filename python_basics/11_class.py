### Class ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Non alias'):
        #self.name = name
        #self.surname = surname
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name #private property
        self.__surname = surname
    
    def get_name (self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} it's walking")


my_person = Person("Pablo", "Ortega")
#print(f"{my_person.name} {my_person.surname}")
print(f"My name is: {my_person.full_name}")
my_person.walk()

##print(my_person.__name) Error try access private property
print(my_person.get_name()) #this form is correctly to access private property


my_other_person = Person ("Antonio","Lucero", "Mojo")
print(f"My name is: {my_other_person.full_name}")
my_other_person.walk()

my_other_person.full_name = "Hanamichi Sakuragui (king of rebound)"
print(my_other_person.full_name)
my_other_person.walk()





