"""
Marvellous Infosystems - Deep Learning Assignment 60
Question-answer sequence: Activation Functions
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Q1. Explain Sigmoid activation function with graph.
# ============================================================
print("""
Q1. Explain Sigmoid activation function with graph.

Answer:
Sigmoid is an activation function that maps any real-valued input to
a value between 0 and 1.

Formula:
    sigma(x) = 1 / (1 + e^(-x))

Properties:
- Output range is (0, 1).
- It has an S-shaped curve.
- sigma(0) = 0.5.
- Large positive inputs approach 1.
- Large negative inputs approach 0.
- It is commonly used in binary-classification output layers.
""")

x = np.linspace(-10, 10, 400)
sigmoid = 1 / (1 + np.exp(-x))
plt.figure(figsize=(8, 5))
plt.plot(x, sigmoid)
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.xlabel("x")
plt.ylabel("sigma(x)")
plt.title("Sigmoid Activation Function")
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# Q2. Write advantages and disadvantages of Sigmoid function.
# ============================================================
print("""
Q2. Write advantages and disadvantages of Sigmoid function.

Answer:

Advantages:
1. Output is bounded between 0 and 1.
2. It is smooth and differentiable.
3. Its output can represent a probability in binary classification.
4. It is simple and easy to understand.

Disadvantages:
1. It can suffer from the vanishing-gradient problem.
2. It is not zero-centered.
3. Learning can become slow in deep networks.
4. It is generally not preferred for modern hidden layers.
""")


# ============================================================
# Q3. Explain Tanh activation function.
# ============================================================
print("""
Q3. Explain Tanh activation function.

Answer:
Tanh (Hyperbolic Tangent) maps an input to a value between -1 and +1.

Formula:
    tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

Properties:
1. Output range is (-1, +1).
2. It has an S-shaped curve.
3. tanh(0) = 0.
4. It is zero-centered.
5. It is differentiable.
6. It can also suffer from vanishing gradients for very large
   positive or negative inputs.
""")


# ============================================================
# Q4. Differentiate Sigmoid and Tanh activation functions.
# ============================================================
print("""
Q4. Differentiate Sigmoid and Tanh activation functions.

Answer:

Property              Sigmoid              Tanh
---------------------------------------------------------
Output range          (0, 1)               (-1, 1)
Zero-centered         No                    Yes
Value at x = 0        0.5                   0
Shape                  S-shaped              S-shaped
Vanishing gradient    Possible              Possible
Common use             Binary output         Some hidden layers/
                                             sequence models

Sigmoid is especially useful when a single output probability is needed
for binary classification. Tanh provides zero-centered outputs.
""")


# ============================================================
# Q5. Explain ReLU activation function with graph.
# ============================================================
print("""
Q5. Explain ReLU activation function with graph.

Answer:
ReLU stands for Rectified Linear Unit.

Formula:
    f(x) = max(0, x)

Therefore:
    x < 0  -> f(x) = 0
    x >= 0 -> f(x) = x

Properties:
1. Negative inputs produce 0.
2. Positive inputs pass through unchanged.
3. It is computationally simple.
4. It is widely used in hidden layers.
5. For positive inputs it helps reduce the vanishing-gradient problem.
""")

relu = np.maximum(0, x)
plt.figure(figsize=(8, 5))
plt.plot(x, relu)
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("ReLU Activation Function: f(x) = max(0, x)")
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# Q6. Why is ReLU commonly used in hidden layers?
# ============================================================
print("""
Q6. Why is ReLU commonly used in hidden layers?

Answer:
ReLU is commonly used because:

1. It is simple and fast to calculate.
2. It introduces non-linearity into the neural network.
3. For positive inputs its gradient is 1, which helps reduce
   vanishing-gradient problems.
4. It can produce sparse activations because negative inputs become 0.
5. It is generally more suitable for deep hidden layers than Sigmoid.

Limitation:
ReLU can suffer from the dying-ReLU problem when neurons remain in the
negative region. Variants such as Leaky ReLU can help with this issue.
""")


# ============================================================
# Q7. What is Softmax activation function?
# ============================================================
print("""
Q7. What is Softmax activation function?

Answer:
Softmax is an activation function commonly used in the output layer of
multiclass classification networks.

Formula:
    softmax(z_i) = e^(z_i) / sum(e^(z_j))

Properties:
1. Each output is between 0 and 1.
2. All output probabilities sum to 1.
3. The outputs can be interpreted as probabilities for the classes.
4. The class with the highest probability is commonly selected.

Example:
    Class A = 0.10
    Class B = 0.70
    Class C = 0.20

Sum = 1.00, so Class B has the highest predicted probability.
""")


# ============================================================
# Q8. Why Softmax is used in multiclass classification?
# ============================================================
print("""
Q8. Why Softmax is used in multiclass classification?

Answer:
Softmax converts the model's output scores into a probability
distribution across all classes.

For example:
    Cat   = 0.20
    Dog   = 0.65
    Horse = 0.15

The values sum to 1. This makes the output easy to interpret and allows
the class with the highest probability to be selected.

Softmax is commonly paired with a multiclass cross-entropy loss.
""")


# ============================================================
# Q9. Which activation function is commonly used for binary
#     classification output layer?
# ============================================================
print("""
Q9. Which activation function is commonly used for binary
classification output layer?

Answer:
Sigmoid is commonly used.

Reason:
It converts the model's output to a value between 0 and 1, which can
represent the probability of the positive class.

Typical configuration:
    Output neurons = 1
    Activation     = Sigmoid
    Common loss    = Binary Cross Entropy
""")


# ============================================================
# Q10. Which activation function is used for multiclass output layer?
# ============================================================
print("""
Q10. Which activation function is used for multiclass output layer?

Answer:
Softmax is commonly used when there are multiple mutually exclusive
classes.

Typical configuration:
    Number of output neurons = Number of classes
    Activation               = Softmax

Example:
    [0.10, 0.20, 0.60, 0.10]

The probabilities sum to 1, and the third class has the highest
probability.
""")


print("""
============================================================
ASSIGNMENT COMPLETED
============================================================
All 10 questions from the attached Assignment 60 PDF are answered in
Question -> Answer sequence. Running this file also displays the
requested Sigmoid and ReLU graphs.
""")
