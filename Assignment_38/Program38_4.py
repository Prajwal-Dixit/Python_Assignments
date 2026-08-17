import pandas as pd

datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

#Value_counts counts the total values associated with different labels(0 & 1 in this case) and returs like [1:18, 0:12]
result = df["FinalResult"].value_counts(normalize=True) * 100       #normalize returns proportion ex [1:0.60, 0:0.40]

print(f"Pass : {result[1]} %")                    # 1 means Passed in the dataset, so for result[1],
print(f"Fail : {result[0]} %")                    # it fetches result associated with 1. Its not related to index

# Conclusion : The dataset is slightly imbalanced as pass and fail percentages are 60/40.
#              It would be balanced if it was 50/50
           