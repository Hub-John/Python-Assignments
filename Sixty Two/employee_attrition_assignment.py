"""
Marvellous Infosystems
Python - Automation & Machine Learning
Deep Learning Assignment

EMPLOYEE ATTRITION PREDICTION USING MLPCLASSIFIER

Assignment source:
The attached 2-page assignment asks us to create Employee_Attrition.csv
and build a Deep Learning-based Employee Attrition Prediction System using
MLPClassifier.

Target:
    0 -> Employee is likely to stay
    1 -> Employee is likely to leave

Expected CSV columns:
    Age
    MonthlyIncome
    YearsAtCompany
    TotalWorkingYears
    DistanceFromHome
    JobSatisfaction
    WorkLifeBalance
    OverTime
    NumCompaniesWorked
    TrainingTimesLastYear
    Attrition

Run:
    python employee_attrition_assignment.py

Or:
    python employee_attrition_assignment.py Employee_Attrition.csv
"""

# ==============================================================
# Imports
# ==============================================================

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# ==============================================================
# Configuration
# ==============================================================

DEFAULT_DATASET = "Employee_Attrition.csv"

EXPECTED_COLUMNS = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "TotalWorkingYears",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "OverTime",
    "NumCompaniesWorked",
    "TrainingTimesLastYear",
    "Attrition",
]

TARGET_COLUMN = "Attrition"


# ==============================================================
# Q1. Load the dataset using Pandas.
# ==============================================================

def load_dataset(file_path):
    """
    Q1 Answer:
    Load Employee_Attrition.csv using Pandas.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"\nDataset file not found: {path}\n"
            "Create Employee_Attrition.csv in the same folder as this "
            "Python file, or pass the CSV path as a command-line argument.\n"
        )

    df = pd.read_csv(path)

    print("\n" + "=" * 75)
    print("Q1. LOAD THE DATASET USING PANDAS")
    print("=" * 75)

    print("Dataset loaded successfully.")
    print("File:", path)

    return df


# ==============================================================
# Q2. Display the shape, columns and first five records.
# ==============================================================

def display_dataset_information(df):
    """
    Q2 Answer:
    Display shape, column names and first five records.
    """
    print("\n" + "=" * 75)
    print("Q2. DISPLAY SHAPE, COLUMNS AND FIRST FIVE RECORDS")
    print("=" * 75)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst five records:")
    print(df.head())


# ==============================================================
# Q3. Check for missing values.
# ==============================================================

def check_missing_values(df):
    """
    Q3 Answer:
    Check the number and percentage of missing values in every column.
    """
    print("\n" + "=" * 75)
    print("Q3. CHECK FOR MISSING VALUES")
    print("=" * 75)

    missing_count = df.isnull().sum()
    missing_percentage = (
        df.isnull().mean() * 100
    ).round(2)

    missing_report = pd.DataFrame(
        {
            "MissingCount": missing_count,
            "MissingPercentage": missing_percentage,
        }
    )

    print(missing_report)

    if missing_count.sum() == 0:
        print("\nAnswer: No missing values are present.")
    else:
        print(
            "\nAnswer: Missing values are present. "
            "The preprocessing pipeline uses median imputation for "
            "numeric columns and most-frequent imputation for categorical "
            "columns."
        )


# ==============================================================
# Q4. Identify numerical and categorical features.
# ==============================================================

def identify_features(df):
    """
    Q4 Answer:
    Identify numerical and categorical input features.

    The assignment explicitly describes OverTime as Yes/No.
    The code detects categorical columns from the actual CSV so it remains
    usable if another categorical feature is added.
    """
    print("\n" + "=" * 75)
    print("Q4. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES")
    print("=" * 75)

    X = df.drop(columns=[TARGET_COLUMN])

    categorical_features = X.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    numerical_features = [
        column
        for column in X.columns
        if column not in categorical_features
    ]

    print("\nNumerical features:")
    print(numerical_features)

    print("\nCategorical features:")
    print(categorical_features)

    return numerical_features, categorical_features


# ==============================================================
# Q5. Convert categorical features such as OverTime into
#     numerical representation.
# ==============================================================

def create_encoder():
    """
    Create a OneHotEncoder compatible with different scikit-learn versions.
    """
    try:
        return OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False,
        )
    except TypeError:
        # Compatibility with older scikit-learn versions.
        return OneHotEncoder(
            handle_unknown="ignore",
            sparse=False,
        )


def build_preprocessor(numerical_features, categorical_features):
    """
    Q5 Answer:
    Convert categorical features to numerical representation using
    OneHotEncoder.

    Example:
        OverTime = Yes / No

    becomes numerical one-hot encoded columns.
    """

    numerical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", create_encoder()),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numerical_pipeline,
                numerical_features,
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features,
            ),
        ],
        remainder="drop",
    )

    return preprocessor


def explain_categorical_encoding():
    print("\n" + "=" * 75)
    print("Q5. CONVERT CATEGORICAL FEATURES INTO NUMERICAL REPRESENTATION")
    print("=" * 75)

    print(
        """
Answer:
Categorical values cannot be directly used by the MLP as text.
Therefore, OneHotEncoder is used.

For example:
    OverTime = Yes / No

is converted into numerical encoded columns.

handle_unknown='ignore' is used so prediction does not fail if an
unseen category occurs in new employee data.
"""
    )


# ==============================================================
# Q6. Convert target Attrition into 0 and 1.
# ==============================================================

def encode_target(df):
    """
    Q6 Answer:
    Convert Attrition:
        No  -> 0 (likely to stay)
        Yes -> 1 (likely to leave)

    The function also handles datasets where the target is already 0/1.
    """
    print("\n" + "=" * 75)
    print("Q6. CONVERT ATTRITION INTO 0 AND 1")
    print("=" * 75)

    target = df[TARGET_COLUMN].copy()

    # Handle string targets.
    if target.dtype == "object" or str(target.dtype) == "category":
        normalized = target.astype(str).str.strip().str.lower()

        mapping = {
            "no": 0,
            "yes": 1,
            "0": 0,
            "1": 1,
        }

        unknown_values = sorted(
            set(normalized.dropna().unique()) - set(mapping.keys())
        )

        if unknown_values:
            raise ValueError(
                "Unknown Attrition values found: "
                f"{unknown_values}. Expected Yes/No or 0/1."
            )

        y = normalized.map(mapping).astype(int)

    else:
        y = pd.to_numeric(target, errors="raise").astype(int)

        invalid_values = sorted(set(y.unique()) - {0, 1})

        if invalid_values:
            raise ValueError(
                "Attrition target must contain only 0 and 1. "
                f"Found: {invalid_values}"
            )

    print("Target mapping:")
    print("    No  -> 0 -> Employee is likely to stay")
    print("    Yes -> 1 -> Employee is likely to leave")

    print("\nEncoded target distribution:")
    print(y.value_counts().sort_index())

    return y


# ==============================================================
# Q7. Separate independent and dependent variables.
# ==============================================================

def separate_x_y(df, y):
    """
    Q7 Answer:
        X = independent/input variables
        y = dependent/target variable
    """
    print("\n" + "=" * 75)
    print("Q7. SEPARATE INDEPENDENT AND DEPENDENT VARIABLES")
    print("=" * 75)

    X = df.drop(columns=[TARGET_COLUMN]).copy()

    print("Independent variable X shape:", X.shape)
    print("Dependent variable y shape   :", y.shape)

    print("\nIndependent variables:")
    print(X.columns.tolist())

    print("\nDependent variable:")
    print(TARGET_COLUMN)

    return X, y


# ==============================================================
# Q8. Divide the dataset into training and testing data.
# ==============================================================

def split_data(X, y):
    """
    Q8 Answer:
    Divide the dataset into training and testing data.

    80% -> training
    20% -> testing

    stratify=y keeps target-class proportions approximately consistent
    between the training and testing sets.
    """
    print("\n" + "=" * 75)
    print("Q8. DIVIDE DATASET INTO TRAINING AND TESTING DATA")
    print("=" * 75)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("Training samples:", len(X_train))
    print("Testing samples :", len(X_test))
    print("Training size   : 80%")
    print("Testing size    : 20%")
    print("Random state    : 42")

    return X_train, X_test, y_train, y_test


# ==============================================================
# Q9. Apply appropriate feature scaling.
# ==============================================================

def explain_feature_scaling():
    """
    Q9 Answer:
    StandardScaler is used for numerical features.

    Scaling is included inside the Pipeline so that statistics are learned
    from the training data only and then applied to the test/new data.
    """
    print("\n" + "=" * 75)
    print("Q9. APPLY APPROPRIATE FEATURE SCALING")
    print("=" * 75)

    print(
        """
Answer:
StandardScaler is used for numerical features.

It transforms each numerical feature approximately as:

    z = (x - mean) / standard_deviation

Feature scaling is important for an MLP because the input variables can
have very different numerical ranges, such as Age, MonthlyIncome and
DistanceFromHome.

The scaler is fitted through the training pipeline and then applied to
testing/new records.
"""
    )


# ==============================================================
# Q10. Design an MLP with at least two hidden layers.
# ==============================================================

def create_mlp():
    """
    Q10 Answer:
    Design an MLP with two hidden layers.

    Architecture:
        Input
          |
        32 neurons
          |
        16 neurons
          |
        Output
    """
    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42,
    )

    print("\n" + "=" * 75)
    print("Q10. DESIGN AN MLP WITH AT LEAST TWO HIDDEN LAYERS")
    print("=" * 75)

    print(
        """
MLP architecture:
    Hidden Layer 1 -> 32 neurons
    Hidden Layer 2 -> 16 neurons

Configuration:
    activation = 'relu'
    solver = 'adam'
    max_iter = 1000
    random_state = 42
"""
    )

    return model


# ==============================================================
# Q11. Train the network.
# ==============================================================

def train_network(
    X_train,
    y_train,
    numerical_features,
    categorical_features,
):
    """
    Q11 Answer:
    Build preprocessing + MLP pipeline and train it.
    """
    print("\n" + "=" * 75)
    print("Q11. TRAIN THE NETWORK")
    print("=" * 75)

    preprocessor = build_preprocessor(
        numerical_features,
        categorical_features,
    )

    model = create_mlp()

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(X_train, y_train)

    print("Network trained successfully.")

    return pipeline


# ==============================================================
# Q12. Display the number of iterations required for training.
# ==============================================================

def display_iterations(model):
    """
    Q12 Answer:
    Read n_iter_ from the trained MLPClassifier.
    """
    print("\n" + "=" * 75)
    print("Q12. NUMBER OF ITERATIONS REQUIRED FOR TRAINING")
    print("=" * 75)

    mlp = model.named_steps["model"]

    print("Number of iterations:", mlp.n_iter_)

    print(
        "\nAnswer: The value above is the number of training iterations "
        "actually used by MLPClassifier."
    )


# ==============================================================
# Q13. Calculate training accuracy.
# ==============================================================

def calculate_training_accuracy(model, X_train, y_train):
    """
    Q13 Answer:
    Calculate accuracy on training data.
    """
    print("\n" + "=" * 75)
    print("Q13. TRAINING ACCURACY")
    print("=" * 75)

    train_predictions = model.predict(X_train)
    train_accuracy = accuracy_score(
        y_train,
        train_predictions,
    )

    print(f"Training accuracy: {train_accuracy:.4f}")
    print(f"Training accuracy: {train_accuracy * 100:.2f}%")

    return train_accuracy


# ==============================================================
# Q14. Calculate testing accuracy.
# ==============================================================

def calculate_testing_accuracy(model, X_test, y_test):
    """
    Q14 Answer:
    Calculate accuracy on testing data.
    """
    print("\n" + "=" * 75)
    print("Q14. TESTING ACCURACY")
    print("=" * 75)

    test_predictions = model.predict(X_test)
    test_accuracy = accuracy_score(
        y_test,
        test_predictions,
    )

    print(f"Testing accuracy: {test_accuracy:.4f}")
    print(f"Testing accuracy: {test_accuracy * 100:.2f}%")

    return test_accuracy


# ==============================================================
# Q15. Generate a confusion matrix.
# ==============================================================

def generate_confusion_matrix(model, X_test, y_test):
    """
    Q15 Answer:
    Generate and display a confusion matrix.
    """
    print("\n" + "=" * 75)
    print("Q15. CONFUSION MATRIX")
    print("=" * 75)

    predictions = model.predict(X_test)

    cm = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1],
    )

    cm_df = pd.DataFrame(
        cm,
        index=[
            "Actual 0 - Stay",
            "Actual 1 - Leave",
        ],
        columns=[
            "Predicted 0 - Stay",
            "Predicted 1 - Leave",
        ],
    )

    print(cm_df)

    print(
        """
Interpretation:
    True Negative  -> Actual 0, Predicted 0
    False Positive -> Actual 0, Predicted 1
    False Negative -> Actual 1, Predicted 0
    True Positive  -> Actual 1, Predicted 1
"""
    )

    return cm


# ==============================================================
# Q16. Plot the loss curve.
# ==============================================================

def plot_loss_curve(model):
    """
    Q16 Answer:
    Plot MLP training loss over iterations.
    """
    print("\n" + "=" * 75)
    print("Q16. LOSS CURVE")
    print("=" * 75)

    mlp = model.named_steps["model"]

    plt.figure(figsize=(9, 5))

    plt.plot(
        range(1, len(mlp.loss_curve_) + 1),
        mlp.loss_curve_,
    )

    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("Employee Attrition MLP - Training Loss Curve")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(
        "Answer: The loss curve shows how training loss changes "
        "as the MLP learns."
    )


# ==============================================================
# Q17. Create a function: PredictAttrition(employee_data)
# ==============================================================

# The global model/X columns are deliberately assigned after training.
# This keeps the required function name exactly as specified in the
# assignment while allowing it to use the trained pipeline.

TRAINED_MODEL = None
TRAINING_FEATURE_COLUMNS = None


def PredictAttrition(employee_data):
    """
    Q17 Answer:
    PredictAttrition(employee_data)

    employee_data can be:
      - one dictionary
      - a pandas DataFrame
      - a list of dictionaries

    Returns:
      0 -> Employee is likely to stay
      1 -> Employee is likely to leave

    If predict_proba is available, the function also displays the predicted
    probability for each class.
    """
    if TRAINED_MODEL is None:
        raise RuntimeError(
            "Model is not trained yet. Run main() first."
        )

    if isinstance(employee_data, dict):
        employee_df = pd.DataFrame([employee_data])

    elif isinstance(employee_data, pd.DataFrame):
        employee_df = employee_data.copy()

    elif isinstance(employee_data, list):
        employee_df = pd.DataFrame(employee_data)

    else:
        raise TypeError(
            "employee_data must be a dictionary, DataFrame, "
            "or list of dictionaries."
        )

    # Ensure exactly the same input feature order used during training.
    employee_df = employee_df.reindex(
        columns=TRAINING_FEATURE_COLUMNS
    )

    predictions = TRAINED_MODEL.predict(employee_df)

    if hasattr(TRAINED_MODEL, "predict_proba"):
        probabilities = TRAINED_MODEL.predict_proba(employee_df)
    else:
        probabilities = None

    results = []

    for index, prediction in enumerate(predictions):
        prediction = int(prediction)

        if prediction == 0:
            result_text = "Employee is likely to stay"
        else:
            result_text = "Employee is likely to leave"

        result = {
            "Prediction": prediction,
            "Result": result_text,
        }

        if probabilities is not None:
            result["StayProbability"] = probabilities[index][0]
            result["LeaveProbability"] = probabilities[index][1]

        results.append(result)

    return pd.DataFrame(results)


# ==============================================================
# Q18. Test the system using at least five new employee records.
# ==============================================================

def test_five_new_employees():
    """
    Q18 Answer:
    Test PredictAttrition() using five new employee records.

    These are demonstration records. Replace their values with actual
    employee information when using the system.
    """
    print("\n" + "=" * 75)
    print("Q18. TEST USING FIVE NEW EMPLOYEE RECORDS")
    print("=" * 75)

    new_employees = pd.DataFrame(
        [
            {
                "Age": 29,
                "MonthlyIncome": 3500,
                "YearsAtCompany": 2,
                "TotalWorkingYears": 6,
                "DistanceFromHome": 18,
                "JobSatisfaction": 2,
                "WorkLifeBalance": 2,
                "OverTime": "Yes",
                "NumCompaniesWorked": 3,
                "TrainingTimesLastYear": 2,
            },
            {
                "Age": 41,
                "MonthlyIncome": 7000,
                "YearsAtCompany": 10,
                "TotalWorkingYears": 17,
                "DistanceFromHome": 5,
                "JobSatisfaction": 4,
                "WorkLifeBalance": 4,
                "OverTime": "No",
                "NumCompaniesWorked": 2,
                "TrainingTimesLastYear": 4,
            },
            {
                "Age": 25,
                "MonthlyIncome": 2800,
                "YearsAtCompany": 1,
                "TotalWorkingYears": 3,
                "DistanceFromHome": 25,
                "JobSatisfaction": 2,
                "WorkLifeBalance": 1,
                "OverTime": "Yes",
                "NumCompaniesWorked": 2,
                "TrainingTimesLastYear": 1,
            },
            {
                "Age": 35,
                "MonthlyIncome": 5200,
                "YearsAtCompany": 7,
                "TotalWorkingYears": 12,
                "DistanceFromHome": 8,
                "JobSatisfaction": 3,
                "WorkLifeBalance": 3,
                "OverTime": "No",
                "NumCompaniesWorked": 3,
                "TrainingTimesLastYear": 3,
            },
            {
                "Age": 50,
                "MonthlyIncome": 9000,
                "YearsAtCompany": 15,
                "TotalWorkingYears": 25,
                "DistanceFromHome": 3,
                "JobSatisfaction": 4,
                "WorkLifeBalance": 4,
                "OverTime": "No",
                "NumCompaniesWorked": 1,
                "TrainingTimesLastYear": 5,
            },
        ]
    )

    print("\nFive new employee records:")
    print(new_employees.to_string(index=False))

    predictions = PredictAttrition(new_employees)

    print("\nPredictions:")
    print(predictions.to_string(index=False))

    print(
        """
Prediction meaning:
    0 -> Employee is likely to stay
    1 -> Employee is likely to leave
"""
    )

    return predictions


# ==============================================================
# Q19. Explain whether the model is suffering from overfitting
#      or underfitting.
# ==============================================================

def explain_fit(train_accuracy, test_accuracy):
    """
    Q19 Answer:
    Compare training and testing accuracy.

    This is a simple practical diagnostic:
      - Training and testing both low -> possible underfitting.
      - Training substantially higher than testing -> possible overfitting.
      - Training and testing reasonably close and good -> less evidence
        of strong overfitting/underfitting.

    Important:
    There is no actual dataset in the assignment PDF, so a final
    dataset-specific conclusion cannot be known until the CSV is supplied
    and the program is executed.
    """
    print("\n" + "=" * 75)
    print("Q19. OVERFITTING OR UNDERFITTING")
    print("=" * 75)

    gap = train_accuracy - test_accuracy

    print(f"Training accuracy: {train_accuracy:.4f}")
    print(f"Testing accuracy : {test_accuracy:.4f}")
    print(f"Accuracy gap     : {gap:.4f}")

    # A simple diagnostic threshold, not a universal rule.
    if train_accuracy < 0.70 and test_accuracy < 0.70:
        conclusion = "Possible underfitting."
    elif gap > 0.10:
        conclusion = "Possible overfitting."
    else:
        conclusion = (
            "No strong evidence of severe overfitting or underfitting "
            "from this simple accuracy comparison."
        )

    print("\nDiagnostic:", conclusion)

    print(
        """
Explanation:
    Underfitting usually means the model is not learning enough from the
    training data, resulting in relatively low training and testing scores.

    Overfitting usually means the model learns the training data very well
    but performs noticeably worse on unseen testing data.

    The exact conclusion depends on the actual Employee_Attrition.csv
    dataset and the resulting training/testing metrics.
"""
    )


# ==============================================================
# Main program
# ==============================================================

def main():
    global TRAINED_MODEL
    global TRAINING_FEATURE_COLUMNS

    # Accept a custom CSV path from the command line.
    dataset_path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else DEFAULT_DATASET
    )

    try:
        # ------------------------------------------------------
        # Q1
        # ------------------------------------------------------
        df = load_dataset(dataset_path)

        # Verify expected assignment columns.
        missing_columns = [
            column
            for column in EXPECTED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                "\nThe dataset is missing these expected columns:\n"
                f"{missing_columns}\n\n"
                f"Expected columns:\n{EXPECTED_COLUMNS}"
            )

        # ------------------------------------------------------
        # Q2
        # ------------------------------------------------------
        display_dataset_information(df)

        # ------------------------------------------------------
        # Q3
        # ------------------------------------------------------
        check_missing_values(df)

        # ------------------------------------------------------
        # Q4
        # ------------------------------------------------------
        numerical_features, categorical_features = identify_features(df)

        # ------------------------------------------------------
        # Q5
        # ------------------------------------------------------
        explain_categorical_encoding()

        # ------------------------------------------------------
        # Q6
        # ------------------------------------------------------
        y = encode_target(df)

        # ------------------------------------------------------
        # Q7
        # ------------------------------------------------------
        X, y = separate_x_y(df, y)

        # ------------------------------------------------------
        # Q8
        # ------------------------------------------------------
        X_train, X_test, y_train, y_test = split_data(X, y)

        # ------------------------------------------------------
        # Q9
        # ------------------------------------------------------
        explain_feature_scaling()

        # ------------------------------------------------------
        # Q10
        # ------------------------------------------------------
        # The actual MLP object is created inside train_network().
        # This call displays the required architecture.
        create_mlp()

        # ------------------------------------------------------
        # Q11
        # ------------------------------------------------------
        TRAINED_MODEL = train_network(
            X_train,
            y_train,
            numerical_features,
            categorical_features,
        )

        TRAINING_FEATURE_COLUMNS = X.columns.tolist()

        # ------------------------------------------------------
        # Q12
        # ------------------------------------------------------
        display_iterations(TRAINED_MODEL)

        # ------------------------------------------------------
        # Q13
        # ------------------------------------------------------
        train_accuracy = calculate_training_accuracy(
            TRAINED_MODEL,
            X_train,
            y_train,
        )

        # ------------------------------------------------------
        # Q14
        # ------------------------------------------------------
        test_accuracy = calculate_testing_accuracy(
            TRAINED_MODEL,
            X_test,
            y_test,
        )

        # ------------------------------------------------------
        # Q15
        # ------------------------------------------------------
        generate_confusion_matrix(
            TRAINED_MODEL,
            X_test,
            y_test,
        )

        # ------------------------------------------------------
        # Q16
        # ------------------------------------------------------
        plot_loss_curve(TRAINED_MODEL)

        # ------------------------------------------------------
        # Q17 + Q18
        # ------------------------------------------------------
        test_five_new_employees()

        # ------------------------------------------------------
        # Q19
        # ------------------------------------------------------
        explain_fit(
            train_accuracy,
            test_accuracy,
        )

        print("\n" + "=" * 75)
        print("ASSIGNMENT COMPLETED")
        print("=" * 75)

    except Exception as error:
        print("\nERROR:")
        print(error)


if __name__ == "__main__":
    main()
