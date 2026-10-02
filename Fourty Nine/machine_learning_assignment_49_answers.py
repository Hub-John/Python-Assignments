"""
Machine Learning Assignment 49
Marvellous Infosystems : Python - Automation & Machine Learning

All questions are answered in the same Question -> Answer sequence as
the assignment PDF.
"""

# ============================================================
# Q1. Write a Python program that calculates the mean of a dataset
# using NumPy for the following values:
# [6, 7, 8, 9, 10, 11, 12]
# ============================================================
print("""
Q1. Write a Python program that calculates the mean of a dataset using
NumPy for the following values:
[6, 7, 8, 9, 10, 11, 12]

Answer:
The mean is the sum of all values divided by the number of values.

Mean = (6 + 7 + 8 + 9 + 10 + 11 + 12) / 7
     = 9
""")

import numpy as np

values = np.array([6, 7, 8, 9, 10, 11, 12])
mean_value = np.mean(values)

print("Dataset:", values)
print("Mean:", mean_value)


# ============================================================
# Q2. Write a Python program that calculates the variance and
# standard deviation of the dataset:
# [6, 7, 8, 9, 10, 11, 12]
# Display both results.
# ============================================================
print("""
Q2. Write a Python program that calculates the variance and standard
deviation of the dataset:
[6, 7, 8, 9, 10, 11, 12]

Answer:
Variance measures the average squared deviation from the mean.
Standard deviation is the square root of the variance.

Using NumPy's default population formulas:
    Variance = 4
    Standard Deviation = 2
""")

variance = np.var(values)
standard_deviation = np.std(values)

print("Variance:", variance)
print("Standard Deviation:", standard_deviation)


# ============================================================
# Q3. Write a Python program using StandardScaler to perform
# feature scaling on:
# [[25,20000],
#  [30,40000],
#  [35,80000]]
# Print the scaled dataset.
# ============================================================
print("""
Q3. Write a Python program using StandardScaler to perform feature
scaling on:
[[25,20000],
 [30,40000],
 [35,80000]]

Answer:
StandardScaler standardizes each feature independently using:

    z = (x - mean) / standard deviation

The columns are therefore converted to comparable standardized scales.
""")

from sklearn.preprocessing import StandardScaler

data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
], dtype=float)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("Original dataset:")
print(data)

print("\nScaled dataset:")
print(scaled_data)


# ============================================================
# Q4. Write a Python program to calculate the Euclidean distance
# between two points before and after applying feature scaling,
# and explain the difference in results.
# ============================================================
print("""
Q4. Write a Python program to calculate the Euclidean distance between
two points before and after applying feature scaling, and explain the
difference in results.

Answer:
The Euclidean distance between two points is:

    d = sqrt((x2-x1)^2 + (y2-y1)^2)

The assignment does not specify which two points to use, so this
solution uses the first two rows of the given dataset:

    Point 1 = [25, 20000]
    Point 2 = [30, 40000]

Before scaling, the second feature has much larger numerical values and
therefore dominates the distance.

After scaling, both features are expressed in standardized units, so
the large numerical magnitude of the second feature no longer dominates
the calculation.
""")

point_1 = data[0]
point_2 = data[1]

distance_before = np.linalg.norm(point_2 - point_1)

scaled_point_1 = scaled_data[0]
scaled_point_2 = scaled_data[1]

distance_after = np.linalg.norm(scaled_point_2 - scaled_point_1)

print("Point 1:", point_1)
print("Point 2:", point_2)
print("Euclidean distance before scaling:", distance_before)
print("Euclidean distance after scaling :", distance_after)


# ============================================================
# Q5. Explain the concept of a classification report in machine
# learning. Why is it used and what type of models require it?
# ============================================================
print("""
Q5. Explain the concept of a classification report in machine learning.
Why is it used and what type of models require it?

Answer:
A classification report is a summary of important evaluation metrics
for a classification model. It commonly contains precision, recall,
F1-score, support, and accuracy.

It is used to understand how well a model predicts each class, rather
than relying only on overall accuracy.

Classification reports are used for classification models whose target
contains discrete class labels.

Examples:
- Logistic Regression classifier
- Decision Tree classifier
- Random Forest classifier
- K-Nearest Neighbors classifier
- Support Vector Machine classifier
- Neural-network classifiers

They are not the standard evaluation report for continuous-value
regression problems.
""")


# ============================================================
# Q6. In a classification report, explain:
# Precision, Recall, F1 Score, Support, Accuracy
# ============================================================
print("""
Q6. In a classification report, explain the following metrics:
Precision
Recall
F1 Score
Support
Accuracy

Answer:

1. Precision:
   Precision tells us how many samples predicted as a class were
   actually members of that class.

       Precision = TP / (TP + FP)

2. Recall:
   Recall tells us how many actual positive samples were correctly
   identified.

       Recall = TP / (TP + FN)

3. F1 Score:
   F1-score is the harmonic mean of precision and recall.

       F1 = 2 * Precision * Recall / (Precision + Recall)

4. Support:
   Support is the number of actual samples belonging to each class.

5. Accuracy:
   Accuracy is the proportion of all predictions that are correct.

       Accuracy = (TP + TN) / (TP + TN + FP + FN)
""")


# ============================================================
# Q7. Consider:
# Actual    = [1,1,1,1,0,0,0,0]
# Predicted = [1,1,0,1,0,1,0,0]
#
# Determine TP, TN, FP, FN.
# ============================================================
print("""
Q7. Consider the following data:

Actual Values    = [1, 1, 1, 1, 0, 0, 0, 0]
Predicted Values = [1, 1, 0, 1, 0, 1, 0, 0]

Determine:
True Positive (TP)
True Negative (TN)
False Positive (FP)
False Negative (FN)

Answer:

Compare the actual and predicted values one by one:

1. 1 -> 1 : TP
2. 1 -> 1 : TP
3. 1 -> 0 : FN
4. 1 -> 1 : TP
5. 0 -> 0 : TN
6. 0 -> 1 : FP
7. 0 -> 0 : TN
8. 0 -> 0 : TN

Therefore:
    TP = 3
    TN = 3
    FP = 1
    FN = 1
""")

actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

tp = int(np.sum((actual == 1) & (predicted == 1)))
tn = int(np.sum((actual == 0) & (predicted == 0)))
fp = int(np.sum((actual == 0) & (predicted == 1)))
fn = int(np.sum((actual == 1) & (predicted == 0)))

print("TP:", tp)
print("TN:", tn)
print("FP:", fp)
print("FN:", fn)


# ============================================================
# Q8. Write a Python program that calculates TP, TN, FP, FN
# for the given arrays. Display all four values.
# ============================================================
print("""
Q8. Write a Python program that calculates TP, TN, FP, FN for:

actual    = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

Display all four values.

Answer:
The program below calculates each value by comparing the actual and
predicted labels.

Result:
    TP = 3
    TN = 3
    FP = 1
    FN = 1
""")

actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

tp = int(np.sum((actual == 1) & (predicted == 1)))
tn = int(np.sum((actual == 0) & (predicted == 0)))
fp = int(np.sum((actual == 0) & (predicted == 1)))
fn = int(np.sum((actual == 1) & (predicted == 0)))

print("True Positive (TP):", tp)
print("True Negative (TN):", tn)
print("False Positive (FP):", fp)
print("False Negative (FN):", fn)


# ============================================================
# Q9. Write a Python program using scikit-learn to generate a
# classification report for the given data.
# ============================================================
print("""
Q9. Write a Python program using scikit-learn to generate a
classification report for:

actual    = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

Display the complete classification report including precision,
recall, F1-score, and support.

Answer:
classification_report() from sklearn.metrics generates precision,
recall, F1-score, support, accuracy, and the macro/weighted averages.
""")

from sklearn.metrics import classification_report

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

report = classification_report(
    actual,
    predicted,
    labels=[0, 1],
    target_names=["Class 0", "Class 1"],
    zero_division=0
)

print("Complete Classification Report:")
print(report)


print("""
============================================================
ASSIGNMENT 49 COMPLETED
============================================================
All 9 questions are answered in Question -> Answer sequence.
============================================================
""")
