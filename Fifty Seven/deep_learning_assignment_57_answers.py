"""
Deep Learning Assignment 57 - Question / Answer Sequence
Marvellous Infosystems : Python - Automation & Machine Learning

All questions from the assignment are answered one by one below.
"""

# Q1. What is Deep Learning? Why is it considered a subset of Machine Learning?
print("""
Q1. What is Deep Learning? Why is it considered a subset of Machine Learning?

Answer:
Deep Learning is a branch of Machine Learning that uses artificial neural
networks with multiple layers to learn patterns and representations from data.

It is considered a subset of Machine Learning because:
1. Machine Learning is the broader field of algorithms that learn from data.
2. Deep Learning is one approach within Machine Learning.
3. Deep Learning mainly uses multi-layer neural networks to automatically
   learn useful features from large amounts of data.

Examples of Deep Learning applications include image recognition, speech
recognition, natural language processing, and recommendation systems.
""")


# Q2. Differentiate Artificial Intelligence, Machine Learning, and Deep Learning with suitable examples.
print("""
Q2. Differentiate Artificial Intelligence, Machine Learning, and Deep Learning
with suitable examples.

Answer:

Artificial Intelligence (AI):
AI is the broad field of creating systems that can perform tasks that
normally require human-like intelligence, such as reasoning, planning,
decision-making, or perception.
Example: A rule-based expert system that recommends actions based on
predefined conditions.

Machine Learning (ML):
ML is a subset of AI in which systems learn patterns from data and use
those patterns to make predictions or decisions without being explicitly
programmed for every case.
Example: An email spam classifier trained using examples of spam and
non-spam emails.

Deep Learning (DL):
DL is a subset of ML that uses neural networks with multiple layers to
learn complex representations from data.
Example: A deep neural network that recognizes objects in photographs.

Relationship:
    Artificial Intelligence
            |
            +-- Machine Learning
                    |
                    +-- Deep Learning
""")


# Q3. Explain the difference between rule-based systems and learning-based systems.
print("""
Q3. Explain the difference between rule-based systems and learning-based systems.

Answer:

Rule-based systems:
- Work using explicitly written rules.
- The programmer specifies the conditions and corresponding actions.
- They do not automatically learn new rules from training data.
- They are useful when the decision logic is clearly known.

Example:
    IF temperature > 38 degrees Celsius
    THEN display "High temperature"

Learning-based systems:
- Learn patterns or relationships from data.
- Their parameters are adjusted during training.
- They can generalize from training examples to unseen data.
- Machine Learning and Deep Learning systems are examples.

Example:
A model trained on many labeled images can learn to classify images
without requiring a separate manually written rule for every possible image.

Main difference:
    Rule-based system -> human-written rules
    Learning-based system -> patterns learned from data
""")


# Q4. What is meant by training a model in Deep Learning?
print("""
Q4. What is meant by training a model in Deep Learning?

Answer:
Training a Deep Learning model means teaching a neural network to learn
a useful mapping from input data to the desired output.

During training:
1. Input data is given to the neural network.
2. The network performs forward propagation and produces a prediction.
3. The prediction is compared with the actual target using a loss function.
4. Backpropagation calculates gradients of the loss with respect to the
   model parameters.
5. An optimizer updates the weights and biases.
6. These steps are repeated over many training examples and iterations.

The goal of training is to adjust the model's parameters so that its
predictions become more accurate and the training loss decreases.
""")


# Q5. What is an Artificial Neural Network (ANN)? Explain with block diagram.
print(r"""
Q5. What is an Artificial Neural Network (ANN)? Explain with block diagram.

Answer:
An Artificial Neural Network (ANN) is a computational model inspired by
the way biological neurons are connected. It consists of interconnected
neurons arranged in layers.

A typical ANN contains:
1. Input layer - receives input features.
2. Hidden layer(s) - processes the inputs and learns patterns.
3. Output layer - produces the final prediction or output.

Block diagram:

    Input Layer          Hidden Layer(s)          Output Layer

    x1  ----\              o ----\
    x2  -----\            /       \
    x3 -------> [ Hidden Neurons ] ---> [ Output ] ---> y
    x4  -----/            \       /
    xn  ----/              o ----/

Data flows from the input layer through hidden layers to the output layer.
Each connection has a weight, and neurons can have a bias and activation
function.
""")


# Q6. Why is it called a Neural Network? Explain relation with human brain neurons.
print("""
Q6. Why is it called a Neural Network? Explain relation with human brain neurons.

Answer:
It is called a Neural Network because its basic computational units,
called artificial neurons, are inspired by biological neurons in the
human brain and are connected together in a network.

Relation with biological neurons:
- Biological neurons receive signals through dendrites, process them in
  the cell body, and transmit signals through the axon.
- Artificial neurons receive numerical inputs, combine them using weights
  and a bias, apply an activation function, and produce an output.
- Connections between artificial neurons are analogous, in a simplified
  mathematical sense, to connections between biological neurons.

Important note:
An ANN is only an abstract mathematical model inspired by biological
neurons. It does not reproduce the full complexity of the human brain.
""")


# Q7. Explain biological neuron and artificial neuron comparison.
print("""
Q7. Explain biological neuron and artificial neuron comparison.

Answer:

Biological Neuron:
- Dendrites receive signals from other neurons.
- The cell body (soma) processes incoming signals.
- The axon carries the resulting signal to other neurons.
- Synapses provide connections between neurons.
- Neural activity is based on complex electrochemical processes.

Artificial Neuron:
- Inputs receive numerical values.
- Weights represent the strength of each input connection.
- A summation operation combines weighted inputs and bias.
- An activation function produces the neuron's output.
- Connections between artificial neurons form a network.

Comparison:

    Biological Neuron       Artificial Neuron
    ------------------------------------------------
    Dendrites               Inputs
    Synapses                Weights
    Cell body               Summation + processing
    Neural firing           Activation/output
    Axon                    Output connection

The comparison is conceptual: artificial neurons are simplified
mathematical abstractions inspired by biological neurons.
""")


# Q8. What is a neuron in ANN? Explain its working.
print("""
Q8. What is a neuron in ANN? Explain its working.

Answer:
A neuron in an Artificial Neural Network is a basic computational unit
that receives inputs, combines them using weights and a bias, applies an
activation function, and produces an output.

Working steps:
1. The neuron receives inputs x1, x2, ..., xn.
2. Each input is multiplied by its corresponding weight.
3. The weighted values are added together.
4. A bias is added.
5. The resulting value is passed through an activation function.
6. The neuron produces an output that is passed to the next layer.

Formula:
    z = w1*x1 + w2*x2 + ... + wn*xn + b
    y = f(z)

Where:
    x = inputs
    w = weights
    b = bias
    f = activation function
    y = output
""")


# Q9. What are weights in neural networks? Why are they important?
print("""
Q9. What are weights in neural networks? Why are they important?

Answer:
Weights are numerical parameters associated with connections between
neurons. A weight determines how strongly an input contributes to the
neuron's weighted sum.

For a neuron:
    z = w1*x1 + w2*x2 + ... + wn*xn + b

Importance of weights:
1. They control the contribution of individual inputs.
2. They allow the network to learn relationships and patterns from data.
3. During training, weights are adjusted to reduce the loss.
4. Learned weights determine how the network transforms inputs into
   useful predictions.

Example:
If x1 = 5 and w1 = 0.8, its contribution to the weighted sum is
5 * 0.8 = 4.

Therefore, weights are among the main parameters that a neural network
learns during training.
""")


# Q10. What is bias in ANN? Why is bias required?
print("""
Q10. What is bias in ANN? Why is bias required?

Answer:
Bias is an additional learnable parameter added to the weighted sum of
a neuron before the activation function.

Formula:
    z = w1*x1 + w2*x2 + ... + wn*xn + b
    y = f(z)

Why bias is required:
1. It allows a neuron to shift its activation threshold.
2. It helps the network fit patterns that may not pass through the origin.
3. It provides additional flexibility when learning the relationship
   between inputs and outputs.
4. Bias is learned along with the weights during training.

Simple example:
If the weighted sum is 0.2 and the bias is -0.5, then:
    z = 0.2 - 0.5 = -0.3

Thus, the bias can change whether and how strongly the neuron activates.
""")


print("""
============================================================
ASSIGNMENT 57 COMPLETED
============================================================
All 10 questions are answered in Question -> Answer sequence.
============================================================
""")
