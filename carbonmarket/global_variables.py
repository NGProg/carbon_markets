import pandas as pd

# class variables :
#     def __init__ (self):
#         global data

data = pd.read_csv('carbonmarket/carbonmarket.csv', header=0, parse_dates=[1], index_col=1)
del data['Unnamed: 0']
df = data.interpolate()