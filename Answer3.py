import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel(r"data.xlsx", sheet_name="Grades")
total_rows = df.shape[0]
info_dict = {}
roll_numbers = []
performance = []
inc=[]
dec=[]
cons=[]
df_result = pd.DataFrame()

for i in range(total_rows):
    roll_no = df.loc[i, "RollNo"]
    marks = df.loc[i, "Test1":"Test10"]
    tests = [
        "Test 1",
        "Test 2",
        "Test 3",
        "Test 4",
        "Test 5",
        "Test 6",
        "Test 7",
        "Test 8",
        "Test 9",
        "Test 10",
    ]
    row_slice = df.loc[i, "Test1":"Test10"]
    mean = row_slice.mean()
    std = round(row_slice.std(ddof=0), 2)
    z = round((row_slice - mean) / std, 2)
    marks_filtered = []
    tests_filtered = []
    # print(' ')
    for j, k, l in zip(marks.to_list(), z, tests):
        # print(j,k,l)
        if k > 1.2 or k < -1.2:
            pass
        else:
            tests_filtered.append(l)
            marks_filtered.append(j)
    z = z.to_list()
    plt.bar(tests_filtered, marks_filtered)
    z = np.polyfit(range(len(tests_filtered)), marks_filtered, 1)
    p = np.poly1d(z)
    slope = p.coeffs[0]
    # print(slope)
    if slope < -0.5:
        result = "Decreasing"
        dec.append(roll_no)
    elif slope > 0.4:
        result = "increasing"
        inc.append(roll_no)
    else:
        result = "Consistant"
        cons.append(roll_no)
    performance.append(result)
    plt.plot(tests_filtered, p(range(len(tests_filtered))), "r--")
    # plt.show()

df_result["RollNo"] = df["RollNo"]
df_result["Overall Performance"] = performance

print(df_result["Overall Performance"].value_counts())
# print(inc,dec,cons)
print('Increaing performance:',inc)
print('Decreaing performance:',dec)
print('Consistant performance:',cons)
