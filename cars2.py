import pandas as pd
cars = pd.read_csv('cars.csv')
x = cars.iloc[0:5,1:10]
a = x.drop(columns = ['cyl','hp','wt','vs'])
b = cars.iloc[0,0]
c = cars.iloc[23,2]
d = cars.loc[[1, 18, 28],['cyl','gear']]