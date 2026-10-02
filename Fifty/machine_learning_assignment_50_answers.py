from pathlib import Path

p = Path("/mnt/data/machine_learning_assignment_50_answers.py")

content = '''"""
Machine Learning Assignment 50
Breast Cancer Prediction
Marvellous Infosystems
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)

print("""
Q1. Load and explore the dataset.

Answer:
The assignment specifies the Breast Cancer Wisconsin Dataset and asks
to use load_breast_cancer() from sklearn. It contains 569 records and
30 real-valued features. The target is:
    0 -> Malignant
    1 -> Benign
""")

data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="Target")

print("Shape:", X.shape)
print("\\nFeature names:")
print(list(X.columns))
print("\\nFirst 5 rows:")
print(X.head())
print("\\nTarget distribution:")
print(y.value_counts().sort_index())


print("""
Q2. Perform data preprocessing:
    - Handle missing values (if any)
    - Normalize or scale features

Answer:
Missing values are checked first. Any missing numerical value is replaced
with that feature's median. StandardScaler is then used to standardize
the features.
""")

print("\\nMissing values before preprocessing:")
print(X.isnull().sum())

X_processed = X.copy()
for column in X_processed.columns:
    if X_processed[column].isnull().any():
        X_processed[column] = X_processed[column].fillna(
            X_processed[column].median()
        )

print("\\nTotal missing values after handling:")
print(int(X_processed.isnull().sum().sum()))


print("""
Q3. Perform exploratory data analysis (EDA):
    - Summary statistics
    - Visualization of feature correlations

Answer:
Summary statistics are generated using describe(). A correlation matrix
is calculated and visualized as a heatmap.
""")

print("\\nSummary statistics:")
print(X_processed.describe().T)

correlation_matrix = X_processed.corr()

plt.figure(figsize=(16, 13))
plt.imshow(correlation_matrix, interpolation="nearest", aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90,
    fontsize=7,
)
plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    fontsize=7,
)
plt.title("Breast Cancer Dataset - Feature Correlation Heatmap")
plt.tight_layout()
plt.show()


print("""
Q4. Split the dataset into training and testing sets.

Answer:
The dataset is divided into training and testing sets. An 80/20 split
with random_state=42 is used, with stratification to preserve class
proportions.
""")

X_train, X_test, y_train, y_test = train_test_split(
    X_processed,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))


print("""
Q5. Build a machine learning classification model to predict tumor type.

Answer:
The assignment does not specify a particular classification algorithm,
so Logistic Regression is used as the classification model. The features
are standardized before training because Logistic Regression can be
affected by feature scale.
""")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=5000, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("Model trained successfully.")


print("""
Q6. Evaluate the model using:
    - Accuracy
    - Confusion Matrix
    - Precision
    - Recall
    - F1-Score

Answer:
All requested metrics are calculated on the test set. The confusion
matrix uses class 0 = Malignant and class 1 = Benign.
""")

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("\\nAccuracy :", f"{accuracy:.4f}")
print("Precision:", f"{precision:.4f}")
print("Recall   :", f"{recall:.4f}")
print("F1-Score :", f"{f1:.4f}")

print("\\nConfusion Matrix:")
print(cm)

print("\\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Malignant (0)", "Benign (1)"],
        zero_division=0,
    )
)


print("""
Q7. Provide your observations and conclusions.

Answer:
1. The dataset contains 569 records and 30 real-valued features.
2. Missing values are checked and handled before model training.
3. Features are standardized before Logistic Regression.
4. Summary statistics and a feature-correlation heatmap are produced
   for EDA.
5. The data is split into training and testing sets.
6. Accuracy, confusion matrix, precision, recall, and F1-score are
   calculated using the test set.

Conclusion:
The script provides a reproducible Logistic Regression classification
solution for the assignment. The numerical metrics printed by the
program are calculated from the actual test split when the script runs.

The assignment does not prescribe a specific algorithm or target
accuracy, so no performance value is invented here.

This is a machine-learning classification exercise; the model output
should not be treated as a medical diagnosis.
""")


print("""
============================================================
ASSIGNMENT 50 COMPLETED
============================================================
All objectives are answered in Question -> Answer sequence.
============================================================
""")
'''

p.write_text(content, encoding="utf-8")
print(str(p))
