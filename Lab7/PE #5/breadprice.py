import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv('BreadReport.csv', index_col=0)
data.fillna(0, inplace=True)
data.index = data.index.astype(int)
annual_average_price = data.mean(axis=1, skipna=True)

plt.figure(figsize=(10, 6))
plt.plot(annual_average_price.index, annual_average_price.values)
plt.title('Average Price of White Bread per Pound in U.S. City Average')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()