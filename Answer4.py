import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r"data.xlsx", sheet_name="Class Attendance")
df["day_of_week"] = df["ClassDate"].dt.strftime("%A")
total_rows = df.shape[0]
print("Best Day to take the class as per attandance:")
print(df["day_of_week"].value_counts())

df["JTime"] = pd.to_datetime(df["JoinTime"], format="%H:%M")
df["LTime"] = pd.to_datetime(df["LeaveTime"], format="%H:%M")
# print(df['ClassDate'].value_counts())

# Calculting time consumed.
df["Time Consumed"] = (df["LTime"] - df["JTime"]).dt.total_seconds() / 60

# group by the hour and minute of the JoinTime column
gb = df.groupby([df["JTime"].dt.hour, df["JTime"].dt.minute])

# calculate the mean time consumed for each group
mean_time_consumed = gb["Time Consumed"].mean()
# find the group with the maximum mean time consumed
best_time = mean_time_consumed.idxmax()
# print the best time to take the class
print("The best time to take the class is at {}:{}".format(best_time[0], best_time[1]))
mean_time_consumed.plot(kind="line")
# set the x-axis label
plt.xlabel("Join time")
# set the y-axis label
plt.ylabel("Mean time consumed (minutes)")
# set the plot title
plt.title("Mean time consumed by join time")
# display the plot
plt.show()
