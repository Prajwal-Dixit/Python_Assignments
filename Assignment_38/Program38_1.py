import pandas as pd

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

print("First 5 records from the dataset are : ")
print(df.head())

print("Last 5 records from the dataset are : ")
print(df.tail())

Rows, Columns = df.shape
print("Total number of Rows are : ", Rows)
print("Total number of columns are : ", Columns)

print("Column names are : ")
print(df.columns.to_list())

print("Column datatypes are : ")
print(df.dtypes)
