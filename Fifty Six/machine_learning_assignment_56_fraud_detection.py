"""
Machine Learning Assignment 56
Marvellous Infosystems : Python - Automation & Machine Learning
Topic: Fraudulent Transaction Detection

This script builds and compares:
1. Decision Tree
2. Bagging Classifier
3. Random Forest Classifier
4. AdaBoost Classifier
5. Voting Classifier

The assignment PDF does not provide a dataset file, so this program expects
a CSV dataset containing the specified features and the target column "Fraud".

Expected columns:
    Transaction Amount
    Transaction Time
    Account Age
    Number of Previous Transactions
    Location Difference
    Device Type
    Failed Login Attempts
    Fraud

Target:
    0 = Normal Transaction
    1 = Fraudulent Transaction

Update DATA_FILE if your CSV has a different filename/path.
"""

import os
import warnings
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

warnings.filterwarnings("ignore")


# ============================================================
# Q1. Decision Tree
# ============================================================
print("""
Q1. Build and evaluate a Decision Tree classifier.

Answer:
A Decision Tree recursively splits the data using feature-based rules.
It is a supervised learning algorithm suitable for classification.
The model is trained below and evaluated using accuracy, precision,
recall, F1 score, and confusion matrix.
""")


# ============================================================
# Q2. Bagging Classifier
# ============================================================
print("""
Q2. Build and evaluate a Bagging Classifier.

Answer:
Bagging (Bootstrap Aggregating) trains multiple versions of a base
estimator on different bootstrap samples and combines their predictions.
This can reduce variance and improve model stability.
""")


# ============================================================
# Q3. Random Forest Classifier
# ============================================================
print("""
Q3. Build and evaluate a Random Forest Classifier.

Answer:
Random Forest is an ensemble of decision trees. It uses bootstrap
sampling and random feature selection while building trees, then
combines their predictions.
""")


# ============================================================
# Q4. AdaBoost Classifier
# ============================================================
print("""
Q4. Build and evaluate an AdaBoost Classifier.

Answer:
AdaBoost builds a sequence of weak learners. Later learners focus more
on observations that earlier learners classified incorrectly.
Their weighted predictions are combined to produce the final result.
""")


# ============================================================
# Q5. Voting Classifier
# ============================================================
print("""
Q5. Build and evaluate a Voting Classifier.

Answer:
A Voting Classifier combines predictions from multiple different
classifiers. With hard voting, the final class is selected by majority
vote among the component classifiers.
""")


# ============================================================
# Q6. Evaluate every model using the required metrics
# ============================================================
print("""
Q6. Evaluate each model using Accuracy, Precision, Recall, F1 Score,
and Confusion Matrix.

Answer:
The script below calculates all five requested evaluation measures
for every model.
""")


# ============================================================
# Q7. Prepare the dataset
# ============================================================
print("""
Q7. Prepare the fraudulent transaction dataset.

Answer:
The assignment specifies these input features:
- Transaction Amount
- Transaction Time
- Account Age
- Number of Previous Transactions
- Location Difference
- Device Type
- Failed Login Attempts

Target:
- Fraud: 0 = Normal Transaction
- Fraud: 1 = Fraudulent Transaction

The CSV file should contain these columns.
""")

DATA_FILE = "fraudulent_transactions.csv"

EXPECTED_FEATURES = [
    "Transaction Amount",
    "Transaction Time",
    "Account Age",
    "Number of Previous Transactions",
    "Location Difference",
    "Device Type",
    "Failed Login Attempts",
]

TARGET = "Fraud"


def load_dataset(file_path):
    """Load the CSV dataset and validate the required columns."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"\nDataset not found: {file_path}\n"
            "Place your CSV file in the same folder as this script or "
            "change DATA_FILE to the correct path.\n"
        )

    df = pd.read_csv(file_path)

    required = EXPECTED_FEATURES + [TARGET]
    missing = [column for column in required if column not in df.columns]

    if missing:
        raise ValueError(
            "The following required columns are missing from the dataset:\n"
            + "\n".join(f" - {column}" for column in missing)
        )

    return df


# ============================================================
# Q8. Handle Transaction Time
# ============================================================
print("""
Q8. Prepare Transaction Time for machine learning.

Answer:
If Transaction Time is stored as a time/date string, the script converts
it into a numeric representation using seconds from midnight. If it is
already numeric, it is kept as numeric data.
""")


def convert_transaction_time(series):
    """
    Convert Transaction Time into a numeric feature.

    Numeric values are preserved. Non-numeric values are interpreted as
    time/date strings where possible. Invalid values become NaN and are
    later handled by the imputer.
    """
    numeric = pd.to_numeric(series, errors="coerce")

    if numeric.notna().sum() == len(series):
        return numeric

    parsed = pd.to_datetime(series, errors="coerce")

    seconds = (
        parsed.dt.hour * 3600
        + parsed.dt.minute * 60
        + parsed.dt.second
    )

    # For rows that were numeric, retain the original numeric value.
    result = seconds.astype(float)
    result[numeric.notna()] = numeric[numeric.notna()].astype(float)

    return result


# ============================================================
# Q9. Preprocess numerical and categorical features
# ============================================================
print("""
Q9. Preprocess numerical and categorical features.

Answer:
Numerical features use median imputation. The categorical Device Type
feature uses the most frequent value for missing data and One-Hot
Encoding to convert categories into numerical columns.
""")

df = load_dataset(DATA_FILE)

df = df.copy()
df["Transaction Time"] = convert_transaction_time(df["Transaction Time"])

X = df[EXPECTED_FEATURES].copy()
y = pd.to_numeric(df[TARGET], errors="coerce")

# Remove rows where the target is missing.
valid_target = y.notna()
X = X.loc[valid_target].copy()
y = y.loc[valid_target].astype(int)

# Keep the expected binary target values.
valid_classes = y.isin([0, 1])
X = X.loc[valid_classes].copy()
y = y.loc[valid_classes].copy()

numeric_features = [
    "Transaction Amount",
    "Transaction Time",
    "Account Age",
    "Number of Previous Transactions",
    "Location Difference",
    "Failed Login Attempts",
]

categorical_features = ["Device Type"]

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ]
)


# ============================================================
# Q10. Split data into training and testing sets
# ============================================================
print("""
Q10. Split the dataset into training and testing sets.

Answer:
The data is divided into training and testing subsets. The training
subset is used to learn model parameters, while the testing subset is
used to evaluate performance on unseen data.
""")

if y.nunique() < 2:
    raise ValueError(
        "The Fraud target must contain both classes: 0 (Normal) and 1 (Fraud)."
    )

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


# ============================================================
# Q11. Create the five requested models
# ============================================================
print("""
Q11. Create the five requested ensemble approaches.

Answer:
The following models are created:
1. Decision Tree
2. Bagging Classifier
3. Random Forest Classifier
4. AdaBoost Classifier
5. Voting Classifier
""")

decision_tree = DecisionTreeClassifier(
    random_state=42,
    class_weight="balanced",
)

# Use a Decision Tree as the base estimator for Bagging.
bagging_base = DecisionTreeClassifier(
    random_state=42,
    max_depth=None,
)

try:
    bagging = BaggingClassifier(
        estimator=bagging_base,
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
    )
except TypeError:
    # Compatibility with older scikit-learn versions.
    bagging = BaggingClassifier(
        base_estimator=bagging_base,
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
    )

random_forest = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1,
)

adaboost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42,
)

# Voting uses three different classifiers.
voting_estimators = [
    (
        "dt",
        DecisionTreeClassifier(
            random_state=42,
            class_weight="balanced",
        ),
    ),
    (
        "rf",
        RandomForestClassifier(
            n_estimators=150,
            random_state=42,
            class_weight="balanced",
            n_jobs=-1,
        ),
    ),
    (
        "lr",
        LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=42,
        ),
    ),
]

voting = VotingClassifier(
    estimators=voting_estimators,
    voting="hard",
)


models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": random_forest,
    "AdaBoost": adaboost,
    "Voting": voting,
}


# ============================================================
# Q12. Train and evaluate each model
# ============================================================
print("""
Q12. Train and evaluate all five models.

Answer:
Each classifier is placed inside a pipeline with the same preprocessing
steps. The pipeline is fitted on the training data and evaluated on the
test data.
""")


def build_pipeline(model):
    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )


results = []
confusion_matrices = {}

for name, model in models.items():
    print("\n" + "=" * 70)
    print(f"Training: {name}")
    print("=" * 70)

    pipeline = build_pipeline(model)
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, zero_division=0
    )
    f1 = f1_score(
        y_test, y_pred, zero_division=0
    )
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

    confusion_matrices[name] = cm

    results.append(
        {
            "Algorithm": name,
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1": f1,
        }
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print("Confusion Matrix [rows=true, columns=predicted]:")
    print(cm)


# ============================================================
# Q13. Prepare final comparison table
# ============================================================
print("""
Q13. Prepare the final comparison table.

Answer:
The assignment requires a comparison of Algorithm, Accuracy, Precision,
Recall, and F1 Score. The table below is generated from the actual test
results after the script is run on the supplied dataset.
""")

comparison = pd.DataFrame(results)

print("\n" + "=" * 90)
print("FINAL COMPARISON")
print("=" * 90)
print(
    comparison.to_string(
        index=False,
        formatters={
            "Accuracy": "{:.4f}".format,
            "Precision": "{:.4f}".format,
            "Recall": "{:.4f}".format,
            "F1": "{:.4f}".format,
        },
    )
)


# ============================================================
# Q14. Display all confusion matrices
# ============================================================
print("""
Q14. Display the confusion matrix for each algorithm.

Answer:
For binary Fraud classification, the confusion matrix is arranged as:

    [[TN, FP],
     [FN, TP]]

TN = Normal transaction correctly predicted as Normal
FP = Normal transaction incorrectly predicted as Fraud
FN = Fraudulent transaction incorrectly predicted as Normal
TP = Fraudulent transaction correctly predicted as Fraud
""")

for name, cm in confusion_matrices.items():
    print(f"\n{name} Confusion Matrix:")
    print(cm)


# ============================================================
# Q15. Recommend the most suitable model
# ============================================================
print("""
Q15. Recommend the most suitable model.

Answer:
Fraud detection can place particular importance on detecting fraudulent
transactions, so Recall and F1 Score are useful measures in addition to
Accuracy and Precision.

Because the assignment does not provide the dataset or actual model
results, this script does not invent a fixed winner. Instead, it selects
the model with the highest F1 Score from the results generated on the
actual dataset. If multiple models have the same F1 Score, Recall,
Precision, and Accuracy are used as tie-breakers.

This recommendation is therefore data-dependent and is produced only
after the script is run.
""")

ranking_for_selection = comparison.sort_values(
    by=["F1", "Recall", "Precision", "Accuracy"],
    ascending=False,
)

selected_model = ranking_for_selection.iloc[0]

print("\n" + "=" * 90)
print("DATA-DRIVEN MODEL SELECTION")
print("=" * 90)
print(
    f"Selected model based on highest F1 Score "
    f"(then Recall, Precision, Accuracy for ties): "
    f"{selected_model['Algorithm']}"
)
print(f"F1 Score : {selected_model['F1']:.4f}")
print(f"Recall   : {selected_model['Recall']:.4f}")
print(f"Precision: {selected_model['Precision']:.4f}")
print(f"Accuracy : {selected_model['Accuracy']:.4f}")

print("""
Note:
The numerical results and selected model above are generated from the
dataset at runtime. They are not hard-coded because the assignment PDF
does not include the transaction dataset itself.
""")


# ============================================================
# End
# ============================================================
print("""
============================================================
ASSIGNMENT 56 COMPLETED
============================================================
Fraudulent Transaction Detection:
- Decision Tree
- Bagging
- Random Forest
- AdaBoost
- Voting

Metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
============================================================
""")
