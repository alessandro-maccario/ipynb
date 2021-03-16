import pandas as pd



### Question 1
###
### Read all input files and put the data in a single dataframe with an additional field year.
### Notice that the column names are not the same in all input files.

db_2015 = pd.read_csv("2015.csv", sep=";")
db_2016 = pd.read_csv("2016.csv", sep=";")
db_2017 = pd.read_csv("2017.csv", sep=";")

print(db_2015)