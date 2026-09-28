
# Marvellous Infosystems : Python - Automation & Machine Learning
# Deep Learning Assignment 65
# Format: Question -> Answer

# ============================================================
# QUESTION 1
# Why flatten layer is required before dense layer?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1")
print("Why flatten layer is required before dense layer?")
print("=" * 70)

print("""
ANSWER:
A Flatten layer converts a multi-dimensional feature map into a
one-dimensional vector.

Convolution and pooling layers produce feature maps with dimensions
such as height, width, and channels. A Dense layer expects its input
in one-dimensional form.

Therefore, the Flatten layer connects the feature extraction part
of a CNN with the Dense layer used for classification or prediction.

Example:
Feature Map:
[1 2]
[3 4]

After Flatten:
[1, 2, 3, 4]
""")


# ============================================================
# QUESTION 2
# What is Fully Connected Layer in CNN?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2")
print("What is Fully Connected Layer in CNN?")
print("=" * 70)

print("""
ANSWER:
A Fully Connected Layer, also called a Dense layer, is a layer in
which every neuron is connected to every neuron in the previous
layer.

In a CNN, it usually receives flattened feature maps and combines
the learned features for classification or prediction.
""")


# ============================================================
# QUESTION 3
# Write all steps of CNN from image input to final prediction.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3")
print("Write all steps of CNN from image input to final prediction.")
print("=" * 70)

print("""
ANSWER:
1. Image Input
2. Convolution
3. Activation Function such as ReLU
4. Pooling
5. Repeat convolution and pooling as required
6. Flatten
7. Fully Connected / Dense Layer
8. Output Layer
9. Final Prediction

Flow:
Image -> Convolution -> ReLU -> Pooling -> Flatten
-> Dense -> Output -> Final Prediction
""")


# ============================================================
# QUESTION 4
# What is TensorFlow? Explain features.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 4")
print("What is TensorFlow? Explain features.")
print("=" * 70)

print("""
ANSWER:
TensorFlow is an open-source machine learning and deep learning
framework used to build, train, and deploy machine learning models.

Important features:
1. Tensor operations using multi-dimensional arrays.
2. Neural network and deep learning support.
3. Automatic differentiation for calculating gradients.
4. GPU and hardware acceleration.
5. Keras integration for model development.
6. Support for model deployment.
""")


# ============================================================
# QUESTION 5
# Differentiate scalar, vector, matrix, and tensor.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 5")
print("Differentiate scalar, vector, matrix, and tensor.")
print("=" * 70)

print("""
ANSWER:

Scalar:
A single value.
Example: 5

Vector:
A one-dimensional collection of values.
Example: [1, 2, 3]

Matrix:
A two-dimensional arrangement of values.
Example:
[[1, 2],
 [3, 4]]

Tensor:
A multi-dimensional array. Scalars, vectors, and matrices can be
considered tensors of different dimensions.
""")


# ============================================================
# QUESTION 6
# What is Sequential model in Keras?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 6")
print("What is Sequential model in Keras?")
print("=" * 70)

print("""
ANSWER:
The Sequential model in Keras creates a neural network as a simple
sequence of layers. Each layer is connected to the next layer.

Example code:
""")

print("""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
""")

print("""
The Sequential model is useful when the model has a straightforward
linear stack of layers.
""")


# ============================================================
# QUESTION 7
# What is Dense layer in Keras?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 7")
print("What is Dense layer in Keras?")
print("=" * 70)

print("""
ANSWER:
A Dense layer in Keras is a fully connected neural network layer.
Every neuron in a Dense layer is connected to all outputs from the
previous layer.

Example:
""")

print("""
from tensorflow.keras.layers import Dense

layer = Dense(10, activation='relu')
""")

print("""
Here, 10 is the number of neurons and ReLU is the activation
function.
""")


# ============================================================
# QUESTION 8
# Write code using Sigmoid in output layer.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 8")
print("Write code using Sigmoid in output layer.")
print("=" * 70)

print("""
ANSWER:
For binary classification, a Sigmoid activation can be used in the
output layer.

Example code:
""")

print("""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(16, activation='relu', input_shape=(10,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()
""")

print("""
The Sigmoid function produces an output between 0 and 1 and is
commonly used for binary classification.
""")


# ============================================================
# QUESTION 9
# Why Deep Learning requires large datasets?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 9")
print("Why Deep Learning requires large datasets?")
print("=" * 70)

print("""
ANSWER:
Deep Learning models usually contain many parameters that must be
learned from data.

Large datasets are useful because:
1. They provide more examples for learning patterns.
2. They provide a wider variety of training examples.
3. They can reduce overfitting when the data is representative.
4. They help complex neural networks learn useful features.
5. They can improve generalization to unseen examples.

Therefore, deep learning often benefits from large and diverse
datasets.
""")


# ============================================================
# QUESTION 10
# Why GPUs are used in Deep Learning?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 10")
print("Why GPUs are used in Deep Learning?")
print("=" * 70)

print("""
ANSWER:
GPUs (Graphics Processing Units) are widely used in Deep Learning
because neural networks require many mathematical operations,
especially matrix and tensor operations.

GPUs contain many processing units that can perform suitable
calculations in parallel.

Advantages:
1. Faster matrix and tensor calculations.
2. Parallel processing of many operations.
3. Faster neural network training.
4. Reduced training time for large models and datasets.
5. Useful acceleration for deep learning workloads.

Therefore, GPUs can significantly speed up suitable deep learning
computations.
""")


# ============================================================
# END OF ASSIGNMENT
# ============================================================
