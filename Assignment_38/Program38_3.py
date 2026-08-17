import pandas as pd

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

print("Average Study hours are : ", df["StudyHours"].mean())
print("Average attendance is : ", df["Attendance"].mean())
print("Maximmum PreviousScore is : ", df["PreviousScore"].max())
print("Minimum SleepHours are : ", df["SleepHours"].min())