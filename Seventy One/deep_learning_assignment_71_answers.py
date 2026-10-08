"""
Deep Learning Assignment 71
Marvellous Infosystems

All 5 questions are answered in the exact sequence of the supplied PDF.
"""

# ============================================================
# QUESTION 1
# Explain RNN and why it is suitable for sequential data.
# ============================================================

print("""
QUESTION 1
==========

Recurrent Neural Network (RNN)

An RNN is a type of neural network designed to process sequential data.
Unlike a basic feed-forward network, an RNN has recurrent connections that
allow information from previous time steps to influence the current step.

Basic idea:

    x_t + h_(t-1) -> RNN -> h_t -> output

Where:
- x_t = current input
- h_(t-1) = previous hidden state
- h_t = new hidden state

Why RNN is suitable for sequential data:

1. It processes data in sequence order.
2. Its hidden state carries information from previous time steps.
3. Previous context can influence the current prediction.
4. It is useful when the order of observations matters.

Examples:
- Natural language and sentences
- Speech signals
- Time-series data
- Sensor readings

Traditional feed-forward neural networks normally process each input
without an internal recurrent state. Therefore they do not naturally model
dependencies across time steps as an RNN does.
""")


# ============================================================
# QUESTION 2
# Differentiate ANN, FNN, CNN and RNN.
# ============================================================

print("""
QUESTION 2
==========

ANN (Artificial Neural Network):
- General term for neural networks made from interconnected artificial
  neurons.
- Can contain input, hidden and output layers.
- Used for classification, regression and many other tasks.

FNN (Feed-Forward Neural Network):
- Information flows from input toward output without recurrent loops.
- Does not maintain a recurrent hidden state.
- Commonly used for fixed-size/tabular classification and regression.

CNN (Convolutional Neural Network):
- Uses convolution filters/kernels to learn local patterns.
- Particularly suited to spatially structured data.
- Common applications: image classification, object detection and
  computer vision.

RNN (Recurrent Neural Network):
- Uses recurrent connections and a hidden state.
- Processes ordered/sequential data and carries information across time.
- Common applications: text, speech and time-series processing.

Summary:

+------+----------------------------+-----------------------------+
| Type | Main architecture          | Typical applications       |
+------+----------------------------+-----------------------------+
| ANN  | General interconnected     | Classification, regression |
|      | neural-network structure   | and prediction              |
| FNN  | Forward-only connections   | Tabular/fixed-size data     |
| CNN  | Convolution/filter layers  | Images and spatial data     |
| RNN  | Recurrent connections +    | Text, speech, time series  |
|      | hidden state               | and sequences               |
+------+----------------------------+-----------------------------+
""")


# ============================================================
# QUESTION 3
# Explain sequence data and examples where order matters.
# ============================================================

print("""
QUESTION 3
==========

Sequence data is data in which observations have an order or position and
the order can carry meaningful information.

In sequence data, changing the order of observations may change the
meaning or the result.

Examples:

1. Natural Language:
   "dog bites man" and "man bites dog" contain the same words but have
   different meanings because the word order is different.

2. Speech:
   Speech is a time-ordered stream of sound features. The order of sounds
   is important for recognizing words.

3. Time-Series:
   Temperature, stock measurements, sensor readings and demand values
   occur at particular times. Earlier observations can influence later
   observations.

4. Video:
   Frames occur in a particular order. Changing the order can change the
   action being represented.

5. User activity/event logs:
   The sequence of events can describe a user's behavior or workflow.

Therefore, sequence models such as RNNs are useful when previous
observations can provide context for later observations.
""")


# ============================================================
# QUESTION 4
# Describe basic RNN architecture.
# ============================================================

print(r"""
QUESTION 4
==========

A basic RNN consists of an input, hidden state with a recurrent
connection, and an output.

Unrolled architecture:

        x(t-1)              x(t)              x(t+1)
           |                  |                  |
           v                  v                  v
       +-------+          +-------+          +-------+
h(t-2)->|  RNN  | -> h(t-1)->|  RNN  | -> h(t) ->|  RNN  |
       +-------+          +-------+          +-------+
           |                  |                  |
         y(t-1)              y(t)             y(t+1)

1. Input Layer:
   Receives the input x_t at each time step. For NLP, this may be a
   representation of the current word/token.

2. Hidden State:
   h_t is the internal representation that carries information from
   previous time steps.

3. Recurrent Connection:
   The previous hidden state h_(t-1) is fed into the RNN together with
   the current input x_t. This creates the recurrent/memory mechanism.

4. Output Layer:
   Uses the hidden representation to produce an output. The output can be
   produced at every time step or from a selected/final hidden state,
   depending on the task.

5. Activation Function:
   A basic RNN commonly uses tanh for its hidden-state activation.
   Other output activations depend on the task, such as sigmoid for
   binary classification.

A common hidden-state equation is:

    h_t = tanh(W_x x_t + W_h h_(t-1) + b)

where W_x and W_h are learned weights and b is a learnable bias.
""")


# ============================================================
# QUESTION 5
# Explain why memory is important in RNN.
# ============================================================

print("""
QUESTION 5
==========

Memory is important in RNNs because the meaning of the current input can
depend on information from earlier inputs.

The RNN's hidden state acts as a form of memory:

    h_t = f(x_t, h_(t-1))

Therefore the current hidden state is influenced by both the current input
and previous sequence information.

Example in language:

    "The movie was not good."

When processing "good", information about "not" from an earlier time step
can influence the current representation. This helps the model understand
the context and classify the sentiment correctly.

Memory is also important for:
- Time-series forecasting
- Speech recognition
- Sequence classification
- Event prediction

Without a mechanism for carrying previous information, the model would
have difficulty using earlier observations to interpret later ones.

Basic RNNs can have difficulty retaining information across very long
sequences because of issues such as vanishing gradients. Architectures
such as LSTM and GRU were developed to handle long-term dependencies more
effectively.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
============================================================
ASSIGNMENT 71 COMPLETED
============================================================

All 5 questions have been answered in the exact sequence of the PDF.

Topics covered:
- RNN concept and sequential data
- ANN vs FNN vs CNN vs RNN
- Sequence data and examples
- Basic RNN architecture
- Hidden state and recurrent connection
- Importance of RNN memory
============================================================
""")
