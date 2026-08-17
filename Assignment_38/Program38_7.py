import pandas as pd
import matplotlib.pyplot as plt

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

plt.boxplot(df["Attendance"])

plt.title("Box plot of attendance")
plt.ylabel("Study Hours")

plt.show()