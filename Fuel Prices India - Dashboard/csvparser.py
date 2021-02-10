import pandas as pd
import numpy as np

def get_dataframe():
	petrol_data = 'data/petrol.csv'
	diesel_data = 'data/diesel.csv'

	data_list = [petrol_data, diesel_data]
	fuel_type = ['Petrol', 'Diesel']
	li = []

	for data, fuel in zip(data_list, fuel_type):
		dataframe = pd.read_csv(data)
		dataframe['fuel'] = fuel
		li.append(dataframe)

	df = pd.concat(li, axis=0, ignore_index=True)
	df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
	df.sort_values('date', inplace=True)

	diesel_city = np.sort(df.loc[df['fuel'] == 'Diesel'].city.unique())
	petrol_city = np.sort(df.loc[df['fuel'] == 'Petrol'].city.unique())
	
	return df, (diesel_city, petrol_city)