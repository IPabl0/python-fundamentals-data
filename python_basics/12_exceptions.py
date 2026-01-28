### Exceptions Handling ###

number_one = 5
number_two = 1
number_two = "1"

#try except
try:
    print(number_one + number_two)
    print('No Errors')
except:
    print("Error")


#try except else
try:
    print(number_one + number_two)
    print('No Errors')
except:
    print("Error")
else: #opcional
    #execute if not exception 
    print("program continue nothing exception")
finally: #opcional
    #execute always
    print("program continue")

#Exception for type
try:
    print(number_one + number_two)
    print('No Errors')
except ValueError:
    print("this is a ValueError")
except TypeError:
    print("this is a TypeError")

#Capture info exception
try:
    print(number_one + number_two)
    print('No Errors')
except TypeError as e:
    print("ERROR ERROR ERROR ERROR ERROR")
    print(f"this is a TypeError: {e}")
except Exception as e:
    print("ERROR ERROR ERROR ERROR ERROR")
    print(f"Huston we have a problem: {e}")


