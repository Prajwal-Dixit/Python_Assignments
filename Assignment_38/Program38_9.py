# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

passed = df[df["FinalResult"] == 1]
fail = df[df["FinalResult"] == 0]

plt.scatter(passed["SleepHours"], passed["FinalResult"],color = "green", label = "Pass")
plt.scatter(fail["SleepHours"], fail["FinalResult"],color = "red", label = "Fail")

plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.legend()
plt.grid(True)
plt.show()

"""
Observation: 
More sleep indicates more chances of passing though it is observed that passed students sleep between
5 - 8 hours and some failed students also took the same sleep(6 hours).
Thus sleep alone is not the only factor by which we can determine if a student passes or fails.
"""