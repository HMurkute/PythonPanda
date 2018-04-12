# In this we create a html file from csv file using pandas module
# I downloaded a random csv file from internet to use here
import pandas as pd
# By using below function we are accessing csv file located on my local computer.
country = pd.read_csv('C:\\Users\\lenovo\\Downloads\\mock.csv', index_col=0) # Here index_col=0 means to doesn't have any indexes

country.to_html('mock.html') # Here we created a mock.html file from csv file above by using this function.
