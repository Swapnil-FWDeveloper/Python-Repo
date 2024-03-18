# Data Frames

import pandas as pd
data = {"Name" :["Swapnil","Shende"],
        "Age":[21,21],
        "Gender":["Male","Male"]
       }
df=pd.DataFrame(data)
print(df) 

# so here we have created data frames 
# remember DataFrame is imp for creating DataFrames


# data=pd.read_csv("") Add the csv file location and remove \ to / or else if file present in folder write the name of file only for CSV 

# for excel
data=pd.read_excel("insurance.xlsx")
print(data)






# Exploring Data in Pandas
import pandas as pd
data=pd.read_excel("insurance.xlsx")
# print(data)

# so in this data we are having 1000 of data but we dont know what is data missing 
# like any cell value or extra cells in a row's of colums so not we will clean the data

# let say want to see starting 10 data
# print(data.head(10))
# print(data.tail(10)) #see ending 10 data

# If want to check the data type of each 
print(data.info())
# it will give total column and rows
# like if have 2 col then it will show 
# nameofcol with its data and memory space 









import pandas as pd
data=pd.read_excel("insurance.xlsx")
print(data.describe())






import pandas as pd
data=pd.read_excel("insurance.xlsx")
print(data.isnull().sum())

# it will find all the null value of the data and tell you how much is the null value in which col or row