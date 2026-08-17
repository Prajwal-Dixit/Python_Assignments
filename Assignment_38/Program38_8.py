# Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

plt.bar(df["AssignmentsCompleted"], df["FinalResult"],color = "skyblue")

plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.show()

"""
Observation: 
Students who completed 5 or more assignments are passed
and other sudents have failed in the exam
"""