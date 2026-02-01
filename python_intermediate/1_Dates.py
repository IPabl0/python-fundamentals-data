### DATES ###

from datetime import datetime

now = datetime.now()

def print_date (date):
    print (date.year)
    print (date.month)
    print (date.day)
    print (date.hour)
    print (date.minute)
    print (date.second)
    print (date.timestamp)

print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)
print ('\n')

#Representacion de un momento justo de mas facil manejo
# Formato posixks??? formato standar
timestamp = now.timestamp()
print (timestamp)
print ('\n')

print ('Defining Date group date and time')
year_2024 = datetime(2024,7,9,9,51,43)
print (year_2024)
print ('\n')

from datetime import time
#Sirve para encapsular tiempo
current_time = time(21, 6, 2)
print ('Current Time group only the hour part')
print (current_time.hour)
print (current_time.minute)
print (current_time.second)
print ('\n')

from datetime import date

#definir date
current_date = date (1988, 7, 9)
print ('Current Date group only the dates')
print (current_date.year)
print (current_date.month)
print (current_date.day)
print ('\n')

#definir date para fecha actual
current_date = date.today()
print ('Current Date group only the dates')
print (current_date.year)
print (current_date.month)
print (current_date.day)
print ('\n')

print ('Operaciones')
#current_date = date(current_date.year, current_date.month + 1, current_date.day)
print ('Mostrar mes siguiente')
print (current_date.month)
print ('\n')

diff = year_2024 - now
print (diff)

from datetime import timedelta
#work with time intervals
start_init_timedelta = timedelta(200, 100, 100, weeks=10)
end_init_timedelta = timedelta(300, 100, 100, weeks=14)
print(end_init_timedelta - start_init_timedelta)
print(end_init_timedelta + start_init_timedelta)
# Add 5 days to the current date
five_days_later = current_date + timedelta(days=5)
print('Current date plus 5 days:')
print(five_days_later)

# Subtract 3 weeks from the current date
three_weeks_ago = current_date - timedelta(weeks=3)
print('Current date minus 3 weeks:')
print(three_weeks_ago)





