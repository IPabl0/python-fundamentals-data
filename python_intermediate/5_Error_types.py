### ERROR TYPES ###

#SyntaxError
#print 'Hi! everyone' #ERROR
print ('Hi everyone')

#NameError
language = 'spanish' #Comment for error
print (language)

#indexError
my_list = ['python', 'java', 'javascript', 'c#', 'golang']
print(my_list[0])
print(my_list[-1])
#print(my_list[8]) #Uncomment for error

#ModuleNotFoundError
#import maths #Uncomment for error
import math

# AttributeError
#print(math.PI) #Uncomment for error
print(math.pi)

#KeyError
my_dict = {"Name":"Pablo", "Surname":"Ortega", "Age":35, 1:"Python"}
#print(my_dict['surname']) #Uncomment for error
print(my_dict['Surname']) 


#TypeError
# print(my_list["Name"]) #Uncomment for error
#print(my_list["0"]) #Uncomment for error
print(my_list[0]) 

#importError
#from math import PI #Uncomment for error
from math import pi


#ValueError
#my_int = int("10 Year") #Uncomment for error
my_int = int("10")
print(type(my_int))

#ZeroDivisionError
print (4/2)
#print (4/0) #Uncomment for error