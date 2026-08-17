# Create a scatter plot of:
# StudyHours vs PreviousScore

import pandas as pd
import matplotlib.pyplot as plt

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

passed = df[df["FinalResult"] == 1]
fail = df[df["FinalResult"] == 0]

plt.scatter(passed["StudyHours"], passed["PreviousScore"], color = "green", marker = "o", label = "Pass")
plt.scatter(fail["StudyHours"], fail["PreviousScore"], color = "red", marker = "o", label = "Fail")

plt.title("Study hours vs Previous score")
plt.xlabel("Study Hours")
plt.ylabel("Previous score")
plt.legend()
plt.grid(True)

plt.show()