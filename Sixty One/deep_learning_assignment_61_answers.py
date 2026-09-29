"""
Marvellous Infosystems
Python - Automation & Machine Learning
Deep Learning Assignment

Topic: Feed Forward Neural Network (FNN), Loss Functions,
Optimizers, Training Concepts and CNN

This file follows the exact question-answer sequence from the
attached assignment PDF.
"""

# ============================================================
# Q1. What is Feed Forward Neural Network (FNN)?
#     Explain architecture.
# ============================================================

print("""
Q1. What is Feed Forward Neural Network (FNN)? Explain architecture.

Answer:
A Feed Forward Neural Network (FNN) is an artificial neural network in
which information moves in one direction, from the input layer through
one or more hidden layers to the output layer.

Architecture:

    Input Layer
        |
        v
    Hidden Layer 1
        |
        v
    Hidden Layer 2
        |
        v
    Output Layer

Main components:

1. Input Layer:
   Receives the input features. For example, if a model has 4 input
   features, the input layer can contain 4 input neurons.

2. Hidden Layer(s):
   These layers contain neurons that perform weighted calculations and
   apply activation functions. Multiple hidden layers allow the network
   to learn complex patterns.

3. Output Layer:
   Produces the final prediction. The number and activation of output
   neurons depend on the problem, such as binary or multi-class
   classification.

Each connection has a weight, and neurons can also have a bias.
""")

# ============================================================
# Q2. Why is it called feed forward network?
# ============================================================

print("""
Q2. Why is it called feed forward network?

Answer:
It is called a Feed Forward Neural Network because information flows
forward only:

    Input -> Hidden Layer(s) -> Output

There are no connections that send information backward to an earlier
layer during the forward pass. The output of one layer becomes the input
to the next layer.

During training, backpropagation is used to send the error information
back through the network for calculating gradients. However, this does
not change the fact that the network's forward information flow is from
input to output.
""")

# ============================================================
# Q3. Explain working steps of FNN from input to output.
# ============================================================

print("""
Q3. Explain working steps of FNN from input to output.

Answer:
The main working steps are:

Step 1: Input
The input features are supplied to the input layer.

Step 2: Weighted Sum
Each neuron calculates a weighted sum of its inputs and adds a bias.

    z = w1*x1 + w2*x2 + ... + wn*xn + b

Step 3: Activation Function
The weighted sum is passed through an activation function.

    a = activation(z)

Common activation functions include ReLU, sigmoid and tanh.

Step 4: Forward Propagation
The activated values are passed from one layer to the next until the
output layer is reached.

Step 5: Output
The output layer produces the prediction, such as a probability for
binary classification.

Step 6: During Training
The prediction is compared with the actual target using a loss function.
The optimizer and backpropagation are then used to update the weights
and biases.
""")

# ============================================================
# Q4. Explain Mean Squared Error with example.
# ============================================================

print("""
Q4. Explain Mean Squared Error with example.

Answer:
Mean Squared Error (MSE) is a loss function commonly used for regression.
It measures the average of the squared differences between actual and
predicted values.

Formula:

             1
MSE = ----------------- * Sum((y_actual - y_predicted)^2)
             n

Example:

Actual values:
    [2, 4, 6]

Predicted values:
    [1, 5, 5]

Step 1: Calculate errors:

    2 - 1 = 1
    4 - 5 = -1
    6 - 5 = 1

Step 2: Square the errors:

    1^2  = 1
    (-1)^2 = 1
    1^2  = 1

Step 3: Calculate the average:

    MSE = (1 + 1 + 1) / 3
        = 1

Therefore, the Mean Squared Error is 1.

A lower MSE generally indicates that predictions are closer to the
actual values.
""")

# ============================================================
# Q5. What is Binary Cross Entropy loss function?
# ============================================================

print("""
Q5. What is Binary Cross Entropy loss function?

Answer:
Binary Cross Entropy (BCE) is a loss function commonly used for binary
classification problems, where the target has two possible classes,
usually 0 and 1.

Formula:

BCE = -[y*log(p) + (1-y)*log(1-p)]

Where:

    y = actual class (0 or 1)
    p = predicted probability of class 1

Example:

If the actual value is:

    y = 1

and the model predicts:

    p = 0.9

then:

    BCE = -log(0.9)
        approximately 0.105

A prediction close to the correct class gives a smaller loss, while a
confident incorrect prediction gives a much larger loss.
""")

# ============================================================
# Q6. What is optimizer in Deep Learning?
# ============================================================

print("""
Q6. What is optimizer in Deep Learning?

Answer:
An optimizer is an algorithm used to update the weights and biases of a
neural network during training so that the loss function is minimized.

The general idea is:

    New Weight = Old Weight - Learning Rate * Gradient

The gradient indicates how the loss changes with respect to a parameter.

Common optimizers include:

1. Gradient Descent
2. Stochastic Gradient Descent (SGD)
3. Adam
4. RMSprop

Adam is widely used because it combines ideas related to momentum and
adaptive learning rates.
""")

# ============================================================
# Q7. What is epoch in neural network training?
# ============================================================

print("""
Q7. What is epoch in neural network training?

Answer:
An epoch is one complete pass through the entire training dataset during
neural network training.

For example, if a training dataset contains 1,000 records and the model
processes all 1,000 records once, that represents one epoch.

Training for multiple epochs allows the neural network to repeatedly learn
from the training data and update its parameters.
""")

# ============================================================
# Q8. Differentiate epoch, batch size, and iteration.
# ============================================================

print("""
Q8. Differentiate epoch, batch size, and iteration.

Answer:

1. Epoch:
   One complete pass through the entire training dataset.

2. Batch Size:
   The number of training samples processed before the model performs
   one parameter update.

3. Iteration:
   One parameter-update step.

Relationship:

    Number of iterations per epoch
        = Number of training samples / Batch size

Example:

Suppose:
    Training samples = 1,000
    Batch size = 100
    Epochs = 10

Then:

    Iterations per epoch = 1,000 / 100 = 10

Total iterations:

    10 epochs * 10 iterations = 100 iterations

Table:

    Concept       Meaning
    ------------------------------------------------
    Epoch         One complete pass over the dataset
    Batch Size    Samples processed in one batch
    Iteration     One update of model parameters
""")

# ============================================================
# Q9. What is CNN? Why is it popular for image processing?
# ============================================================

print("""
Q9. What is CNN? Why is it popular for image processing?

Answer:
CNN stands for Convolutional Neural Network. It is a type of neural
network particularly designed to work effectively with data having a
grid-like structure, especially images.

A typical CNN can contain:

    Input Image
        |
        v
    Convolution Layer
        |
        v
    Activation Function
        |
        v
    Pooling Layer
        |
        v
    More Convolution/Pooling Layers
        |
        v
    Flatten
        |
        v
    Fully Connected Layer
        |
        v
    Output

Why CNN is popular for image processing:

1. It automatically learns useful visual features.
2. Early layers can learn simple patterns such as edges.
3. Deeper layers can learn more complex patterns.
4. Convolution uses local regions of the image.
5. Weight sharing reduces the number of parameters compared with a
   fully connected network operating directly on all image pixels.
6. Pooling can reduce spatial dimensions and computation.
""")

# ============================================================
# Q10. Why CNN performs better than ANN for image data?
# ============================================================

print("""
Q10. Why CNN performs better than ANN for image data?

Answer:
CNNs are generally better suited to image data because they preserve and
use the spatial structure of images.

Main reasons:

1. Local Connectivity:
   CNN filters examine small local regions rather than connecting every
   neuron to every pixel.

2. Parameter Sharing:
   The same filter weights are reused across different image locations.
   This greatly reduces the number of parameters.

3. Feature Extraction:
   CNNs automatically learn hierarchical features such as edges,
   textures, shapes and higher-level visual patterns.

4. Spatial Information:
   Convolution operations retain information about where patterns occur
   in the image.

5. Computational Efficiency:
   Because of local connections and shared weights, CNNs can process
   images more efficiently than a fully connected ANN with a comparable
   direct image input.

Therefore, although a standard ANN can be used for image data, CNNs are
specifically designed to exploit the structure of images and are usually
more suitable for image-processing tasks.
""")

# ============================================================
# Assignment completed
# ============================================================

print("""
============================================================
ASSIGNMENT COMPLETED
============================================================

All 10 questions have been answered in the same sequence as the
assignment PDF.
""")
