# Marvellous Infosystems : Python - Automation & Machine Learning
# Deep Learning Assignment
#
# Format: Question -> Answer
# Based on the uploaded assignment PDF.

import math
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# QUESTION 1
# Write a Python program to simulate a single artificial neuron.
#
# Input:
# x1 = 2
# x2 = 3
# w1 = 0.4
# w2 = 0.6
# bias = 0.5
#
# Tasks:
# 1. Calculate weighted sum.
# 2. Apply sigmoid activation function.
# 3. Display final output.
# 4. Explain whether output is close to 0 or 1.
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 1 - SINGLE ARTIFICIAL NEURON")
print("=" * 60)

x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

weighted_sum = (x1 * w1) + (x2 * w2) + bias

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

output = sigmoid(weighted_sum)

print("Weighted Sum:", weighted_sum)
print("Sigmoid Output:", output)

if output > 0.5:
    print("Explanation: The output is closer to 1.")
else:
    print("Explanation: The output is closer to 0.")


# ============================================================
# QUESTION 2
# Write a Python program to demonstrate different activation
# functions.
#
# Functions:
# 1. Sigmoid
# 2. ReLU
# 3. Tanh
#
# Tasks:
# 1. Accept input values from -10 to 10.
# 2. Plot all activation functions using Matplotlib.
# 3. Explain the use of each activation function.
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 2 - ACTIVATION FUNCTIONS")
print("=" * 60)

# Input values from -10 to 10
x = np.linspace(-10, 10, 400)

# Activation functions
sigmoid_values = 1 / (1 + np.exp(-x))
relu_values = np.maximum(0, x)
tanh_values = np.tanh(x)

# Display a few calculated values
print("Input range: -10 to 10")
print("\nActivation function uses:")
print("1. Sigmoid: Produces values between 0 and 1 and is commonly")
print("   used for binary classification output.")
print("2. ReLU: Returns 0 for negative values and the input for")
print("   positive values. It is commonly used in hidden layers.")
print("3. Tanh: Produces values between -1 and 1 and is useful when")
print("   centered output around zero is desired.")

# Plot all activation functions
plt.figure(figsize=(10, 6))
plt.plot(x, sigmoid_values, label="Sigmoid")
plt.plot(x, relu_values, label="ReLU")
plt.plot(x, tanh_values, label="Tanh")

plt.title("Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.grid(True)
plt.legend()
plt.show()


# ============================================================
# QUESTION 3
# Write a Python program to calculate loss manually.
#
# Tasks:
# 1. Implement Mean Squared Error.
# 2. Implement Binary Cross Entropy.
# 3. Take actual and predicted values.
# 4. Display the calculated loss.
# 5. Explain which loss function is used for regression
#    and classification.
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 3 - LOSS FUNCTIONS")
print("=" * 60)

# Actual and predicted values
actual = np.array([1, 0, 1, 1])
predicted = np.array([0.9, 0.2, 0.8, 0.7])

def mean_squared_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)

def binary_cross_entropy(actual, predicted):
    # Small value to avoid log(0)
    epsilon = 1e-15
    predicted = np.clip(predicted, epsilon, 1 - epsilon)

    return -np.mean(
        actual * np.log(predicted) +
        (1 - actual) * np.log(1 - predicted)
    )

mse_loss = mean_squared_error(actual, predicted)
bce_loss = binary_cross_entropy(actual, predicted)

print("Actual Values:   ", actual)
print("Predicted Values:", predicted)
print("Mean Squared Error:", mse_loss)
print("Binary Cross Entropy:", bce_loss)

print("\nExplanation:")
print("MSE is commonly used for regression problems.")
print("Binary Cross Entropy is commonly used for binary classification.")


# ============================================================
# QUESTION 4
# Write a Python program to show how weights are updated in ANN.
#
# Tasks:
# 1. Take input, weight, bias, target output, and learning rate.
# 2. Calculate prediction.
# 3. Calculate error.
# 4. Update weight using gradient descent logic.
# 5. Display old weight and updated weight.
# ============================================================

print("\n" + "=" * 60)
print("QUESTION 4 - WEIGHT UPDATE IN ANN")
print("=" * 60)

# Input values
input_value = 2.0
weight = 0.5
bias = 0.1
target = 1.0
learning_rate = 0.1

# Calculate prediction
prediction = (input_value * weight) + bias

# Calculate error
error = target - prediction

# Gradient descent logic
# For a simple linear neuron:
# gradient = error * input
gradient = error * input_value

# Save old weight
old_weight = weight

# Update weight
weight = weight + (learning_rate * gradient)

print("Input:", input_value)
print("Old Weight:", old_weight)
print("Bias:", bias)
print("Target Output:", target)
print("Learning Rate:", learning_rate)
print("Prediction:", prediction)
print("Error:", error)
print("Gradient:", gradient)
print("Updated Weight:", weight)

print("\nExplanation:")
print("The weight is adjusted using the error and learning rate.")
print("Gradient descent changes the weight so that the prediction")
print("moves closer to the target output.")


# ============================================================
# END OF ASSIGNMENT
# ============================================================
