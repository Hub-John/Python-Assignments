# Marvellous Infosystems : Python - Automation & Machine Learning
# Deep Learning Assignment 67
# Format: Question -> Answer

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# QUESTION 1
# Create a neural network model to predict whether a customer
# will leave a service.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1 - CUSTOMER CHURN PREDICTION")
print("=" * 70)

# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
], dtype=float)

# 0 = Customer will stay
# 1 = Customer will leave
y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# Answer 1: Load/Create dataset
print("\n1. Dataset created successfully.")
print("Number of records:", len(X))

# Answer 2: Clean the dataset
print("\n2. Cleaning the dataset...")
if np.isnan(X).any():
    column_means = np.nanmean(X, axis=0)
    rows, cols = np.where(np.isnan(X))
    X[rows, cols] = column_means
    print("Missing values replaced with column means.")
else:
    print("No missing values found. Dataset is clean.")

# Answer 3: Apply StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n3. StandardScaler applied successfully.")

# Answer 4: Train FNN model
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

model = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    solver="lbfgs",
    max_iter=2000,
    random_state=42
)

model.fit(X_train, y_train)
print("4. FNN model trained successfully.")

# Answer 5: Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n5. Model Evaluation")
print("Actual values:   ", y_test)
print("Predicted values:", y_pred)
print("Accuracy:", accuracy)

# Test input from assignment
new_customer = np.array([[46, 1450, 5, 6, 9]], dtype=float)
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)[0]

print("\nTest Input:", new_customer.tolist())

if prediction == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer may stay")

print("Assignment Expected Output: Customer may leave")


# ============================================================
# QUESTION 2
# Create a neural network model to predict loan approval.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2 - LOAN APPROVAL PREDICTION")
print("=" * 70)

# Features:
# [Applicant Income, Credit Score, Loan Amount,
#  Existing EMI, Employment Status]
#
# Employment Status:
# 0 = Not Stable
# 1 = Stable

X_loan = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
], dtype=float)

# 0 = Loan rejected
# 1 = Loan approved
y_loan = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

# Answer 1: Preprocess categorical values
print("\n1. Preprocess categorical values")
print("Employment Status is already encoded as:")
print("0 = Not Stable")
print("1 = Stable")
print("No additional categorical encoding is required.")

# Answer 2: Apply scaling
loan_scaler = StandardScaler()
X_loan_scaled = loan_scaler.fit_transform(X_loan)

print("\n2. StandardScaler applied successfully.")

# Answer 3: Train FNN model
X_loan_train, X_loan_test, y_loan_train, y_loan_test = train_test_split(
    X_loan_scaled, y_loan, test_size=0.3, random_state=42, stratify=y_loan
)

loan_model = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    solver="lbfgs",
    max_iter=2000,
    random_state=42
)

loan_model.fit(X_loan_train, y_loan_train)
print("3. FNN model trained successfully.")

# Answer 4: Evaluate model
loan_test_prediction = loan_model.predict(X_loan_test)
loan_accuracy = accuracy_score(y_loan_test, loan_test_prediction)

print("\n4. Model Evaluation")
print("Actual values:   ", y_loan_test)
print("Predicted values:", loan_test_prediction)
print("Accuracy:", loan_accuracy)

# Answer 5: Predict approval for new applicant
new_applicant = np.array([[55000, 720, 400000, 10000, 1]], dtype=float)
new_applicant_scaled = loan_scaler.transform(new_applicant)
loan_prediction = loan_model.predict(new_applicant_scaled)[0]

print("\nTest Input:", new_applicant.tolist())

if loan_prediction == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")

print("Assignment Expected Output: Loan Approved")


# ============================================================
# END OF ASSIGNMENT
# ============================================================
