#This project works with real data about earthquakes in Chile.
#Data source: https://www.kaggle.com/datasets/nicolasgonzalezmunoz/earthquakes-on-chile
#The program is based on searching for and displaying seismic events starting from a magnitude given by the user

#Este proyecto trabaja con data real sobre terremotos en Chile.
#Fuente de datos: https://www.kaggle.com/datasets/nicolasgonzalezmunoz/earthquakes-on-chile
# El programa se basa en buscar y mostrar los movimientos telúricos a partir de una magnitud dada por el usuario

import csv

while True:

    with open("data/seismic_data.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        user_magnitude = float(input("Enter the minimum magnitude to filter earthquakes: "))
        print(f"Earthquakes with magnitude greater than or equal to {user_magnitude}:")
        
        for row in reader:
            try:
                magnitude = float(row["Magnitude"])
                if magnitude >= user_magnitude:
                    print(f"Date: {row['Date(UTC)']}, Latitude: {row['Latitude']}, Longitude: {row['Longitude']}, Magnitude: {magnitude}")
            except ValueError:
                print(f"Invalid magnitude value in row: {row}")
                
    if input("Do you want to search again? (yes/no): ").lower() != 'yes':
        break

