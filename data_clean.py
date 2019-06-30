import pandas as pd

data = pd.read_csv("plane_crash_data.csv") 

#Eliminamos todas esas columnas que no nos hacen falta

data_clean = data.drop(columns= ['time', 'location', 'operator', 'flight_number', 'route',
       'aircraft_type', 'registration', 'cn_ln', 'aboard', 'fatalities',
       'ground','summary'], axis = 1)

