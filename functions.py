import pandas as pd
import matplotlib.pyplot as plt

filename = "API_SI.POV.DDAY_DS2_en_csv_v2_10474275.csv"

df = pd.read_csv(filename, header=2)
df.drop([0,1])

# creating series for arg, ivo and usa
arg = df.iloc[7, :]
arg = arg.dropna()
arg = arg[4:]

ivo = df.iloc[39, :]
ivo = ivo.dropna()
ivo = ivo[4:]

usa = df.iloc[249, :]
usa = usa.dropna()
usa = usa[4:]

# creating dict of series
my_dict = {'ARG': arg, 'IVO': ivo, 'USA': usa}

# creating dataframe from dict
my_df = pd.DataFrame(my_dict)
# filling the missing values with the mean value for each country
my_df = my_df.fillna(my_df.mean())

print(my_df)

my_df.plot()

