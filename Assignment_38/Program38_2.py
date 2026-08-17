# 2. Write a program to:
# • Display total number of students in the dataset
# • Count how many students Passed (FinalResult = 1)
# • Count how many students Failed (FinalResult = 0)

import pandas as pd

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

rows, columns = df.shape
#len(df)
print(f"Total number of students : ", rows)

print("Number of passed students : ", (df["FinalResult"] == 1).sum())
print("Number of failed students : ", (df["FinalResult"] == 0).sum())