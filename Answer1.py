import pandas as pd

df = pd.read_excel(r"data.xlsx", sheet_name="Class Participation")
filtered_df = df.loc[(df["PollParticipation"] == "Yes") & (df["DoubtAsked"] == "No")]
filtered_df = df.loc[(df["PollParticipation"] == "Yes") & (df["DoubtAsked"] == "No")]
# print(filtered_df.head(5))
counts = filtered_df["QuestionsAnswered"].value_counts()
print('Total students who participated in Poll and didn\'t ask doubt:', (counts["Yes"] + counts["No"]))
print('Total students with correct answer in poll and didn\'t ask doubt:',counts["Yes"])
print('Total students with incorrect answer in poll and didn\'t ask doubt:',counts["No"])
prob = (counts["Yes"] / (counts["Yes"] + counts["No"])) * 100
print('Probablity of getting an answer:',prob)
