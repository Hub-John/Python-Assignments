"""
Deep Learning Assignment 69 - All 8 questions answered in PDF order.
"""

# Q1
print("""
Q1. Hidden State in RNN
=======================
The hidden state is an internal representation that carries information
from previous time steps to the current step.

At time t:
h_t = tanh(W_x x_t + W_h h_(t-1) + b)

Because h_t depends on h_(t-1), information from earlier inputs can be
carried forward. Thus, the hidden state acts as a form of sequence memory.
Example: x1 -> h1 -> x2 -> h2 -> x3 -> h3.
""")

# Q2
print("""
Q2. RNN Reading "food was not good"
====================================
An RNN reads the sentence one word at a time:

t1: food -> h1
t2: was + h1 -> h2
t3: not + h2 -> h3
t4: good + h3 -> h4

Each new hidden state receives the current word and information from the
previous hidden state. Therefore, when "good" is processed, information
about the earlier word "not" can influence the representation and the
sentiment prediction.
""")

# Q3
print("""
Q3. SimpleRNN Hidden-State Formula
==================================
The formula given in the assignment is:

h_t = tanh(W_x x_t + W_h h_(t-1) + b)

Terms:
h_t       = new hidden state at time t.
tanh      = nonlinear activation, producing values between -1 and +1.
W_x       = input-to-hidden weight matrix.
x_t       = current input vector.
W_h       = recurrent hidden-to-hidden weight matrix.
h_(t-1)   = previous hidden state containing previous information.
b         = learnable bias vector.

The weighted input, recurrent information and bias are added first, then
tanh is applied to produce the new hidden state.
""")

# Q4
print("""
Q4. Role of Input, Previous Hidden State, Weights and Bias
===========================================================
Input vector (x_t): represents the current item being processed.
Previous hidden state (h_(t-1)): carries context from earlier time steps.
Weights (W_x, W_h): control the contribution of current and previous
                    information and are learned during training.
Bias (b): a learnable offset that gives the transformation more flexibility.

Together they form:
h_t = tanh(W_x x_t + W_h h_(t-1) + b)
""")

# Q5
print("""
Q5. Why Sequence Order Matters
===============================
RNNs are designed for ordered data. Changing the order can change the
meaning and the hidden states.

Example:
"dog bites man" and "man bites dog" contain the same words but have
different meanings because the order is different.

In time series, earlier observations also occur before later observations.
Therefore the sequence order must be preserved for the RNN to learn the
correct temporal relationships.
""")

# Q6
print("""
Q6. Why tanh is Commonly Used in SimpleRNN
===========================================
1. tanh is nonlinear, allowing the network to learn nonlinear patterns.
2. Its output is bounded between -1 and +1.
3. It is zero-centered, so it can represent positive and negative values.
4. Its bounded hidden-state representation is suitable for recurrent
   processing.

Formula:
tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

SimpleRNNs can still suffer from vanishing gradients on long sequences.
""")

# Q7
print("""
Q7. Calculate tanh([-2, -1, 0, 1, 2])
=======================================
Approximate outputs:

tanh(-2) = -0.9640
tanh(-1) = -0.7616
tanh( 0) =  0.0000
tanh( 1) =  0.7616
tanh( 2) =  0.9640

Therefore:
[-0.9640, -0.7616, 0.0000, 0.7616, 0.9640]
""")

import math

values = [-2, -1, 0, 1, 2]
print("Python calculation:")
for value in values:
    print(f"tanh({value}) = {math.tanh(value):.4f}")

# Q8
print("""
Q8. Why Sigmoid is Used for Binary Sentiment Analysis
======================================================
Sigmoid converts a real-valued output into a number between 0 and 1:

sigmoid(z) = 1 / (1 + e^(-z))

For binary sentiment:
0 = Negative
1 = Positive

A sigmoid output can be interpreted as the model's estimated probability
of the positive class. For example, 0.90 indicates a high predicted
probability for Positive.

Using a threshold of 0.5:
probability >= 0.5 -> Positive
probability <  0.5 -> Negative

Therefore sigmoid is suitable for a single-output binary classification
layer and is commonly used with binary cross-entropy loss.
""")

print("""
============================================================
ASSIGNMENT 69 COMPLETED
============================================================
All 8 questions answered in the exact sequence of the PDF.
""")
