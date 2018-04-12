import pandas as pd
# This operation joins the two dataframes.

df1 = pd.DataFrame({'Int_Rate':[2, 1, 2, 3],'Ind_Gdp':[50, 45, 65, 23]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'Low_Tier_HPI':[50, 38, 72, 82],'Umemployment':[1, 3, 5, 6]},
                   index = [2001, 2003, 2004, 2004])

joined = df1.join(df2) # This syntax joins the df1 with df2.

print(joined)
# Joining of dataframes happens by index value. It joins the value by checking the index value on both
# dataframes and giving them values. If one dataframes doesn't have one index value then the join operation
# will give the value NaN to column whose value is not present.
