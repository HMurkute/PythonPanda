# In this we cover concatenation.
import pandas as pd

df1 = pd.DataFrame({'HPI':[78, 35, 48, 71], 'Int_Rate':[2, 3, 4, 5],
                    'US_GST':[34, 29, 38, 47]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[78, 35, 48, 71], 'Int_Rate':[2, 3, 4, 5],
                    'US_GST':[34, 29, 38, 47]},
                   index = [2005, 2006, 2007, 2008])

Concat = pd.concat([df1,df2]) # This syntax does the concatenation of df1 and df2. Concat is variable name.

print(Concat)

