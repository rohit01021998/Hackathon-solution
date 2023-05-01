import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r"data.xlsx", sheet_name="Grades")
df_result = pd.DataFrame()
total_rows = df.shape[0]
roll_number_list = []
row_average_list = []

df0 = pd.read_excel(r"data.xlsx", sheet_name="Video Consupmtion")
df0 = df0.astype(str)
df0 = df0.apply(lambda x: x.str.replace("%", ""))
row_consumption_list = []

df1 = pd.read_excel(r"data.xlsx", sheet_name="Class Participation")
df1 = df1.astype(str)
df1 = df1.apply(lambda x: x.str.replace("Yes", "1"))
df1 = df1.apply(lambda x: x.str.replace("No", "0"))
row_participation_sum_list = []

df2 = pd.read_excel(r"data.xlsx", sheet_name="Student Details")
stream_list = df2["Stream"].to_list()

df3 = pd.read_excel(r"data.xlsx", sheet_name="Class Attendance")
df3 = pd.DataFrame(df3["RollNo"].value_counts())

for i in range(total_rows):
    row_slice = df1.loc[i, "PollParticipation":"QuestionsAnswered"]
    row_slice = row_slice.astype(int)
    row_participation_sum = row_slice.sum()
    row_participation_sum_list.append(row_participation_sum)


for i in range(total_rows):
    row_slice = df0.loc[i, "Learning Video 001":"Learning Video 014"]
    row_slice = row_slice.astype(float)
    row_consumption_mean = row_slice.mean()
    row_consumption_list.append(row_consumption_mean * 100)


for i in range(total_rows):
    roll_number = df.loc[i, "RollNo"]
    row_slice = df.loc[i, "Test1":"Test10"]
    row_average = row_slice.mean()
    roll_number_list.append(roll_number)
    row_average_list.append(row_average)
    # print (roll_number,row_average)

df_result["RollNo"] = roll_number_list
df_result["Average_marks"] = row_average_list
df_result["Average_consumption"] = row_consumption_list
df_result["Participation_score"] = row_participation_sum_list
df_result["stream"] = stream_list


df_result = pd.merge(df3, df_result, on="RollNo")

science = df_result.loc[df_result["stream"] == "Science"]
commerce = df_result.loc[df_result["stream"] == "Commerce"]

science["final_score"] = (
    0.5 * science["Average_marks"]
    + 0.15 * science["Participation_score"]
    + 0.1 * science["Average_consumption"]
    + 0.25 * science["count"]
)
commerce["final_score"] = (
    0.5 * commerce["Average_marks"]
    + 0.15 * commerce["Participation_score"]
    + 0.1 * commerce["Average_consumption"]
    + 0.25 * commerce["count"]
)

df_sorted_science = science.sort_values("final_score", ascending=False)
df_sorted_commerce = commerce.sort_values("final_score", ascending=False)
df_sorted_science = df_sorted_science.rename(columns={'count': 'Attendance'})
df_sorted_commerce = df_sorted_commerce.rename(columns={'count': 'Attendance'})

print('Top 3 students in science stream')
print(df_sorted_science.head(3))
print(' ')
print('Top 3 students in commerce stream')
print(df_sorted_commerce.head(3))
