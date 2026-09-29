"""
Deep Learning Assignment
Loan Default Prediction using Multi-Layer Perceptron

Source assignment:
Marvellous Infosystems - Python Automation & Machine Learning
Deep Learning Assignment

IMPORTANT:
The assignment PDF specifies the dataset columns and tasks, but it does not
include the actual dataset values. Therefore, this program calculates all
dataset-dependent results when the CSV dataset is supplied.

Expected CSV columns:
Age, Income, LoanAmount, CreditScore, EmploymentYears,
ExistingLoans, MonthlyDebt, LoanTerm, PreviousDefault,
HomeOwnership, Default

Target:
Default
    0 -> Low default risk
    1 -> High default risk

Run:
    python loan_default_ann_assignment.py
or:
    python loan_default_ann_assignment.py path/to/your_dataset.csv
"""

# ============================================================
# Q1. Load and understand the dataset.
# ============================================================

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


EXPECTED_COLUMNS = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm",
    "PreviousDefault",
    "HomeOwnership",
    "Default",
]

TARGET_COLUMN = "Default"

# Change this filename if your dataset has a different name.
DEFAULT_DATASET = "loan_data.csv"


def load_dataset(file_path):
    """Load the CSV dataset and display its basic structure."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"\nDataset not found: {path}\n"
            "Place the CSV dataset in the same folder as this .py file, "
            "or run the program with the CSV path as an argument.\n"
        )

    df = pd.read_csv(path)

    print("\n" + "=" * 70)
    print("Q1. LOAD AND UNDERSTAND THE DATASET")
    print("=" * 70)

    print("\nDataset shape:", df.shape)
    print("\nFirst 5 records:")
    print(df.head())

    print("\nColumn names:")
    print(list(df.columns))

    print("\nData types:")
    print(df.dtypes)

    print("\nStatistical summary:")
    print(df.describe(include="all").transpose())

    missing_expected = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing_expected:
        raise ValueError(
            f"\nMissing expected columns: {missing_expected}\n"
            f"Available columns: {list(df.columns)}"
        )

    return df


# ============================================================
# Q2. Perform exploratory analysis.
# ============================================================

def exploratory_analysis(df):
    print("\n" + "=" * 70)
    print("Q2. EXPLORATORY ANALYSIS")
    print("=" * 70)

    print("\nDataset shape:", df.shape)

    print("\nUnique values:")
    for column in df.columns:
        print(f"{column}: {df[column].nunique(dropna=True)}")

    print("\nNumeric columns:")
    print(df.select_dtypes(include=np.number).columns.tolist())

    print("\nCategorical columns:")
    print(df.select_dtypes(exclude=np.number).columns.tolist())

    print("\nTarget distribution:")
    print(df[TARGET_COLUMN].value_counts(dropna=False))

    # Histograms for numeric features.
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    numeric_features = [
        column for column in numeric_columns if column != TARGET_COLUMN
    ]

    if numeric_features:
        df[numeric_features].hist(figsize=(14, 10), bins=20)
        plt.suptitle("Exploratory Analysis - Numeric Features")
        plt.tight_layout()
        plt.show()

    # Correlation matrix for numeric data.
    if len(numeric_columns) > 1:
        print("\nNumeric correlation matrix:")
        print(df[numeric_columns].corr().round(3))


# ============================================================
# Q3. Find missing values.
# ============================================================

def check_missing_values(df):
    print("\n" + "=" * 70)
    print("Q3. FIND MISSING VALUES")
    print("=" * 70)

    missing = df.isnull().sum()
    missing_percentage = (missing / len(df) * 100).round(2)

    missing_report = pd.DataFrame(
        {
            "MissingCount": missing,
            "MissingPercentage": missing_percentage,
        }
    )

    print(missing_report)

    if missing.sum() == 0:
        print("\nAnswer: No missing values are present.")
    else:
        print("\nAnswer: Missing values are present.")
        print("The preprocessing pipeline below handles numeric and categorical")
        print("missing values using median and most-frequent imputation.")


# ============================================================
# Q4. Check whether target classes are balanced.
# ============================================================

def check_class_balance(df):
    print("\n" + "=" * 70)
    print("Q4. CHECK WHETHER TARGET CLASSES ARE BALANCED")
    print("=" * 70)

    counts = df[TARGET_COLUMN].value_counts().sort_index()
    percentages = df[TARGET_COLUMN].value_counts(
        normalize=True
    ).sort_index() * 100

    balance_report = pd.DataFrame(
        {
            "Count": counts,
            "Percentage": percentages.round(2),
        }
    )

    print(balance_report)

    if len(counts) == 2:
        ratio = counts.min() / counts.max()

        if ratio >= 0.80:
            print(
                "\nAnswer: The classes are approximately balanced "
                "(minor difference between class sizes)."
            )
        else:
            print(
                "\nAnswer: The classes are imbalanced because one class "
                "has substantially more samples than the other."
            )
    else:
        print(
            "\nAnswer: The target does not contain exactly two classes. "
            "Inspect the target values before training."
        )

    return counts


# ============================================================
# Q5. Encode categorical variables.
# ============================================================

def identify_columns(df):
    """
    Identify numeric and categorical input columns.

    The assignment specifically describes:
      PreviousDefault -> Yes/No
      HomeOwnership   -> Rent/Own/Mortgage

    The code detects categorical columns automatically so it also works if
    the dataset contains additional categorical columns.
    """
    X = df.drop(columns=[TARGET_COLUMN])

    categorical_columns = X.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    numeric_columns = [
        column for column in X.columns
        if column not in categorical_columns
    ]

    return numeric_columns, categorical_columns


def build_preprocessor(numeric_columns, categorical_columns):
    """
    Q5/Q9:
    - Encode categorical variables using OneHotEncoder.
    - Scale numeric variables using StandardScaler.
    - Impute missing values before encoding/scaling.
    """
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    # Newer scikit-learn uses sparse_output; older versions use sparse.
    try:
        encoder = OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False,
        )
    except TypeError:
        encoder = OneHotEncoder(
            handle_unknown="ignore",
            sparse=False,
        )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", encoder),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ],
        remainder="drop",
    )

    return preprocessor


def encode_categorical_variables(df):
    print("\n" + "=" * 70)
    print("Q5. ENCODE CATEGORICAL VARIABLES")
    print("=" * 70)

    numeric_columns, categorical_columns = identify_columns(df)

    print("\nNumeric columns:")
    print(numeric_columns)

    print("\nCategorical columns:")
    print(categorical_columns)

    print(
        "\nAnswer: Categorical variables are encoded with OneHotEncoder. "
        "This converts values such as Yes/No and Rent/Own/Mortgage into "
        "numeric machine-learning features."
    )

    return numeric_columns, categorical_columns


# ============================================================
# Q6. Separate X and y.
# ============================================================

def separate_x_y(df):
    print("\n" + "=" * 70)
    print("Q6. SEPARATE X AND y")
    print("=" * 70)

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    print("X shape:", X.shape)
    print("y shape:", y.shape)

    print("\nX = input features")
    print("y = Default target")

    return X, y


# ============================================================
# Q7. Split dataset into training and testing data.
# ============================================================

def split_dataset(X, y):
    print("\n" + "=" * 70)
    print("Q7. SPLIT DATASET INTO TRAINING AND TESTING DATA")
    print("=" * 70)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("Training samples:", len(X_train))
    print("Testing samples :", len(X_test))
    print("Test size       : 20%")
    print("Random state    : 42")

    return X_train, X_test, y_train, y_test


# ============================================================
# Q8. Explain whether stratified splitting should be used.
# ============================================================

def explain_stratification():
    print("\n" + "=" * 70)
    print("Q8. SHOULD STRATIFIED SPLITTING BE USED?")
    print("=" * 70)

    print(
        """
Answer:
Yes, stratified splitting should be used for this classification problem.

Reason:
The target variable Default has two classes:
    0 -> Low default risk
    1 -> High default risk

Using stratify=y keeps approximately the same class proportion in both
training and testing sets. This is especially useful when the target
classes are imbalanced or when the dataset is not very large.

The code therefore uses:
    train_test_split(..., stratify=y)
"""
    )


# ============================================================
# Q9. Scale the features.
# ============================================================

def explain_scaling():
    print("\n" + "=" * 70)
    print("Q9. SCALE THE FEATURES")
    print("=" * 70)

    print(
        """
Answer:
MLP neural networks generally benefit from features being on comparable
scales. Age, Income, LoanAmount, CreditScore, MonthlyDebt, etc. can have
very different numeric ranges.

StandardScaler transforms numeric features approximately as:

    z = (x - mean) / standard_deviation

The preprocessing pipeline performs scaling using StandardScaler after
median imputation.
"""
    )


# ============================================================
# Q10. Create an MLPClassifier.
# ============================================================

def create_mlp(activation="relu", hidden_layer_sizes=(32, 16),
               learning_rate_init=0.001):
    """
    Assignment starting configuration:
        hidden_layer_sizes=(32, 16)
        activation='relu'
        solver='adam'
        max_iter=1000
        random_state=42

    learning_rate_init is explicitly supplied so Experiment 3 can change it.
    """
    return MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42,
        learning_rate_init=learning_rate_init,
    )


# ============================================================
# Q11. Train the model.
# ============================================================

def train_baseline_model(X_train, y_train, numeric_columns,
                         categorical_columns):
    print("\n" + "=" * 70)
    print("Q10. CREATE MLPCLASSIFIER")
    print("=" * 70)

    model = create_mlp()

    print(
        """
MLPClassifier configuration:
    hidden_layer_sizes=(32, 16)
    activation='relu'
    solver='adam'
    max_iter=1000
    random_state=42
    learning_rate_init=0.001
"""
    )

    preprocessor = build_preprocessor(
        numeric_columns,
        categorical_columns,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    print("\n" + "=" * 70)
    print("Q11. TRAIN THE MODEL")
    print("=" * 70)

    pipeline.fit(X_train, y_train)

    print("Baseline MLP model trained successfully.")

    return pipeline


# ============================================================
# Q12. Calculate accuracy.
# Q13. Generate confusion matrix.
# Q14. Generate classification report.
# Q15. Calculate precision, recall and F1-score.
# ============================================================

def evaluate_model(model, X_test, y_test, model_name="Baseline"):
    print("\n" + "=" * 70)
    print("Q12-Q15. MODEL EVALUATION")
    print("=" * 70)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test, predictions, zero_division=0
    )
    recall = recall_score(
        y_test, predictions, zero_division=0
    )
    f1 = f1_score(
        y_test, predictions, zero_division=0
    )

    cm = confusion_matrix(y_test, predictions)

    print(f"\nModel: {model_name}")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-score : {f1:.4f}")

    print("\nQ13. Confusion Matrix:")
    print(cm)

    print("\nQ14. Classification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=["Low default risk (0)", "High default risk (1)"],
            zero_division=0,
        )
    )

    return {
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1,
    }


# ============================================================
# Q16. Plot training loss.
# ============================================================

def plot_training_loss(model):
    print("\n" + "=" * 70)
    print("Q16. PLOT TRAINING LOSS")
    print("=" * 70)

    mlp = model.named_steps["model"]

    plt.figure(figsize=(8, 5))
    plt.plot(
        range(1, len(mlp.loss_curve_) + 1),
        mlp.loss_curve_,
    )
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss Curve")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(
        "Answer: The loss curve shows how the model's training loss "
        "changes across iterations."
    )


# ============================================================
# Q17. Test the model on new loan applicants.
# ============================================================

def test_new_applicant(model, X_columns):
    print("\n" + "=" * 70)
    print("Q17. TEST THE MODEL ON A NEW LOAN APPLICANT")
    print("=" * 70)

    # Example applicant created only to demonstrate prediction.
    # Replace these values with real applicant information.
    new_applicant = pd.DataFrame(
        [
            {
                "Age": 35,
                "Income": 750000,
                "LoanAmount": 250000,
                "CreditScore": 720,
                "EmploymentYears": 8,
                "ExistingLoans": 1,
                "MonthlyDebt": 15000,
                "LoanTerm": 60,
                "PreviousDefault": "No",
                "HomeOwnership": "Own",
            }
        ]
    )

    # Keep only the columns used by the training data and in the same order.
    new_applicant = new_applicant.reindex(columns=X_columns)

    prediction = model.predict(new_applicant)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(new_applicant)[0]
        high_default_probability = probability[1]
    else:
        high_default_probability = None

    print("\nNew applicant:")
    print(new_applicant.to_string(index=False))

    print("\nPrediction:", int(prediction))

    if prediction == 0:
        print("Result: 0 -> Low default risk")
    else:
        print("Result: 1 -> High default risk")

    if high_default_probability is not None:
        print(
            f"Predicted probability of high default risk: "
            f"{high_default_probability:.4f}"
        )

    print(
        "\nNote: This is a demonstration applicant. Replace the values "
        "inside new_applicant with the actual applicant's information."
    )


# ============================================================
# Hyperparameter Experiment
# Change one parameter at a time.
# ============================================================

def run_experiment(
    experiment_name,
    values,
    parameter_name,
    X_train,
    X_test,
    y_train,
    y_test,
    numeric_columns,
    categorical_columns,
):
    """
    Run one hyperparameter experiment while keeping all other baseline
    settings unchanged.
    """
    print("\n" + "=" * 70)
    print(experiment_name)
    print("=" * 70)

    results = []

    for value in values:
        kwargs = {
            "activation": "relu",
            "hidden_layer_sizes": (32, 16),
            "learning_rate_init": 0.001,
        }

        kwargs[parameter_name] = value

        model = create_mlp(**kwargs)

        preprocessor = build_preprocessor(
            numeric_columns,
            categorical_columns,
        )

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        result = {
            "Parameter": parameter_name,
            "Value": str(value),
            "Accuracy": accuracy_score(y_test, predictions),
            "Precision": precision_score(
                y_test, predictions, zero_division=0
            ),
            "Recall": recall_score(
                y_test, predictions, zero_division=0
            ),
            "F1": f1_score(
                y_test, predictions, zero_division=0
            ),
        }

        results.append(result)

        print(
            f"\n{parameter_name}={value} -> "
            f"Accuracy={result['Accuracy']:.4f}, "
            f"Precision={result['Precision']:.4f}, "
            f"Recall={result['Recall']:.4f}, "
            f"F1={result['F1']:.4f}"
        )

    results_df = pd.DataFrame(results)
    print("\nExperiment results:")
    print(results_df.to_string(index=False))

    return results_df


# ============================================================
# Main program
# ============================================================

def main():
    dataset_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DATASET

    try:
        df = load_dataset(dataset_path)
    except Exception as error:
        print(error)
        return

    # Q2
    exploratory_analysis(df)

    # Q3
    check_missing_values(df)

    # Q4
    check_class_balance(df)

    # Q5
    numeric_columns, categorical_columns = encode_categorical_variables(df)

    # Q6
    X, y = separate_x_y(df)

    # Q7
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Q8
    explain_stratification()

    # Q9
    explain_scaling()

    # Q10 + Q11
    baseline_model = train_baseline_model(
        X_train,
        y_train,
        numeric_columns,
        categorical_columns,
    )

    # Q12-Q15
    baseline_results = evaluate_model(
        baseline_model,
        X_test,
        y_test,
        model_name="Baseline (32,16) + ReLU",
    )

    # Q16
    plot_training_loss(baseline_model)

    # Q17
    test_new_applicant(
        baseline_model,
        X.columns.tolist(),
    )

    # ========================================================
    # Hyperparameter Experiment 1 - Activation
    # Assignment values:
    # identity, logistic, tanh, relu
    # ========================================================
    activation_results = run_experiment(
        experiment_name="EXPERIMENT 1 - ACTIVATION",
        values=["identity", "logistic", "tanh", "relu"],
        parameter_name="activation",
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
    )

    # ========================================================
    # Hyperparameter Experiment 2 - Hidden Layers
    # Assignment values:
    # (10,), (20,10), (50,25), (100,50,25)
    # ========================================================
    hidden_layer_results = run_experiment(
        experiment_name="EXPERIMENT 2 - HIDDEN LAYERS",
        values=[
            (10,),
            (20, 10),
            (50, 25),
            (100, 50, 25),
        ],
        parameter_name="hidden_layer_sizes",
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
    )

    # ========================================================
    # Hyperparameter Experiment 3 - Learning Rate
    # The assignment says to try different values.
    # ========================================================
    learning_rate_results = run_experiment(
        experiment_name="EXPERIMENT 3 - LEARNING RATE",
        values=[0.0001, 0.001, 0.01, 0.1],
        parameter_name="learning_rate_init",
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
    )

    # ========================================================
    # Final summary
    # ========================================================
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    print("\nBaseline metrics:")
    print(pd.DataFrame([baseline_results]).to_string(index=False))

    print(
        """
The experiment tables above should be used to compare the effect of
activation function, hidden-layer architecture, and learning rate.

No fixed accuracy/precision/recall/F1 values are hard-coded because the
assignment PDF does not contain the actual dataset records. The metrics are
calculated from the supplied dataset when this program is executed.
"""
    )


if __name__ == "__main__":
    main()
