"""
Machine Learning Assignment 55
Marvellous Infosystems : Python - Automation & Machine Learning

Topic:
Customer Loan Approval Using Voting Classification

Assignment requirements:
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors
- Hard Voting Classifier
- Soft Voting Classifier

Expected dataset columns:
    Age
    Income
    Credit Score
    Existing Loan
    Employment Experience
    Loan Amount
    LoanApproved

Target:
    LoanApproved
        0 = Loan Rejected
        1 = Loan Approved

The PDF does not include the actual dataset, so this program expects a CSV
file and calculates the requested accuracy values when the script is run.
Change DATA_FILE if your dataset has a different filename/path.
"""

import os
import warnings
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

warnings.filterwarnings("ignore")


# ============================================================
# Q1. Load the dataset.
# ============================================================
print("""
Q1. Load the dataset.

Answer:
The loan approval dataset is loaded from a CSV file using pandas.
The dataset should contain the customer information specified in the
assignment and the target column LoanApproved.
""")

DATA_FILE = "loan_approval.csv"

EXPECTED_COLUMNS = [
    "Age",
    "Income",
    "Credit Score",
    "Existing Loan",
    "Employment Experience",
    "Loan Amount",
    "LoanApproved",
]

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(
        f"""
Dataset not found: {DATA_FILE}

Place your loan approval CSV file in the same directory as this script,
or change the DATA_FILE variable to the correct file path.

Expected columns:
{EXPECTED_COLUMNS}
"""
    )

df = pd.read_csv(DATA_FILE)

missing_columns = [
    column for column in EXPECTED_COLUMNS
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        "The following required columns are missing from the dataset:\n"
        + "\n".join(f"- {column}" for column in missing_columns)
    )

print("Dataset loaded successfully.")
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# Q2. Check for missing values.
# ============================================================
print("""
Q2. Check for missing values.

Answer:
Missing values are checked using isnull().sum(). The preprocessing
pipeline also handles any missing numerical values using the median.
""")

print("\nMissing values in each column:")
print(df[EXPECTED_COLUMNS].isnull().sum())


# ============================================================
# Q3. Separate input and output variables.
# ============================================================
print("""
Q3. Separate input and output variables.

Answer:
The customer information columns are used as input variables X, while
LoanApproved is used as the target/output variable y.

Input variables:
- Age
- Income
- Credit Score
- Existing Loan
- Employment Experience
- Loan Amount

Target:
- LoanApproved
    0 = Loan Rejected
    1 = Loan Approved
""")

feature_columns = [
    "Age",
    "Income",
    "Credit Score",
    "Existing Loan",
    "Employment Experience",
    "Loan Amount",
]

target_column = "LoanApproved"

X = df[feature_columns].copy()
y = pd.to_numeric(df[target_column], errors="coerce")

# Remove rows with missing/invalid target values.
valid_target = y.notna()
X = X.loc[valid_target].copy()
y = y.loc[valid_target].astype(int)

# Keep only the binary target values required by the assignment.
valid_classes = y.isin([0, 1])
X = X.loc[valid_classes].copy()
y = y.loc[valid_classes].copy()

print("Input shape:", X.shape)
print("Target shape:", y.shape)


# ============================================================
# Q4. Split the dataset into training and testing data.
# ============================================================
print("""
Q4. Split the dataset into training and testing data.

Answer:
The dataset is split into training and testing portions. The training
data is used to train the classifiers, while the testing data is used
to calculate accuracy on unseen examples.

An 80% training and 20% testing split is used.
""")

if y.nunique() < 2:
    raise ValueError(
        "LoanApproved must contain both 0 (Rejected) and 1 (Approved)."
    )

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


# ============================================================
# Q5. Train Logistic Regression.
# ============================================================
print("""
Q5. Train Logistic Regression.

Answer:
Logistic Regression is a supervised classification algorithm. It
estimates the probability of the positive class and converts that
probability into a class prediction.

The numerical features are standardized before Logistic Regression.
""")

numeric_preprocessor = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_preprocessor, feature_columns),
    ]
)

logistic_regression = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=2000)),
    ]
)

logistic_regression.fit(X_train, y_train)


# ============================================================
# Q6. Train Decision Tree.
# ============================================================
print("""
Q6. Train Decision Tree.

Answer:
A Decision Tree classifies observations by learning a sequence of
feature-based decision rules. It does not require feature scaling.
""")

decision_tree = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", DecisionTreeClassifier(random_state=42)),
    ]
)

decision_tree.fit(X_train, y_train)


# ============================================================
# Q7. Train KNN.
# ============================================================
print("""
Q7. Train KNN.

Answer:
K-Nearest Neighbors (KNN) classifies a new observation based on the
classes of nearby training observations. Since KNN is distance-based,
the numerical features are standardized before classification.
""")

knn = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", KNeighborsClassifier(n_neighbors=5)),
    ]
)

knn.fit(X_train, y_train)


# ============================================================
# Q8. Calculate individual accuracy of all three algorithms.
# ============================================================
print("""
Q8. Calculate the individual accuracy of all three algorithms.

Answer:
Accuracy is the proportion of correctly classified test observations:

    Accuracy = Correct Predictions / Total Predictions

The accuracy of Logistic Regression, Decision Tree, and KNN is
calculated below.
""")

logistic_pred = logistic_regression.predict(X_test)
decision_tree_pred = decision_tree.predict(X_test)
knn_pred = knn.predict(X_test)

logistic_accuracy = accuracy_score(y_test, logistic_pred)
decision_tree_accuracy = accuracy_score(y_test, decision_tree_pred)
knn_accuracy = accuracy_score(y_test, knn_pred)

print(f"Logistic Regression Accuracy: {logistic_accuracy:.4f}")
print(f"Decision Tree Accuracy      : {decision_tree_accuracy:.4f}")
print(f"KNN Accuracy                : {knn_accuracy:.4f}")


# ============================================================
# Q9. Create a Hard Voting Classifier.
# ============================================================
print("""
Q9. Create a Hard Voting Classifier.

Answer:
A Hard Voting Classifier combines the class predictions of multiple
classifiers. The final class is selected by majority voting.

The three classifiers required by the assignment are:
- Logistic Regression
- Decision Tree
- KNN
""")

hard_voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=2000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5)),
    ],
    voting="hard",
)

# Since the three estimators have different preprocessing requirements,
# use a common numeric preprocessing pipeline before the voting classifier.
# All assignment features are expected to be numerical.
hard_voting_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("voting", hard_voting),
    ]
)

hard_voting_pipeline.fit(X_train, y_train)


# ============================================================
# Q10. Calculate Hard Voting accuracy.
# ============================================================
print("""
Q10. Calculate the accuracy of the Hard Voting Classifier.

Answer:
The trained Hard Voting Classifier is evaluated on the testing data
using accuracy.
""")

hard_voting_pred = hard_voting_pipeline.predict(X_test)
hard_voting_accuracy = accuracy_score(y_test, hard_voting_pred)

print(f"Hard Voting Accuracy: {hard_voting_accuracy:.4f}")


# ============================================================
# Q11. Create a Soft Voting Classifier.
# ============================================================
print("""
Q11. Create a Soft Voting Classifier.

Answer:
A Soft Voting Classifier combines the predicted class probabilities
from the component classifiers. The class with the highest average
probability is selected as the final prediction.

Soft voting requires classifiers that provide probability estimates.
Logistic Regression, Decision Tree, and KNN all support predict_proba().
""")

soft_voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=2000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5)),
    ],
    voting="soft",
)

soft_voting_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("voting", soft_voting),
    ]
)

soft_voting_pipeline.fit(X_train, y_train)


# ============================================================
# Q12. Calculate Soft Voting accuracy.
# ============================================================
print("""
Q12. Calculate the accuracy of the Soft Voting Classifier.

Answer:
The trained Soft Voting Classifier is evaluated on the testing data
using accuracy.
""")

soft_voting_pred = soft_voting_pipeline.predict(X_test)
soft_voting_accuracy = accuracy_score(y_test, soft_voting_pred)

print(f"Soft Voting Accuracy: {soft_voting_accuracy:.4f}")


# ============================================================
# Q13. Compare all models.
# ============================================================
print("""
Q13. Compare:
- Logistic Regression
- Decision Tree
- KNN
- Hard Voting
- Soft Voting

Answer:
The final comparison table required by the assignment is generated
below. The actual accuracy values depend on the supplied dataset and
are therefore calculated at runtime rather than hard-coded.
""")

comparison = pd.DataFrame(
    {
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "KNN",
            "Hard Voting",
            "Soft Voting",
        ],
        "Accuracy": [
            logistic_accuracy,
            decision_tree_accuracy,
            knn_accuracy,
            hard_voting_accuracy,
            soft_voting_accuracy,
        ],
    }
)

print("\nFinal Comparison:")
print(
    comparison.to_string(
        index=False,
        formatters={"Accuracy": "{:.4f}".format},
    )
)


print("""
============================================================
ASSIGNMENT 55 COMPLETED
============================================================
Customer Loan Approval Using Voting Classification

Models:
- Logistic Regression
- Decision Tree
- KNN
- Hard Voting
- Soft Voting

Metric:
- Accuracy

The final comparison table is printed after running the script
with the actual dataset.
============================================================
""")
