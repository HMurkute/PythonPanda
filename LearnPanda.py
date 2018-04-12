import pandas as pd

XYZ_web = {'Days': [1, 2, 3, 4, 5, 6],
           'Visitors':[1000, 2090, 4987, 7652, 2873, 6539],
           'Bounce_Rate':[29, 17, 56, 23, 18, 10]}

df = pd.DataFrame(XYZ_web)

print(df)

print(df.head(2)) # It prints only the first two rows of the dataframe.
print(df.tail(2)) # It prints the last two rows of the dataframe.


