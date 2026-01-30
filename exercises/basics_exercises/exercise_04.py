list_temperatures_celsius = [36.6, 37.0, 38.5, 39.2, 40.0]
list_temperatures_fahrenheit = [] 
print("Temperatures in Celsius: \n", list_temperatures_celsius)
for temp_celsius in list_temperatures_celsius:
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    list_temperatures_fahrenheit.append(f"{temp_fahrenheit:.2f}")

print("\nTemperatures in Fahrenheit: \n", list_temperatures_fahrenheit)
