"""
Machine Learning Assignment 42
Manual KNN implementation - no machine-learning library.

Q1: Classify a new point using K=3.
Q2: Show how prediction changes for K=1, 3, 5.
Q3: Predict student Pass/Fail from study hours and attendance.

Note for Q2:
The PDF provides only 4 training points but asks for K=5.
Standard KNN requires K <= number of training points, so K=5 is
not mathematically valid for the supplied dataset. The program
reports this instead of inventing a fifth point.
"""

import math
from collections import Counter


# ============================================================
# Q1 - DATASET AND MANUAL KNN FUNCTIONS
# ============================================================

DATASET = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue"),
]


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_distances(dataset, new_x, new_y):
    distances = []

    for name, x, y, label in dataset:
        distance = euclidean_distance(new_x, new_y, x, y)
        distances.append((name, x, y, label, distance))

    distances.sort(key=lambda item: item[4])
    return distances


def knn_predict(dataset, new_x, new_y, k):
    if k <= 0:
        raise ValueError("K must be greater than zero.")

    if k > len(dataset):
        raise ValueError(
            f"K={k} is invalid because the dataset has only "
            f"{len(dataset)} points."
        )

    distances = calculate_distances(dataset, new_x, new_y)
    nearest = distances[:k]

    labels = [item[3] for item in nearest]
    votes = Counter(labels)
    prediction = votes.most_common(1)[0][0]

    return prediction, nearest


# ============================================================
# Q1. Accept X/Y, calculate distances, sort, select K=3,
#     and predict the class by majority voting.
# ============================================================

print("=" * 65)
print("Q1. MANUAL KNN CLASSIFICATION")
print("=" * 65)

print("\nDataset:")
print("Point   X   Y   Label")
for row in DATASET:
    print(f"{row[0]:<7}{row[1]:<4}{row[2]:<4}{row[3]}")

x_text = input("\nEnter X coordinate (Enter = 2): ").strip()
y_text = input("Enter Y coordinate (Enter = 2): ").strip()

new_x = float(x_text) if x_text else 2.0
new_y = float(y_text) if y_text else 2.0

distances = calculate_distances(DATASET, new_x, new_y)

print(f"\nNew point: ({new_x}, {new_y})")
print("\nSorted distances:")

for name, x, y, label, distance in distances:
    print(f"{name} - Distance: {distance:.2f} - Class: {label}")

prediction, nearest = knn_predict(DATASET, new_x, new_y, 3)

print("\nNearest Neighbors:")
for name, x, y, label, distance in nearest:
    print(f"{name} - Distance: {distance:.2f}")

print("Predicted Class:", prediction)


# ============================================================
# Q2. Predict the same point for K=1, K=3 and K=5 and explain.
# ============================================================

print("\n" + "=" * 65)
print("Q2. EFFECT OF CHANGING K")
print("=" * 65)

for k in [1, 3, 5]:
    try:
        result, nearest = knn_predict(DATASET, new_x, new_y, k)
        print(f"K = {k} -> {result}")
        print("Neighbors:", [n[0] for n in nearest])
    except ValueError as error:
        print(f"K = {k} -> Cannot calculate: {error}")

print("""
Explanation:
A small K gives more importance to the closest observations.
A larger K includes more observations, so farther points can
influence the majority vote and the prediction may change.

The assignment's expected output says K=5 -> Blue, but its Q1
dataset contains only four points (A, B, C and D). Standard KNN
cannot select five distinct nearest neighbors from four points.
Therefore this program correctly reports K=5 as invalid rather
than inventing a fifth training record.
""")


# ============================================================
# Q3. Student Pass/Fail using manual KNN.
#
# Dataset:
# 2 hours, 60% -> Fail
# 5 hours, 80% -> Pass
# 6 hours, 85% -> Pass
# 1 hour, 50% -> Fail
#
# K=3 is used because the PDF does not specify a K for Q3.
# ============================================================

print("\n" + "=" * 65)
print("Q3. STUDENT PASS/FAIL USING MANUAL KNN")
print("=" * 65)

STUDENTS = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail"),
]


def student_knn_predict(study_hours, attendance, k=3):
    if k > len(STUDENTS):
        raise ValueError("K is larger than the student dataset.")

    distances = []

    for hours, attend, result in STUDENTS:
        distance = math.sqrt(
            (study_hours - hours) ** 2
            + (attendance - attend) ** 2
        )
        distances.append((hours, attend, result, distance))

    distances.sort(key=lambda item: item[3])
    nearest = distances[:k]

    result = Counter(
        item[2] for item in nearest
    ).most_common(1)[0][0]

    return result, nearest


print("\nTraining data:")
print("Study Hours   Attendance   Result")
for hours, attend, result in STUDENTS:
    print(f"{hours:<14}{attend:<13}{result}")

study_text = input("\nEnter Study Hours (Enter = 4): ").strip()
attendance_text = input("Enter Attendance (Enter = 70): ").strip()

study_hours = float(study_text) if study_text else 4.0
attendance = float(attendance_text) if attendance_text else 70.0

student_result, student_neighbors = student_knn_predict(
    study_hours,
    attendance,
    k=3
)

print("\nNearest neighbors:")
for hours, attend, result, distance in student_neighbors:
    print(
        f"Study Hours={hours}, Attendance={attend}, "
        f"Result={result}, Distance={distance:.2f}"
    )

print("\nPredicted Result:", student_result)

# ============================================================
# End of Assignment 42
# ============================================================
