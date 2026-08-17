import pandas as pd
import matplotlib.pyplot as plt

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

plt.hist(df["StudyHours"], color = "yellow", edgecolor = "black")

plt.title("Student result distribution")
plt.xlabel("Study hours")
plt.ylabel("Number of students")
plt.show()

"""
The study hours are fairly spread between 1-2 hours to 8.5 hours.
Most students study for 2, 6 and 8 hours.
"""