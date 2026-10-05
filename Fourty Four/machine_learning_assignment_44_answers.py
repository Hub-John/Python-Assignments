"""
Machine Learning Assignment 44
Marvellous Infosystems : Python - Automation & Machine Learning

All 10 questions are answered in the same Question -> Answer sequence
as given in the assignment PDF.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Q1. Create a DataFrame for student marks and print basic
#     information like shape, columns, and data types.
# ============================================================

data = {
    "Name": ["Amit", "Sagar", "Pooja"],
    "Math": [85, 90, 78],
    "Science": [92, 88, 80],
    "English": [75, 85, 82]
}

df = pd.DataFrame(data)

print("Q1. Student DataFrame")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# ============================================================
# Q2. Use the DataFrame from Q1 and print descriptive
#     statistics using .describe().
# ============================================================

print("\nQ2. Descriptive Statistics")
print(df.describe())


# ============================================================
# Q3. Add a new column 'Total' to the DataFrame as the sum
#     of all subject marks.
# ============================================================

df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

print("\nQ3. DataFrame with Total column")
print(df)


# ============================================================
# Q4. Display students who scored more than 85 in Science.
# ============================================================

science_above_85 = df[df["Science"] > 85]

print("\nQ4. Students scoring more than 85 in Science")
print(science_above_85)


# ============================================================
# Q5. Replace 'Pooja' with 'Puja' in the 'Name' column.
# ============================================================

df["Name"] = df["Name"].replace("Pooja", "Puja")

print("\nQ5. After replacing Pooja with Puja")
print(df)


# ============================================================
# Q6. Sort the DataFrame by 'Total' marks in descending order.
# ============================================================

df = df.sort_values(by="Total", ascending=False).reset_index(drop=True)

print("\nQ6. DataFrame sorted by Total in descending order")
print(df)


# ============================================================
# Q7. Create a bar plot of student names vs total marks.
# ============================================================

plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Total"])
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Student Names vs Total Marks")
plt.tight_layout()
plt.show()


# ============================================================
# Q8. Plot a line chart of marks for 'Amit' across all subjects.
# ============================================================

amit = df[df["Name"] == "Amit"].iloc[0]

subjects = ["Math", "Science", "English"]
amit_marks = [amit[subject] for subject in subjects]

plt.figure(figsize=(8, 5))
plt.plot(subjects, amit_marks, marker="o")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's Marks Across All Subjects")
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# Q9. Create a DataFrame with missing values and fill them
#     with column mean.
# ============================================================

data2 = {
    "Name": ["Amit", "Sagar", "Pooja"],
    "Math": [np.nan, 76, 88],
    "Science": [91, np.nan, 85]
}

df2 = pd.DataFrame(data2)

print("\nQ9. DataFrame before filling missing values")
print(df2)

# Fill missing numeric values using the mean of their respective
# columns.
numeric_columns = ["Math", "Science"]

for column in numeric_columns:
    df2[column] = df2[column].fillna(df2[column].mean())

print("\nQ9. DataFrame after filling missing values with column mean")
print(df2)


# ============================================================
# Q10. Drop the 'English' column from the original DataFrame.
# ============================================================

df_without_english = df.drop(columns=["English"])

print("\nQ10. DataFrame after dropping English column")
print(df_without_english)


# ============================================================
# End of Assignment 44
# ============================================================
