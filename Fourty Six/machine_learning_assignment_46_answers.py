"""
Machine Learning Assignment 46
Marvellous Infosystems : Python - Automation & Machine Learning

Assignment topic:
Advertisement agency dataset / Linear Regression application.

The PDF asks for an ML application that:
1. Gets data from MarvellousAdvertising.csv
2. Cleans, prepares and manipulates the data
3. Trains a Linear Regression model
4. Divides the dataset into half for training and uses the remaining half for testing
5. Displays predicted values and expected values

Note:
The PDF text mentions "Classification", but the specified algorithm is
Linear Regression and the target is the continuous Sales value. Therefore,
this implementation follows the specified Linear Regression algorithm.
"""

# ============================================================
# Q1. Get Data
#
# Load data from MarvellousAdvertising.csv into Python.
#
# Dataset columns shown in the PDF:
# TV, radio, newspaper, sales
# ============================================================

import pandas as pd

file_name = "MarvellousAdvertising.csv"

try:
    data = pd.read_csv(file_name)
except FileNotFoundError:
    raise FileNotFoundError(
        f"'{file_name}' was not found. Place the CSV file in the same "
        "folder as this Python program and run it again."
    )

print("Q1. Get Data")
print("Dataset loaded successfully.")
print("\nFirst 10 records:")
print(data.head(10))

print("\nDataset shape:")
print(data.shape)

print("\nDataset columns:")
print(list(data.columns))


# ============================================================
# Q2. Clean, Prepare and Manipulate Data
#
# Prepare the data in a format accepted by the ML algorithm.
#
# Features:
#   TV
#   radio
#   newspaper
#
# Target:
#   sales
# ============================================================

print("\nQ2. Clean, Prepare and Manipulate Data")

required_columns = ["TV", "radio", "newspaper", "sales"]

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    raise ValueError(
        "The CSV file is missing required columns: "
        + ", ".join(missing_columns)
    )

# Keep only the columns required by the assignment.
data = data[required_columns].copy()

# Convert all required columns to numeric values.
# Invalid values are converted to NaN and then removed.
for column in required_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")

print("Missing values before cleaning:")
print(data.isnull().sum())

# Remove records containing missing values.
data = data.dropna().reset_index(drop=True)

print("\nMissing values after cleaning:")
print(data.isnull().sum())

# X contains input features.
X = data[["TV", "radio", "newspaper"]]

# y contains the target/output.
y = data["sales"]

print("\nInput features:")
print(X.head())

print("\nTarget (Sales):")
print(y.head())


# ============================================================
# Q3. Train Data
#
# Select Linear Regression from scikit-learn.
# Divide the dataset into half for training.
# ============================================================

from sklearn.linear_model import LinearRegression

print("\nQ3. Train Data")

# The assignment explicitly asks to divide the dataset into half.
# The first half is used for training and the remaining half for testing.
split_index = len(data) // 2

X_train = X.iloc[:split_index]
y_train = y.iloc[:split_index]

X_test = X.iloc[split_index:]
y_test = y.iloc[split_index:]

print("Total records   :", len(data))
print("Training records:", len(X_train))
print("Testing records :", len(X_test))

# Create and train the Linear Regression model.
model = LinearRegression()
model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully.")

print("Coefficients:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature}: {coefficient}")

print("Intercept:", model.intercept_)


# ============================================================
# Q4. Test the Data
#
# Test the model using the remaining half of the dataset.
# ============================================================

print("\nQ4. Test Data")

predicted_values = model.predict(X_test)

print("Model prediction completed.")

print("\nPredicted Sales:")
for value in predicted_values:
    print(round(value, 2))


# ============================================================
# Q5. Display Predicted Values and Expected Values
#
# Display the predicted Sales values produced by Linear
# Regression alongside the actual/expected Sales values.
# ============================================================

print("\nQ5. Predicted Values vs Expected Values")

results = pd.DataFrame({
    "Expected Sales": y_test.values,
    "Predicted Sales": predicted_values
})

results["Predicted Sales"] = results["Predicted Sales"].round(2)

print(results.to_string(index=False))


# ============================================================
# Complete Application
# ============================================================

print("\n" + "=" * 60)
print("Machine Learning Application Completed")
print("=" * 60)
print("Algorithm : Linear Regression")
print("Features  : TV, radio, newspaper")
print("Target    : sales")
print("Training  : First half of dataset")
print("Testing   : Remaining half of dataset")
print("=" * 60)
