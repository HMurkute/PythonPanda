import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df = pd.DataFrame({'Day':[1, 2, 3, 4], 'Visitors':[200, 100, 321, 190], 'Bounce_rate':[23, 12, 29, 10]})

df.set_index('Day', inplace=True) # This command sets the index to Day column replacing the usual indexing which starts
# at 0.
# print(df) I put this command in comments for plotting dataframe below. For seeing the dataframe remove this from comments

# Now we plot the dataframe in graph but we have to import certain libraries like matplotlib, style

df.plot()
plt.show()

df = df.rename(columns={'Visitors':'Users'}) # This syntax changes the column name of visitors to Users in printing the
                                             # dataframe.
print(df)

