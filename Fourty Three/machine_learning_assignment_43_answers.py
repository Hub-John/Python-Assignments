"""
Machine Learning Assignment 43
Marvellous Infosystems : Python - Automation & Machine Learning

All assignment steps are answered in Step -> Answer sequence.

Requirements from the PDF:
- Load MarvellousInfosystems_PlayPredictor.csv
- Features: Wether and Temperature
- Target: Play
- Encode string fields using LabelEncoder
- Use K Nearest Neighbour classification
- Train on the whole dataset
- Use K = 3 for prediction
- Create CheckAccuracy()
- Split the dataset into two equal parts for accuracy testing
- Calculate accuracy by changing K
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ============================================================
# STEP 1: GET DATA
# ============================================================

FILE_NAME = "MarvellousInfosystems_PlayPredictor.csv"

try:
    data = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    raise FileNotFoundError(
        f"{FILE_NAME} not found. Put the CSV file in the same "
        "folder as this program."
    )

print("=" * 60)
print("STEP 1: GET DATA")
print("=" * 60)
print(data)
print("\nShape:", data.shape)
print("Columns:", list(data.columns))


# ============================================================
# STEP 2: CLEAN, PREPARE AND MANIPULATE DATA
# ============================================================

print("\n" + "=" * 60)
print("STEP 2: CLEAN, PREPARE AND MANIPULATE DATA")
print("=" * 60)

# The assignment spells the feature as "Wether".
# Also accept "Weather" if that is how the CSV is named.
if "Wether" in data.columns:
    weather_column = "Wether"
elif "Weather" in data.columns:
    weather_column = "Weather"
else:
    raise ValueError("CSV must contain Wether (or Weather).")

if "Temperature" not in data.columns:
    raise ValueError("CSV must contain Temperature.")

if "Play" not in data.columns:
    raise ValueError("CSV must contain Play.")

weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()
play_encoder = LabelEncoder()

data["Wether_Encoded"] = weather_encoder.fit_transform(
    data[weather_column].astype(str)
)
data["Temperature_Encoded"] = temperature_encoder.fit_transform(
    data["Temperature"].astype(str)
)
data["Play_Encoded"] = play_encoder.fit_transform(
    data["Play"].astype(str)
)

print("\nWether mapping:")
for label, value in zip(
    weather_encoder.classes_,
    weather_encoder.transform(weather_encoder.classes_)
):
    print(label, "->", value)

print("\nTemperature mapping:")
for label, value in zip(
    temperature_encoder.classes_,
    temperature_encoder.transform(temperature_encoder.classes_)
):
    print(label, "->", value)

print("\nPlay mapping:")
for label, value in zip(
    play_encoder.classes_,
    play_encoder.transform(play_encoder.classes_)
):
    print(label, "->", value)

X = data[["Wether_Encoded", "Temperature_Encoded"]]
y = data["Play_Encoded"]

print("\nPrepared data:")
print(data)


# ============================================================
# STEP 3: TRAIN DATA
# ============================================================

print("\n" + "=" * 60)
print("STEP 3: TRAIN DATA")
print("=" * 60)

K = 3

model = KNeighborsClassifier(n_neighbors=K)

# The PDF explicitly says to train using the whole dataset.
model.fit(X, y)

print("KNN model trained using the whole dataset.")
print("K =", K)


# ============================================================
# STEP 4: TEST DATA
# ============================================================

print("\n" + "=" * 60)
print("STEP 4: TEST DATA")
print("=" * 60)

print("Available Wether values:", list(weather_encoder.classes_))
print("Available Temperature values:",
      list(temperature_encoder.classes_))

weather_input = input(
    "\nEnter Wether (press Enter for Sunny): "
).strip()

temperature_input = input(
    "Enter Temperature (press Enter for Hot): "
).strip()

if not weather_input:
    weather_input = "Sunny"

if not temperature_input:
    temperature_input = "Hot"

if weather_input not in weather_encoder.classes_:
    raise ValueError(
        f"Invalid Wether '{weather_input}'. "
        f"Choose from {list(weather_encoder.classes_)}"
    )

if temperature_input not in temperature_encoder.classes_:
    raise ValueError(
        f"Invalid Temperature '{temperature_input}'. "
        f"Choose from {list(temperature_encoder.classes_)}"
    )

weather_value = weather_encoder.transform([weather_input])[0]
temperature_value = temperature_encoder.transform(
    [temperature_input]
)[0]

test_input = [[weather_value, temperature_value]]

prediction_encoded = model.predict(test_input)[0]
prediction = play_encoder.inverse_transform(
    [prediction_encoded]
)[0]

print("\nInput Wether      :", weather_input)
print("Input Temperature :", temperature_input)
print("Predicted result  :", prediction)


# ============================================================
# STEP 5: CALCULATE ACCURACY
# ============================================================

print("\n" + "=" * 60)
print("STEP 5: CALCULATE ACCURACY")
print("=" * 60)


def CheckAccuracy(k_value):
    """
    Divide the dataset into two equal parts for training/testing
    and return KNN accuracy for the supplied K.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.50,
        random_state=42
    )

    if k_value > len(X_train):
        raise ValueError(
            f"K={k_value} is larger than the training set size "
            f"({len(X_train)})."
        )

    accuracy_model = KNeighborsClassifier(
        n_neighbors=k_value
    )
    accuracy_model.fit(X_train, y_train)

    y_predicted = accuracy_model.predict(X_test)

    return accuracy_score(y_test, y_predicted)


print("\nAccuracy for different K values:")

# With the assignment dataset, a 50/50 split gives 5 training
# records, so these K values are valid.
for k_value in [1, 3, 5]:
    accuracy = CheckAccuracy(k_value)
    print(
        f"K = {k_value} -> "
        f"Accuracy = {accuracy * 100:.2f}%"
    )


# ============================================================
# Final result
# ============================================================

print("\n" + "=" * 60)
print("Assignment 43 completed successfully.")
print("=" * 60)
