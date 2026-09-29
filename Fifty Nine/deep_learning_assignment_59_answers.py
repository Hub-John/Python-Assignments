"""
Marvellous Infosystems
Python - Automation & Machine Learning
Deep Learning Assignment 59

Topic: Neural Network Layers

This file follows the exact question-answer sequence from the
attached assignment PDF.
"""

# ============================================================
# Q1. What is Input Layer? Explain its role in ANN.
# ============================================================

print("""
Q1. What is Input Layer? Explain its role in ANN.

Answer:
The Input Layer is the first layer of an Artificial Neural Network (ANN).
It receives the input features or data that are given to the neural
network.

For example, if a model uses three features:

    Age
    Salary
    Experience

then the input layer can have three input neurons.

Role of the Input Layer:
1. Receives input features.
2. Represents the input data in the neural network.
3. Passes the input values to the first hidden layer, if hidden layers
   are present.
4. It defines the number of input features that the network expects.

The input layer generally does not perform complex learning operations;
the main computation happens in subsequent layers.
""")


# ============================================================
# Q2. What is Hidden Layer? Why is it called hidden?
# ============================================================

print("""
Q2. What is Hidden Layer? Why is it called hidden?

Answer:
A Hidden Layer is a layer of neurons located between the input layer and
the output layer of a neural network.

It is called "hidden" because its neurons and their intermediate
calculations are not directly visible as the input or final output of
the network.

A hidden layer typically performs:

    Weighted Sum -> Bias Addition -> Activation Function

For example:

    z = w1*x1 + w2*x2 + b
    output = activation(z)

A neural network can have one or more hidden layers.
""")


# ============================================================
# Q3. What is Output Layer? Explain its purpose.
# ============================================================

print("""
Q3. What is Output Layer? Explain its purpose.

Answer:
The Output Layer is the final layer of a neural network. It produces the
model's final prediction or result.

Its structure and activation function depend on the problem.

Examples:

1. Binary Classification:
   Usually one output neuron with a Sigmoid activation function.

2. Multiclass Classification:
   Usually one output neuron per class with Softmax activation.

3. Regression:
   Often one output neuron with a suitable output activation, commonly
   a linear output.

Therefore, the output layer converts the information learned by the
network into the required prediction.
""")


# ============================================================
# Q4. Why are hidden layers important in Deep Learning?
# ============================================================

print("""
Q4. Why are hidden layers important in Deep Learning?

Answer:
Hidden layers are important because they allow a neural network to learn
complex patterns and relationships from data.

Their importance includes:

1. They perform transformations of the input data.
2. They introduce non-linearity through activation functions.
3. Multiple hidden layers can learn hierarchical representations.
4. Earlier layers can learn simpler patterns.
5. Deeper layers can combine simpler patterns into more complex features.

For example, in image recognition:

    Edges -> Shapes -> Parts -> Objects

Thus, hidden layers are a major reason deep neural networks can solve
complex problems that a simple linear model cannot solve.
""")


# ============================================================
# Q5. How many hidden layers make a network "Deep"?
# ============================================================

print("""
Q5. How many hidden layers make a network "Deep"?

Answer:
There is no single universal numerical boundary that defines exactly how
many hidden layers make a network "deep".

In general, a neural network with multiple hidden layers is called a
Deep Neural Network (DNN). The term "deep" refers to having multiple
levels of learned transformations between input and output.

A network with:
    Input -> Hidden -> Output

has one hidden layer.

A network with:
    Input -> Hidden 1 -> Hidden 2 -> Hidden 3 -> Output

has three hidden layers and is clearly a multi-layer/deep architecture.

The exact number of layers required depends on the problem and model
architecture.
""")


# ============================================================
# Q6. What operations happen in Input Layer?
# ============================================================

print("""
Q6. What operations happen in Input Layer?

Answer:
The input layer mainly receives and represents the input features.

Typical activities associated with the input stage are:

1. Receiving input values.
2. Matching the input data to the expected number of features.
3. Passing those values to the next layer.

For example:

    Input features = [x1, x2, x3]

These values are passed to the neurons in the first hidden layer.

Data preprocessing such as normalization, standardization, or encoding
is commonly performed before or as part of the model's input pipeline,
rather than being considered a learning operation of the input neurons
themselves.
""")


# ============================================================
# Q7. What operations happen in Hidden Layer?
# ============================================================

print("""
Q7. What operations happen in Hidden Layer?

Answer:
A hidden-layer neuron generally performs the following operations:

Step 1: Receives inputs from the previous layer.

Step 2: Multiplies each input by its corresponding weight.

Step 3: Adds the weighted values and bias.

    z = w1*x1 + w2*x2 + ... + wn*xn + b

Step 4: Applies an activation function.

    a = activation(z)

Step 5: Sends the resulting activation to the next layer.

These operations are repeated through the hidden layers, allowing the
network to learn increasingly complex representations.
""")


# ============================================================
# Q8. What happens in Output Layer during prediction?
# ============================================================

print("""
Q8. What happens in Output Layer during prediction?

Answer:
During prediction, the output layer receives the values produced by the
last hidden layer and converts them into the final model output.

The exact operation depends on the task.

Binary classification:
    A single output can use Sigmoid to produce a value between 0 and 1.

Multiclass classification:
    Softmax can convert the output scores into probabilities for all
    classes.

Regression:
    The output is commonly a continuous numerical value.

The final output is then interpreted as the prediction of the neural
network.
""")


# ============================================================
# Q9. Draw ANN having 3 input neurons, 2 hidden neurons, and
#     1 output neuron.
# ============================================================

print("""
Q9. Draw ANN having 3 input neurons, 2 hidden neurons, and 1 output neuron.

Answer:

A simple fully connected representation is:

             INPUT LAYER       HIDDEN LAYER       OUTPUT

               x1  o ----------- o h1
                    \           /  \ 
                     \         /    \
               x2  o --\-------/------o h2 -----> o y
                       \       \     /
                        \       \   /
               x3  o ----\-------\-/

More clearly, all three input neurons are connected to both hidden
neurons, and both hidden neurons are connected to the output neuron.

Architecture:

    Input Layer       Hidden Layer       Output Layer

       (x1)  -------->   (h1)  --------         |                |                      |                |              > (y)
         |                |             /
       (x2)  -------->   (h2)  --------/
         |
       (x3)  -------->   (h1) and (h2)

Conceptual flow:

    3 Input Neurons
          |
          v
    2 Hidden Neurons
          |
          v
    1 Output Neuron

The actual network normally has a weight on every connection.
""")

# A text/ASCII diagram is used so that the .py file remains self-contained
# and can be opened easily in any editor.


# ============================================================
# Q10. Can a neural network work without hidden layer?
#      Explain with example.
# ============================================================

print("""
Q10. Can a neural network work without hidden layer?
     Explain with example.

Answer:
Yes. A neural network can work without a hidden layer.

Such a network can have:

    Input Layer -> Output Layer

This is essentially a single-layer neural network. For example, a
perceptron can perform simple binary classification when the classes are
linearly separable.

Example:
Suppose we want to classify points using a linear decision boundary:

    y = activation(w1*x1 + w2*x2 + b)

The model can separate data if a suitable straight-line boundary can
separate the classes.

However, a network without hidden layers cannot learn arbitrary complex
non-linear relationships. Hidden layers with non-linear activation
functions allow neural networks to learn much more complex patterns.

Therefore:
    Simple / linearly separable problem -> hidden layer may not be needed.
    Complex non-linear problem          -> hidden layers are generally
                                           needed.
""")


# ============================================================
# Assignment completed
# ============================================================

print("""
============================================================
ASSIGNMENT COMPLETED
============================================================

All 10 questions from Deep Learning Assignment 59 have been answered
in the same Question -> Answer sequence as the PDF.
""")
