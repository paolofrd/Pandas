import pandas as pd
cars = pd.read_csv('cars.csv')
car = cars.loc[0:4]
carr = car.append(cars.loc[27:31])