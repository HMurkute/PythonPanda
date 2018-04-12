import pandas as pd
# We first see the operation by which we can perform merging of two dataframes.

df1 = pd.DataFrame({'HPI':[80, 90, 70, 60],'Int_Rate':[2, 1, 2, 3],'Ind_Gdp':[50, 45, 65, 23]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80, 90, 70, 60],'Int_Rate':[2, 1, 2, 3],'Ind_Gdp':[50, 45, 65, 23]},
                   index = [2001, 2002, 2003, 2004])

merge = pd.merge(df1,df2, on = 'HPI') # This command merges the above dataframes.

print(merge) # This command prints the merge variable which holds the merged dataframe.



