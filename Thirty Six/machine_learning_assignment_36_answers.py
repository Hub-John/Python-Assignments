"""
Marvellous Infosystems - Machine Learning Assignment 36

All 10 questions are answered in the same sequence as the assignment.
"""

# ============================================================
# QUESTION 1
# Differentiate model.fit() and model.predict().
# ============================================================

print("""
QUESTION 1
==========

model.fit():
- Used during TRAINING.
- It gives the machine learning algorithm the training data and correct
  target values so the model can learn patterns.
- Example:
      model.fit(X_train, y_train)

model.predict():
- Used after training to make predictions for new/test input data.
- It uses the patterns learned during fit().
- Example:
      y_pred = model.predict(X_test)

In short:
fit()     -> learns from training data
predict() -> produces predictions from the learned model
""")


# ============================================================
# QUESTION 2
# Define Accuracy and give formula.
# ============================================================

print("""
QUESTION 2
==========

Accuracy is the proportion of all predictions made by a classification
model that are correct.

Formula:

Accuracy = (Number of Correct Predictions / Total Predictions) * 100

Using confusion-matrix terms:

Accuracy = (TP + TN) / (TP + TN + FP + FN) * 100

In simple words:
Accuracy tells us what percentage of the model's total predictions were
correct.
""")


# ============================================================
# QUESTION 3
# 80 correct out of 100; is high accuracy always good?
# ============================================================

print("""
QUESTION 3
==========

Given:
Correct predictions = 80
Total samples = 100

Accuracy = (80 / 100) * 100
         = 80%

Answer:
The accuracy is 80%.

Is high accuracy always good?
No. Accuracy alone may be misleading when classes are imbalanced.

Example:
If 95 out of 100 samples belong to one class, a model that always predicts
that majority class can achieve 95% accuracy while completely failing to
identify the minority class.

Therefore, depending on the problem, we should also examine metrics such
as precision, recall, F1-score and the confusion matrix.
""")


# ============================================================
# QUESTION 4
# Explain Confusion Matrix and why it is more informative than accuracy.
# ============================================================

print("""
QUESTION 4
==========

A Confusion Matrix is a table that compares the actual classes with the
classes predicted by a classification model.

For binary classification it contains:
- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

Why is it more informative than accuracy?

Accuracy gives one overall number for correct predictions. A confusion
matrix shows exactly how the model is making mistakes.

It tells us:
- How many positive cases were correctly identified.
- How many negative cases were correctly identified.
- How many negative cases were incorrectly predicted as positive.
- How many positive cases were incorrectly predicted as negative.

Thus, it helps identify the type and direction of classification errors.
""")


# ============================================================
# QUESTION 5
# Cricket vs Tennis ball classification:
# TP, TN, FP, FN.
# ============================================================

print("""
QUESTION 5
==========

For this example, consider:
Positive class = Cricket ball
Negative class = Tennis ball

True Positive (TP):
- Actual ball = Cricket
- Predicted ball = Cricket
- Meaning: A real cricket ball was correctly identified as a cricket ball.

True Negative (TN):
- Actual ball = Tennis
- Predicted ball = Tennis
- Meaning: A real tennis ball was correctly identified as a tennis ball.

False Positive (FP):
- Actual ball = Tennis
- Predicted ball = Cricket
- Meaning: A tennis ball was incorrectly classified as a cricket ball.

False Negative (FN):
- Actual ball = Cricket
- Predicted ball = Tennis
- Meaning: A cricket ball was incorrectly classified as a tennis ball.
""")


# ============================================================
# QUESTION 6
# Tennis ball predicted as cricket ball.
# ============================================================

print("""
QUESTION 6
==========

If a tennis ball is predicted as a cricket ball:

Error type = False Positive (FP)

Reason:
In this example, Cricket is treated as the positive class and Tennis as
the negative class.

The actual class is negative (Tennis), but the model predicted the
positive class (Cricket). Therefore, it is called a False Positive.
""")


# ============================================================
# QUESTION 7
# Confusion matrix:
#
#                  Predicted Cricket   Predicted Tennis
# Actual Cricket          40                  5
# Actual Tennis            3                 52
#
# Calculate accuracy, total errors and correct predictions.
# ============================================================

print("""
QUESTION 7
==========

Given confusion matrix:

                  Predicted Cricket   Predicted Tennis
Actual Cricket          40                  5
Actual Tennis            3                 52

Correct predictions:
= 40 + 52
= 92

Total errors:
= 5 + 3
= 8

Total samples:
= 40 + 5 + 3 + 52
= 100

Accuracy:
= Correct Predictions / Total Samples * 100
= 92 / 100 * 100
= 92%

Answers:
- Accuracy = 92%
- Total Errors = 8
- Total Correct Predictions = 92
""")


# Also demonstrate the Question 7 calculation using Python.
print("QUESTION 7 - Python calculation")

actual = ["Cricket"] * 45 + ["Tennis"] * 55
predicted = (
    ["Cricket"] * 40
    + ["Tennis"] * 5
    + ["Cricket"] * 3
    + ["Tennis"] * 52
)

correct = sum(a == p for a, p in zip(actual, predicted))
total = len(actual)
errors = total - correct
accuracy = correct / total * 100

print("Correct predictions:", correct)
print("Total errors:", errors)
print(f"Accuracy: {accuracy:.2f}%")


# ============================================================
# QUESTION 8
# Binary vs Multiclass Classification.
# ============================================================

print("""
QUESTION 8
==========

Binary Classification:
- There are two possible output classes.
- Example: Email classification -> Spam or Not Spam.

Multiclass Classification:
- There are more than two possible output classes.
- Example: Classifying an image as Cat, Dog or Horse.

Difference:
Binary classification -> 2 classes
Multiclass classification -> 3 or more classes
""")


# ============================================================
# QUESTION 9
# Confusion matrix in multiclass classification.
# ============================================================

print("""
QUESTION 9
==========

In binary classification, the confusion matrix is normally a 2 x 2 table:

             Predicted 0   Predicted 1
Actual 0        TN             FP
Actual 1        FN             TP

In multiclass classification, the confusion matrix becomes an N x N
matrix, where N is the number of classes.

For example, with 3 classes:

             Pred A  Pred B  Pred C
Actual A       ...     ...     ...
Actual B       ...     ...     ...
Actual C       ...     ...     ...

The diagonal values represent correct predictions for each class.
Off-diagonal values represent misclassifications between classes.

Therefore:
- Binary classification -> 2 x 2 matrix
- 3-class classification -> 3 x 3 matrix
- N-class classification -> N x N matrix
""")


# ============================================================
# QUESTION 10
# Iris dataset:
# features, label, why multiclass, number of classes.
# ============================================================

print("""
QUESTION 10
===========

Iris Dataset

Features:
1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

Label:
- Species of the iris flower.

The three classes are:
1. Iris setosa
2. Iris versicolor
3. Iris virginica

Why is it a multiclass classification problem?
Because the target label can belong to one of three different classes,
rather than only two classes.

Number of possible output classes:
3

Therefore, Iris is a 3-class multiclass classification problem.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
============================================================
ASSIGNMENT 36 COMPLETED
============================================================

All 10 questions have been answered in question-answer sequence.

Important numerical answer:
Question 7 -> Accuracy = 92%, Correct = 92, Errors = 8.

Iris dataset:
4 input features and 3 possible output classes.
============================================================
""")
