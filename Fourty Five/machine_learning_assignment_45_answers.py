"""
Machine Learning Assignment 45
All questions answered in Question -> Answer sequence.

NOTE: The PDF contains the questions but no student dataset or gender
values. This program therefore expects students.csv with at least:
Name, Math, English, plus the other subject columns in your dataset.
Fill GENDER_MAP with the actual gender values before running Q2/Q3.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

INPUT_FILE = "students.csv"
OUTPUT_FILE = "final_students.csv"

df = pd.read_csv(INPUT_FILE)

required = ["Name", "Math", "English"]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError("Missing required columns: " + ", ".join(missing))

print("Original DataFrame:")
print(df)

# ============================================================
# Q1. Normalize the 'Math' scores using Min-Max scaling.
# ============================================================
scaler = MinMaxScaler()
df["Math_Normalized"] = scaler.fit_transform(df[["Math"]]).ravel()

print("\nQ1. Math after Min-Max scaling:")
print(df[["Math", "Math_Normalized"]])

# ============================================================
# Q2. Create a gender column and perform one-hot encoding.
# ============================================================
# The PDF does not provide gender values, so supply them here.
GENDER_MAP = {
    # "Sagar": "Male",
    # "Student2": "Female",
}

df["Gender"] = df["Name"].map(GENDER_MAP)

if df["Gender"].isna().any():
    print("\nWARNING: Gender is missing for:")
    print(df.loc[df["Gender"].isna(), "Name"].tolist())
    print("Fill GENDER_MAP with the correct values.")

gender_dummies = pd.get_dummies(df["Gender"], prefix="Gender", dtype=int)
df = pd.concat([df, gender_dummies], axis=1)

print("\nQ2. Gender and one-hot encoded columns:")
print(df)

# ============================================================
# Q3. Group students by gender and calculate average marks.
# ============================================================
numeric = df.select_dtypes(include="number").columns
average_columns = [
    c for c in numeric
    if c != "Math_Normalized" and not c.startswith("Gender_")
]
gender_average = df.groupby("Gender")[average_columns].mean()

print("\nQ3. Average marks by gender:")
print(gender_average)

# ============================================================
# Q4. Plot a pie chart of subject marks for 'Sagar'.
# ============================================================
if "Sagar" not in df["Name"].astype(str).values:
    raise ValueError("Student 'Sagar' is not present in students.csv.")

sagar = df[df["Name"].astype(str) == "Sagar"].iloc[0]
subject_columns = [
    c for c in df.select_dtypes(include="number").columns
    if c != "Math_Normalized" and not c.startswith("Gender_")
]
sagar_marks = sagar[subject_columns]

print("\nQ4. Sagar's subject marks:")
print(sagar_marks)

plt.figure(figsize=(7, 7))
plt.pie(sagar_marks.values, labels=sagar_marks.index, autopct="%1.1f%%")
plt.title("Subject Marks for Sagar")
plt.tight_layout()
plt.show()

# ============================================================
# Q5. Add Status: Total >= 250 -> Pass, otherwise Fail.
# ============================================================
total_columns = [
    c for c in df.select_dtypes(include="number").columns
    if c != "Math_Normalized" and not c.startswith("Gender_")
]
df["Total"] = df[total_columns].sum(axis=1)
df["Status"] = df["Total"].apply(
    lambda x: "Pass" if x >= 250 else "Fail"
)

print("\nQ5. Total and Status:")
print(df[["Name", "Total", "Status"]])

# ============================================================
# Q6. Count how many students passed.
# ============================================================
passed_count = (df["Status"] == "Pass").sum()
print("\nQ6. Number of students passed:", passed_count)

# ============================================================
# Q7. Export the final DataFrame to a CSV file.
# ============================================================
df.to_csv(OUTPUT_FILE, index=False)
print("\nQ7. Exported:", OUTPUT_FILE)

# ============================================================
# Q8. Plot a histogram of Math marks.
# ============================================================
plt.figure(figsize=(8, 5))
plt.hist(df["Math"], bins=10, edgecolor="black")
plt.xlabel("Math Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Math Marks")
plt.tight_layout()
plt.show()

# ============================================================
# Q9. Rename 'Math' column to 'Mathematics'.
# ============================================================
df.rename(columns={"Math": "Mathematics"}, inplace=True)
df.to_csv(OUTPUT_FILE, index=False)

print("\nQ9. Renamed Math -> Mathematics.")
print(df.columns.tolist())

# ============================================================
# Q10. Plot a boxplot for English marks to check distribution
#      and outliers.
# ============================================================
plt.figure(figsize=(7, 5))
plt.boxplot(df["English"].dropna())
plt.ylabel("English Marks")
plt.title("English Marks - Boxplot")
plt.tight_layout()
plt.show()

print("\nQ10. English boxplot displayed.")
print("Final DataFrame:")
print(df)
