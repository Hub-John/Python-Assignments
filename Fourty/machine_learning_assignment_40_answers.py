"""
Marvellous Infosystems - Machine Learning Assignment 40
Student Performance ML Dataset - Decision Tree Classification

Dataset required:
    student_performance_ml.csv

Expected columns:
    StudyHours, Attendance, PreviousScore, AssignmentsCompleted,
    SleepHours, FinalResult

FinalResult:
    1 = Pass
    0 = Fail

This program answers Questions 1 to 10 in the same order as the assignment.
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ============================================================
# COMMON SETUP: LOAD DATA AND CREATE BASE DECISION TREE MODEL
# ============================================================

FILE_NAME = "student_performance_ml.csv"

df = pd.read_csv(FILE_NAME)

required_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "FinalResult",
]

missing_columns = [c for c in required_columns if c not in df.columns]
if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}. "
        f"Expected columns are: {required_columns}"
    )

features = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

X = df[features]
y = df["FinalResult"]

# Keep one fixed split for fair comparison across most questions.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
base_accuracy = accuracy_score(y_test, y_pred)


# ============================================================
# QUESTION 1
# Feature importance using model.feature_importances_
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 1: FEATURE IMPORTANCE")
print("=" * 75)

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_,
}).sort_values("Importance", ascending=False)

print(importance_df.to_string(index=False))

most_important = importance_df.iloc[0]
least_important = importance_df.iloc[-1]

print(f"\nMost important feature: {most_important['Feature']}")
print(f"Importance score: {most_important['Importance']:.6f}")

print(f"\nLeast important feature: {least_important['Feature']}")
print(f"Importance score: {least_important['Importance']:.6f}")

print(
    "\nAnswer: The feature with the highest importance score contributes "
    "the most to the Decision Tree's predictions. The feature with the "
    "lowest score contributes the least for this trained tree."
)


# ============================================================
# QUESTION 2
# Remove SleepHours and compare accuracy
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 2: REMOVE SLEEPHOURS")
print("=" * 75)

features_without_sleep = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
]

X_no_sleep = df[features_without_sleep]

X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(
    X_no_sleep,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

model_no_sleep = DecisionTreeClassifier(random_state=42)
model_no_sleep.fit(X_train_ns, y_train_ns)

pred_no_sleep = model_no_sleep.predict(X_test_ns)
accuracy_no_sleep = accuracy_score(y_test_ns, pred_no_sleep)

print(f"Previous accuracy (all features): {base_accuracy:.4f}")
print(f"New accuracy (without SleepHours): {accuracy_no_sleep:.4f}")
print(f"Accuracy change: {accuracy_no_sleep - base_accuracy:+.4f}")

if accuracy_no_sleep > base_accuracy:
    print("Conclusion: Removing SleepHours improved test accuracy.")
elif accuracy_no_sleep < base_accuracy:
    print("Conclusion: Removing SleepHours reduced test accuracy.")
else:
    print("Conclusion: Removing SleepHours did not change test accuracy.")


# ============================================================
# QUESTION 3
# Train using only StudyHours and Attendance
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 3: STUDYHOURS + ATTENDANCE ONLY")
print("=" * 75)

two_features = ["StudyHours", "Attendance"]
X_two = df[two_features]

X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(
    X_two,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

model_two = DecisionTreeClassifier(random_state=42)
model_two.fit(X_train_2, y_train_2)

pred_two = model_two.predict(X_test_2)
accuracy_two = accuracy_score(y_test_2, pred_two)

print(f"Full-feature accuracy: {base_accuracy:.4f}")
print(f"StudyHours + Attendance accuracy: {accuracy_two:.4f}")
print(f"Accuracy change: {accuracy_two - base_accuracy:+.4f}")

if accuracy_two >= base_accuracy:
    print("Conclusion: The two-feature model is still performing well relative to the full model.")
else:
    print("Conclusion: The two-feature model performs worse than the full-feature model.")


# ============================================================
# QUESTION 4
# Predict results for 5 new students
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 4: PREDICT 5 NEW STUDENTS")
print("=" * 75)

new_students = pd.DataFrame({
    "StudyHours": [2, 4, 6, 8, 3],
    "Attendance": [65, 75, 85, 95, 70],
    "PreviousScore": [48, 62, 78, 90, 55],
    "AssignmentsCompleted": [3, 5, 7, 9, 4],
    "SleepHours": [7, 6, 7, 8, 6],
})

new_predictions = model.predict(new_students[features])

new_students["PredictedResult"] = new_predictions
new_students["Prediction"] = new_students["PredictedResult"].map({
    1: "Pass",
    0: "Fail",
})

print(new_students.to_string(index=False))


# ============================================================
# QUESTION 5
# Manually calculate accuracy and verify sklearn accuracy
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 5: MANUAL ACCURACY CALCULATION")
print("=" * 75)

correct_predictions = (y_test.to_numpy() == y_pred).sum()
total_predictions = len(y_test)

manual_accuracy = correct_predictions / total_predictions

print(f"Correct predictions: {correct_predictions}")
print(f"Total test samples: {total_predictions}")
print(f"Manual accuracy: {manual_accuracy:.4f}")
print(f"sklearn accuracy_score: {base_accuracy:.4f}")

if abs(manual_accuracy - base_accuracy) < 1e-12:
    print("Verification: Manual accuracy MATCHES sklearn accuracy_score.")
else:
    print("Verification: Manual accuracy does NOT match sklearn accuracy_score.")


# ============================================================
# QUESTION 6
# Identify misclassified students
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 6: MISCLASSIFIED STUDENTS")
print("=" * 75)

# Preserve original DataFrame index so the original student rows can be shown.
test_indices = X_test.index

misclassified_mask = y_test.to_numpy() != y_pred

misclassified = df.loc[test_indices[misclassified_mask]].copy()
misclassified["PredictedResult"] = y_pred[misclassified_mask]

misclassified["ActualLabel"] = misclassified["FinalResult"].map({
    1: "Pass",
    0: "Fail",
})
misclassified["PredictedLabel"] = misclassified["PredictedResult"].map({
    1: "Pass",
    0: "Fail",
})

display_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "FinalResult",
    "PredictedResult",
    "ActualLabel",
    "PredictedLabel",
]

if len(misclassified) == 0:
    print("No students were misclassified.")
else:
    print(misclassified[display_columns].to_string())

print(f"\nNumber of misclassified students: {len(misclassified)}")

if len(misclassified) > 0:
    print(
        "\nCommon-pattern analysis: inspect StudyHours, Attendance, "
        "PreviousScore and AssignmentsCompleted in the rows above. "
        "Misclassified students may have feature combinations that overlap "
        "the decision boundaries between Pass and Fail."
    )
else:
    print("There is no misclassification pattern because all test records were correct.")


# ============================================================
# QUESTION 7
# Compare random_state = 0, 10, 42
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 7: RANDOM_STATE COMPARISON")
print("=" * 75)

random_states = [0, 10, 42]
random_state_results = []

for rs in random_states:
    X_tr, X_te, y_tr, y_te = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=rs,
        stratify=y,
    )

    rs_model = DecisionTreeClassifier(random_state=rs)
    rs_model.fit(X_tr, y_tr)

    rs_pred = rs_model.predict(X_te)
    rs_accuracy = accuracy_score(y_te, rs_pred)

    random_state_results.append({
        "random_state": rs,
        "testing_accuracy": rs_accuracy,
    })

random_state_df = pd.DataFrame(random_state_results)
print(random_state_df.to_string(index=False))

if random_state_df["testing_accuracy"].nunique() > 1:
    print(
        "\nAnswer: Yes, the result changes. Different random states can "
        "produce different train/test splits, which can change the testing accuracy."
    )
else:
    print(
        "\nAnswer: The testing accuracy is the same for these three random states "
        "on this dataset, although different splits can generally change accuracy."
    )


# ============================================================
# QUESTION 8
# Decision Tree Visualization and root node
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 8: DECISION TREE VISUALIZATION")
print("=" * 75)

root_feature_index = model.tree_.feature[0]
root_feature = (
    features[root_feature_index]
    if root_feature_index >= 0
    else "Leaf node"
)

print(f"Root node feature: {root_feature}")
print(
    "Why selected first: A Decision Tree selects the split that gives "
    "the greatest improvement in node purity (based on its splitting criterion)."
)

plt.figure(figsize=(20, 10))
plot_tree(
    model,
    feature_names=features,
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True,
)
plt.title("Decision Tree - Student Performance")
plt.tight_layout()
plt.show()


# ============================================================
# QUESTION 9
# Add PerformanceIndex and compare accuracy
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 9: PERFORMANCEINDEX")
print("=" * 75)

df_with_index = df.copy()
df_with_index["PerformanceIndex"] = (
    df_with_index["StudyHours"] * 2
    + df_with_index["Attendance"]
)

features_with_index = features + ["PerformanceIndex"]

X_index = df_with_index[features_with_index]

X_train_pi, X_test_pi, y_train_pi, y_test_pi = train_test_split(
    X_index,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

model_index = DecisionTreeClassifier(random_state=42)
model_index.fit(X_train_pi, y_train_pi)

pred_index = model_index.predict(X_test_pi)
accuracy_index = accuracy_score(y_test_pi, pred_index)

print("PerformanceIndex formula:")
print("PerformanceIndex = (StudyHours * 2) + Attendance")
print(f"\nOriginal accuracy: {base_accuracy:.4f}")
print(f"Accuracy with PerformanceIndex: {accuracy_index:.4f}")
print(f"Accuracy change: {accuracy_index - base_accuracy:+.4f}")

if accuracy_index > base_accuracy:
    print("Conclusion: Accuracy improved after adding PerformanceIndex.")
elif accuracy_index < base_accuracy:
    print("Conclusion: Accuracy decreased after adding PerformanceIndex.")
else:
    print("Conclusion: Accuracy did not change after adding PerformanceIndex.")


# ============================================================
# QUESTION 10
# max_depth = None, training and testing accuracy
# ============================================================

print("\n" + "=" * 75)
print("QUESTION 10: max_depth = None")
print("=" * 75)

unlimited_model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42,
)

unlimited_model.fit(X_train, y_train)

train_pred = unlimited_model.predict(X_train)
test_pred = unlimited_model.predict(X_test)

training_accuracy = accuracy_score(y_train, train_pred)
testing_accuracy = accuracy_score(y_test, test_pred)

print(f"Training accuracy: {training_accuracy:.4f}")
print(f"Testing accuracy: {testing_accuracy:.4f}")

if training_accuracy == 1.0 and testing_accuracy < 1.0:
    print(
        "\nExplanation: The model has learned the training data extremely well, "
        "but its performance on unseen test data is lower. This is a sign of "
        "overfitting. A fully grown Decision Tree can create very specific "
        "rules for the training records, including noise or unusual patterns, "
        "that do not generalize to new students."
    )
elif training_accuracy > testing_accuracy:
    print(
        "\nExplanation: Training accuracy is higher than testing accuracy, "
        "which can indicate some degree of overfitting. The difference should "
        "be evaluated along with the size and quality of the dataset."
    )
else:
    print(
        "\nExplanation: Training accuracy is not higher than testing accuracy "
        "in this run. The requested 100%-training-accuracy overfitting condition "
        "does not occur for this dataset/split."
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("ASSIGNMENT 40 COMPLETED")
print("=" * 75)
print("All 10 questions have been implemented in sequence.")
print("Dataset:", FILE_NAME)
print("Base Decision Tree testing accuracy:", f"{base_accuracy:.4f}")
print("Required package: pandas, matplotlib, scikit-learn")
