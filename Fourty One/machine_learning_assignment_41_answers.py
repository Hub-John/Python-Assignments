"""
Marvellous Infosystems - Python Programming / Machine Learning Assignment 41
Wine Classification

Question/Step 1: Get Data
Question/Step 2: Clean, Prepare and Manipulate Data
Question/Step 3: Train Data
Question/Step 4: Test Data
Question/Step 5: Calculate Accuracy

The PDF specifies the workflow but does not specify a classifier or split ratio.
This implementation uses the standard scikit-learn Wine dataset, StandardScaler,
KNN (K=5), and an 80/20 stratified train-test split.
"""

# ============================================================
# QUESTION 1 - STEP 1: GET DATA
# ============================================================
from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target + 1, name="Class")  # 0,1,2 -> Class 1,2,3

print("=" * 70)
print("QUESTION 1 - STEP 1: GET DATA")
print("=" * 70)
print("Dataset shape:", X.shape)

print("\n13 Wine Features:")
for i, feature in enumerate(wine.feature_names, 1):
    print(f"{i}. {feature}")

print("\nClasses:", sorted(y.unique()))
print("\nFirst 5 records:")
print(X.head())


# ============================================================
# QUESTION 2 - STEP 2: CLEAN, PREPARE AND MANIPULATE DATA
# ============================================================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("\n" + "=" * 70)
print("QUESTION 2 - STEP 2: CLEAN, PREPARE AND MANIPULATE DATA")
print("=" * 70)

print("Missing values:")
print(X.isnull().sum())

# Standardize all 13 numerical features.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 80% training and 20% testing; stratify preserves class proportions.
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ============================================================
# QUESTION 3 - STEP 3: TRAIN DATA
# ============================================================
from sklearn.neighbors import KNeighborsClassifier

print("\n" + "=" * 70)
print("QUESTION 3 - STEP 3: TRAIN DATA")
print("=" * 70)

# The PDF does not specify an algorithm, so KNN is selected.
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print("Algorithm: K-Nearest Neighbors (KNN)")
print("K =", 5)
print("Model trained successfully.")


# ============================================================
# QUESTION 4 - STEP 4: TEST DATA
# ============================================================
print("\n" + "=" * 70)
print("QUESTION 4 - STEP 4: TEST DATA")
print("=" * 70)

y_pred = model.predict(X_test)

results = pd.DataFrame({
    "Expected Class": y_test.values,
    "Predicted Class": y_pred
})

print("Expected vs Predicted:")
print(results.to_string(index=False))


# ============================================================
# QUESTION 5 - STEP 5: CALCULATE ACCURACY
# ============================================================
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("\n" + "=" * 70)
print("QUESTION 5 - STEP 5: CALCULATE ACCURACY")
print("=" * 70)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Accuracy Percentage: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Class 1", "Class 2", "Class 3"]
))


# ============================================================
# BONUS: PREDICT A NEW WINE
# ============================================================
print("\n" + "=" * 70)
print("NEW WINE PREDICTION EXAMPLE")
print("=" * 70)

# For demonstration, use the first wine record as a new sample.
sample = X.iloc[[0]]
sample_scaled = scaler.transform(sample)
predicted_class = model.predict(sample_scaled)[0]

print("Predicted Wine Class:", predicted_class)
