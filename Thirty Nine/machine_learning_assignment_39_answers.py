"""
Marvellous Infosystems - Machine Learning Assignment 39
Student Performance ML - Decision Tree Classification

Required CSV: student_performance_ml.csv
Columns: StudyHours, Attendance, PreviousScore,
         AssignmentsCompleted, SleepHours, FinalResult
FinalResult: 1=Pass, 0=Fail
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ============================================================
# COMMON SETUP
# ============================================================
FILE_NAME = "student_performance_ml.csv"

df = pd.read_csv(FILE_NAME)

features = [
    "StudyHours", "Attendance", "PreviousScore",
    "AssignmentsCompleted", "SleepHours"
]
target = "FinalResult"

required = features + [target]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

X = df[features]
y = df[target]

# The assignment does not specify a split ratio.
# We use a standard 80/20 stratified split.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# ============================================================
# QUESTION 1
# Import DecisionTreeClassifier, create model and train it.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 1 - DECISION TREE TRAINING")
print("=" * 70)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("Decision Tree model trained successfully.")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# ============================================================
# QUESTION 2
# Predict X_test and display predicted and actual values.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 2 - PREDICTION")
print("=" * 70)

y_pred = model.predict(X_test)

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})
print(comparison.to_string(index=False))

# ============================================================
# QUESTION 3
# Calculate accuracy using accuracy_score.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 3 - ACCURACY")
print("=" * 70)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print(f"Accuracy Percentage: {accuracy * 100:.2f}%")

# ============================================================
# QUESTION 4
# Generate confusion matrix using ConfusionMatrixDisplay.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 4 - CONFUSION MATRIX")
print("=" * 70)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

print("\nAssuming Pass (1) is the positive class:")
print("True Positive (TP): Actual Pass and predicted Pass.")
print("True Negative (TN): Actual Fail and predicted Fail.")
print("False Positive (FP): Actual Fail but predicted Pass.")
print("False Negative (FN): Actual Pass but predicted Fail.")

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail (0)", "Pass (1)"]
)
disp.plot()
plt.title("Student Performance - Confusion Matrix")
plt.tight_layout()
plt.show()

# ============================================================
# QUESTION 5
# Calculate training and testing accuracy and comment.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 5 - TRAINING VS TESTING ACCURACY")
print("=" * 70)

train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, y_pred)

print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy : {test_accuracy:.4f}")

if train_accuracy == 1.0 and test_accuracy < 1.0:
    print("Observation: Strong evidence of overfitting.")
elif train_accuracy > test_accuracy + 0.10:
    print("Observation: Possible overfitting.")
elif train_accuracy < 0.70 and test_accuracy < 0.70:
    print("Observation: Possible underfitting.")
else:
    print("Observation: No strong evidence of severe overfitting/underfitting.")

# ============================================================
# QUESTION 6
# Compare max_depth = 1, 3, None.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 6 - DECISION TREE DEPTH COMPARISON")
print("=" * 70)

depth_results = []

for depth in [1, 3, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    pred = tree.predict(X_test)
    acc = accuracy_score(y_test, pred)
    depth_results.append([depth, acc, acc * 100])

depth_df = pd.DataFrame(
    depth_results,
    columns=["max_depth", "testing_accuracy", "testing_accuracy_percent"]
)
print(depth_df.to_string(index=False))

best = depth_df.loc[depth_df["testing_accuracy"].idxmax()]
print(
    f"\nBest testing accuracy in this split: max_depth={best['max_depth']} "
    f"({best['testing_accuracy_percent']:.2f}%)"
)
print("Observation: A shallow tree can underfit; an unrestricted tree can "
      "fit training data closely and may overfit.")

# ============================================================
# QUESTION 7
# Predict the specified new student.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 7 - NEW STUDENT PREDICTION")
print("=" * 70)

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

new_pred = model.predict(new_student[features])[0]
label = "Pass" if new_pred == 1 else "Fail"

print(new_student.to_string(index=False))
print(f"Predicted FinalResult: {new_pred}")
print(f"Prediction: {label}")

# ============================================================
# QUESTION 8
# Single structured program: loading, analysis, visualization,
# split, training, prediction, accuracy, confusion matrix,
# and final conclusion.
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 8 - COMPLETE STRUCTURED PROGRAM")
print("=" * 70)

# 1. Dataset loading
print("\n1. Dataset Loading")
print("Shape:", df.shape)

# 2. Data analysis
print("\n2. Data Analysis")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nStatistical summary:")
print(df.describe())

# 3. Visualization
print("\n3. Visualization")
df[features].hist(figsize=(12, 8))
plt.suptitle("Student Performance Feature Distributions")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
df[target].value_counts().sort_index().plot(kind="bar")
plt.xlabel("FinalResult (0=Fail, 1=Pass)")
plt.ylabel("Number of Students")
plt.title("Final Result Distribution")
plt.tight_layout()
plt.show()

# 4. Train-test split
print("\n4. Train-Test Split")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 5. Model training
print("\n5. Model Training")
print("Decision Tree model trained.")

# 6. Prediction
print("\n6. Prediction")
print("Test predictions:", y_pred)

# 7. Accuracy calculation
print("\n7. Accuracy Calculation")
print(f"Testing Accuracy: {accuracy * 100:.2f}%")

# 8. Confusion matrix
print("\n8. Confusion Matrix")
print(cm)

# 9. Final conclusion
print("\n9. Final Conclusion")
if test_accuracy >= 0.80:
    print("The Decision Tree achieved good testing performance.")
else:
    print("Testing performance is below 80%; model tuning or another "
          "algorithm may be considered.")

print("\nAssignment 39 completed.")
