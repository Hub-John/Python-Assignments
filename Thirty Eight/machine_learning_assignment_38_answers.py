"""
Marvellous Infosystems - Python Assignment 38
Machine Learning - Student Performance ML Dataset

Dataset required:
    student_performance_ml.csv

Expected columns:
    StudyHours
    Attendance
    PreviousScore
    AssignmentsCompleted
    SleepHours
    FinalResult

FinalResult:
    1 = Pass
    0 = Fail

This program answers Questions 1 to 10 in the same order as the assignment.
"""

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# QUESTION 1
# Load student_performance_ml.csv using pandas.
# Display first 5, last 5, shape, columns and data types.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 1 - LOAD AND EXPLORE DATASET")
print("=" * 75)

FILE_NAME = "student_performance_ml.csv"

df = pd.read_csv(FILE_NAME)

print("\nFirst 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

print("\nTotal number of rows and columns:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# ============================================================
# QUESTION 2
# Display total students, passed students and failed students.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 2 - STUDENT PASS/FAIL COUNTS")
print("=" * 75)

total_students = len(df)
passed_students = (df["FinalResult"] == 1).sum()
failed_students = (df["FinalResult"] == 0).sum()

print("Total number of students:", total_students)
print("Students Passed (FinalResult = 1):", passed_students)
print("Students Failed (FinalResult = 0):", failed_students)


# ============================================================
# QUESTION 3
# Calculate average StudyHours, average Attendance,
# maximum PreviousScore and minimum SleepHours.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 3 - STATISTICAL VALUES")
print("=" * 75)

average_study_hours = df["StudyHours"].mean()
average_attendance = df["Attendance"].mean()
maximum_previous_score = df["PreviousScore"].max()
minimum_sleep_hours = df["SleepHours"].min()

print(f"Average StudyHours: {average_study_hours:.2f}")
print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Maximum PreviousScore: {maximum_previous_score}")
print(f"Minimum SleepHours: {minimum_sleep_hours}")


# ============================================================
# QUESTION 4
# Use value_counts() to analyze FinalResult.
# Calculate Pass/Fail percentages and determine balance.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 4 - FINAL RESULT DISTRIBUTION")
print("=" * 75)

result_counts = df["FinalResult"].value_counts().sort_index()

pass_count = result_counts.get(1, 0)
fail_count = result_counts.get(0, 0)

pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print("FinalResult value_counts():")
print(df["FinalResult"].value_counts())

print(f"\nPass students: {pass_count} ({pass_percentage:.2f}%)")
print(f"Fail students: {fail_count} ({fail_percentage:.2f}%)")

# A simple practical rule: if each class is between 40% and 60%,
# call it reasonably balanced. Otherwise, call it imbalanced.
if 40 <= pass_percentage <= 60 and 40 <= fail_percentage <= 60:
    balance_answer = "The dataset is reasonably balanced."
else:
    balance_answer = "The dataset is not balanced; one class has a noticeably larger share."

print("\nAnswer:", balance_answer)
print(
    "Justification: Class balance is judged from the percentage of Pass "
    "and Fail records. A large difference between the two percentages "
    "indicates class imbalance."
)


# ============================================================
# QUESTION 5
# Analyze whether higher StudyHours increase passing chance
# and whether higher Attendance improves FinalResult.
# Write 4-5 lines of observations.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 5 - STUDY HOURS AND ATTENDANCE OBSERVATIONS")
print("=" * 75)

passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

pass_study_mean = passed["StudyHours"].mean()
fail_study_mean = failed["StudyHours"].mean()

pass_attendance_mean = passed["Attendance"].mean()
fail_attendance_mean = failed["Attendance"].mean()

study_difference = pass_study_mean - fail_study_mean
attendance_difference = pass_attendance_mean - fail_attendance_mean

if study_difference > 0:
    study_observation = (
        "1. Students who passed have a higher average StudyHours than students who failed."
    )
elif study_difference < 0:
    study_observation = (
        "1. Students who passed have a lower average StudyHours than students who failed."
    )
else:
    study_observation = (
        "1. The average StudyHours is the same for Pass and Fail groups."
    )

if attendance_difference > 0:
    attendance_observation = (
        "2. Students who passed have a higher average Attendance than students who failed."
    )
elif attendance_difference < 0:
    attendance_observation = (
        "2. Students who passed have a lower average Attendance than students who failed."
    )
else:
    attendance_observation = (
        "2. The average Attendance is the same for Pass and Fail groups."
    )

print(f"Average StudyHours - Pass: {pass_study_mean:.2f}")
print(f"Average StudyHours - Fail: {fail_study_mean:.2f}")
print(f"Average Attendance - Pass: {pass_attendance_mean:.2f}%")
print(f"Average Attendance - Fail: {fail_attendance_mean:.2f}%")

print("\nObservations:")
print(study_observation)
print(attendance_observation)
print(
    "3. A higher Pass-group average suggests a positive relationship in this dataset, "
    "but it does not by itself prove causation."
)
print(
    "4. Similarly, a higher Pass-group attendance average suggests attendance is "
    "associated with better outcomes in the dataset."
)
print(
    "5. The exact relationship should be interpreted using the complete dataset and "
    "not from a single student or a single observation."
)


# ============================================================
# QUESTION 6
# Plot histogram of StudyHours and explain distribution.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 6 - HISTOGRAM OF STUDYHOURS")
print("=" * 75)

plt.figure(figsize=(8, 5))
plt.hist(
    df["StudyHours"],
    bins=10,
    edgecolor="black"
)
plt.xlabel("StudyHours per Day")
plt.ylabel("Number of Students")
plt.title("Distribution of StudyHours")
plt.tight_layout()
plt.show()

study_min = df["StudyHours"].min()
study_max = df["StudyHours"].max()
study_median = df["StudyHours"].median()

print(f"Minimum StudyHours: {study_min}")
print(f"Median StudyHours: {study_median}")
print(f"Maximum StudyHours: {study_max}")

print(
    "\nExplanation: The histogram shows how frequently different study-hour "
    "ranges occur. The tallest bars represent the most common study-hour ranges. "
    "The overall spread shows whether students have similar or widely varying "
    "study habits."
)


# ============================================================
# QUESTION 7
# Scatter plot StudyHours vs PreviousScore.
# Use different colors for Pass and Fail students.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 7 - STUDYHOURS VS PREVIOUSSCORE")
print("=" * 75)

plt.figure(figsize=(8, 5))

pass_data = df[df["FinalResult"] == 1]
fail_data = df[df["FinalResult"] == 0]

plt.scatter(
    pass_data["StudyHours"],
    pass_data["PreviousScore"],
    label="Pass",
    alpha=0.7
)

plt.scatter(
    fail_data["StudyHours"],
    fail_data["PreviousScore"],
    label="Fail",
    alpha=0.7
)

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(
    "Observation: The scatter plot compares study time and previous examination "
    "score while visually separating Pass and Fail students. Clustering of Pass "
    "points at higher study hours/scores would suggest a positive association, "
    "but the plot should be interpreted from the actual distribution."
)


# ============================================================
# QUESTION 8
# Draw a boxplot for Attendance and identify outliers.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 8 - ATTENDANCE BOXPLOT AND OUTLIERS")
print("=" * 75)

plt.figure(figsize=(7, 5))
plt.boxplot(
    df["Attendance"].dropna(),
    vert=True
)
plt.ylabel("Attendance (%)")
plt.title("Boxplot of Attendance")
plt.tight_layout()
plt.show()

# IQR method for identifying outliers.
q1 = df["Attendance"].quantile(0.25)
q3 = df["Attendance"].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

attendance_outliers = df[
    (df["Attendance"] < lower_bound) |
    (df["Attendance"] > upper_bound)
]

print(f"Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Lower outlier boundary: {lower_bound:.2f}")
print(f"Upper outlier boundary: {upper_bound:.2f}")

if attendance_outliers.empty:
    print("\nNo Attendance outliers were detected using the 1.5 × IQR rule.")
else:
    print(
        f"\n{len(attendance_outliers)} Attendance outlier(s) detected "
        "using the 1.5 × IQR rule:"
    )
    print(attendance_outliers[["Attendance", "FinalResult"]])


# ============================================================
# QUESTION 9
# Plot relationship between AssignmentsCompleted and FinalResult.
# Explain observation.
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 9 - ASSIGNMENTS COMPLETED VS FINAL RESULT")
print("=" * 75)

plt.figure(figsize=(8, 5))

plt.scatter(
    pass_data["AssignmentsCompleted"],
    pass_data["FinalResult"],
    label="Pass",
    alpha=0.7
)

plt.scatter(
    fail_data["AssignmentsCompleted"],
    fail_data["FinalResult"],
    label="Fail",
    alpha=0.7
)

plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult (0=Fail, 1=Pass)")
plt.title("AssignmentsCompleted vs FinalResult")
plt.yticks([0, 1], ["Fail", "Pass"])
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

pass_assignments_mean = pass_data["AssignmentsCompleted"].mean()
fail_assignments_mean = fail_data["AssignmentsCompleted"].mean()

print(f"Average AssignmentsCompleted - Pass: {pass_assignments_mean:.2f}")
print(f"Average AssignmentsCompleted - Fail: {fail_assignments_mean:.2f}")

if pass_assignments_mean > fail_assignments_mean:
    print(
        "Observation: Passing students complete more assignments on average. "
        "This suggests a positive association between assignment completion "
        "and FinalResult in this dataset."
    )
elif pass_assignments_mean < fail_assignments_mean:
    print(
        "Observation: Passing students complete fewer assignments on average. "
        "Therefore, the dataset does not show a positive association based on "
        "this simple group comparison."
    )
else:
    print(
        "Observation: The average number of completed assignments is the same "
        "for Pass and Fail groups."
    )

print(
    "This comparison indicates association, not proof that completing more "
    "assignments directly causes a student to pass."
)


# ============================================================
# QUESTION 10
# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success?
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 10 - SLEEPHOURS VS FINAL RESULT")
print("=" * 75)

plt.figure(figsize=(8, 5))

plt.scatter(
    pass_data["SleepHours"],
    pass_data["FinalResult"],
    label="Pass",
    alpha=0.7
)

plt.scatter(
    fail_data["SleepHours"],
    fail_data["FinalResult"],
    label="Fail",
    alpha=0.7
)

plt.xlabel("SleepHours")
plt.ylabel("FinalResult (0=Fail, 1=Pass)")
plt.title("SleepHours vs FinalResult")
plt.yticks([0, 1], ["Fail", "Pass"])
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(
    "\nAnswer: No, sleeping more does not guarantee success. SleepHours is "
    "only one factor among several factors that may influence performance. "
    "The dataset should be examined as a whole, including StudyHours, "
    "Attendance, PreviousScore and AssignmentsCompleted."
)

sleep_pass_mean = pass_data["SleepHours"].mean()
sleep_fail_mean = fail_data["SleepHours"].mean()

print(f"Average SleepHours - Pass: {sleep_pass_mean:.2f}")
print(f"Average SleepHours - Fail: {sleep_fail_mean:.2f}")

if sleep_pass_mean > sleep_fail_mean:
    print(
        "In this dataset, the Pass group sleeps more on average, but this "
        "does not mean more sleep guarantees passing."
)
elif sleep_pass_mean < sleep_fail_mean:
    print(
        "In this dataset, the Pass group sleeps less on average; therefore, "
        "more sleep clearly cannot be treated as a guarantee of success."
    )
else:
    print(
        "The two groups have the same average SleepHours, so sleep duration "
        "alone does not distinguish the outcomes."
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("ASSIGNMENT 38 COMPLETED")
print("=" * 75)
print("All 10 questions have been implemented in the required sequence.")
print("Run this file in the same folder as student_performance_ml.csv.")
