# Marvellous Infosystems : Python - Automation & Machine Learning
# Deep Learning Assignment 68
# Format: Question -> Answer

# ============================================================
# QUESTION 1
# Write a Python program to manually perform convolution.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1 - MANUAL CONVOLUTION")
print("=" * 70)

# Input Image Matrix
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# 3x3 edge detection kernel
kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

rows = len(image)
cols = len(image[0])
kernel_size = len(kernel)

feature_map = []

print("\nImage:")
for row in image:
    print(row)

print("\nKernel:")
for row in kernel:
    print(row)

print("\nRegion Calculations:")

# Move the kernel over the image
for i in range(rows - kernel_size + 1):
    feature_row = []

    for j in range(cols - kernel_size + 1):
        region = [
            image[i + r][j:j + kernel_size]
            for r in range(kernel_size)
        ]

        total = 0
        calculations = []

        # Multiplication and addition
        for r in range(kernel_size):
            for c in range(kernel_size):
                multiplication = region[r][c] * kernel[r][c]
                total += multiplication
                calculations.append(
                    f"{region[r][c]}*{kernel[r][c]}"
                )

        print("\nRegion at row", i, "column", j)
        for row in region:
            print(row)

        print("Calculation:")
        print(" + ".join(calculations))
        print("Output =", total)

        feature_row.append(total)

    feature_map.append(feature_row)

print("\nFeature Map:")
for row in feature_map:
    print(row)

print("\nExpected Feature Map:")
print("[3, 3, 3]")
print("[0, 0, 0]")
print("[-3, -3, -3]")


# ============================================================
# QUESTION 2
# Write a Python program to demonstrate ReLU and Max Pooling.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2 - RELU AND MAX POOLING")
print("=" * 70)

# Input Feature Map
feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

print("\nInput Feature Map:")
for row in feature_map:
    print(row)

# Answer 1 and 2: Apply ReLU
# ReLU rule:
# If value < 0, convert it to 0.
# If value >= 0, keep it unchanged.

relu_output = []

for row in feature_map:
    relu_row = []

    for value in row:
        if value < 0:
            relu_row.append(0)
        else:
            relu_row.append(value)

    relu_output.append(relu_row)

print("\nAfter ReLU:")
for row in relu_output:
    print(row)

# Answer 3: Apply 2x2 Max Pooling
#
# Note:
# The provided assignment gives a 3x3 feature map but does not
# specify stride or padding. Using a standard 2x2 pooling window
# with stride 1 produces a 2x2 output.

pool_size = 2
stride = 1

pooled_output = []

for i in range(0, len(relu_output) - pool_size + 1, stride):
    pooled_row = []

    for j in range(0, len(relu_output[0]) - pool_size + 1, stride):
        region = [
            relu_output[i + r][j:j + pool_size]
            for r in range(pool_size)
        ]

        maximum = max(max(row) for row in region)
        pooled_row.append(maximum)

    pooled_output.append(pooled_row)

print("\nAfter 2x2 Max Pooling:")
for row in pooled_output:
    print(row)

# Answer 4 and 5
print("\nExplanation:")
print("Max Pooling selects the maximum value from each pooling region.")
print("Pooling reduces the spatial size of a feature map, which")
print("reduces computation and keeps important features.")


# ============================================================
# QUESTION 3
# Write a Python program to show flattening.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3 - FLATTENING")
print("=" * 70)

# Input Matrix
matrix = [
    [6, 4],
    [8, 6]
]

print("\nInput Matrix:")
for row in matrix:
    print(row)

# Answer 1 and 2: Convert 2D matrix into 1D vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("\nFlatten Output:")
print(flatten_output)

# Answer 3: Pass flattened vector to a fully connected layer
# Example weights and bias are selected to demonstrate the
# calculation manually because the assignment does not provide
# specific weights or bias.

weights = [0.1, 0.2, 0.3, 0.4]
bias = 0.5

weighted_sum = 0

for i in range(len(flatten_output)):
    weighted_sum += flatten_output[i] * weights[i]

final_output = weighted_sum + bias

print("\nFully Connected Layer:")
print("Flattened Input:", flatten_output)
print("Weights:", weights)
print("Bias:", bias)

print("\nManual Calculation:")
for i in range(len(flatten_output)):
    print(
        flatten_output[i],
        "*",
        weights[i],
        "=",
        flatten_output[i] * weights[i]
    )

print("Weighted Sum + Bias =", final_output)

# Answer 4 and 5
print("\nFinal Output:", final_output)

print("\nExplanation:")
print("A Flatten layer converts a multi-dimensional feature map")
print("into a one-dimensional vector.")
print("This vector can then be given to a fully connected layer")
print("for classification or prediction.")


# ============================================================
# END OF ASSIGNMENT
# ============================================================
