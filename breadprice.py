import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Read data from CSV file with the first row as column headers
data = pd.read_csv('BreadReport.csv', index_col=0)

# Fill NaN values with 0 or any other appropriate value
data.fillna(0, inplace=True)

# Parse the index to extract the year
data.index = data.index.astype(int)

# Calculate the annual average price
annual_average_price = data.mean(axis=1, skipna=True)

# Create a line plot of the annual average price
plt.figure(figsize=(10, 6))
plt.plot(annual_average_price.index, annual_average_price.values)
plt.title('Average Price of White Bread per Pound in U.S. City Average')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()

# Save the plot to a file named breadprice_plot.png
plt.savefig('breadprice_plot.png', dpi=300, bbox_inches='tight')
