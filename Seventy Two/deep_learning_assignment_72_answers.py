"""
Deep Learning Assignment 72 - Marvellous Infosystems
All questions answered in the exact sequence/numbering of the supplied PDF.
Note: The PDF jumps from Q6 to Q8; Q7 is not present, so it is not invented.
"""

print(r"""
Q1. BASIC RNN ARCHITECTURE
==========================
An RNN processes a sequence one time step at a time. At time t it receives
the current input x_t and the previous hidden state h_(t-1).

Diagram:

 x(t-1)       x(t)       x(t+1)
   |            |           |
   v            v           v
+------+     +------+    +------+
| RNN  | --> | RNN  | -> | RNN  |
+------+     +------+    +------+
 h(t-1)       h(t)        h(t+1)
   |            |           |
 y(t-1)       y(t)        y(t+1)

Input layer: receives x_t at each time step.
Hidden state: stores a representation of previous information.
Recurrent connection: passes h_(t-1) to the next time step.
Output layer: produces y_t when an output is required.
Flow across time: information moves from earlier to later time steps.

Typical equations:
h_t = tanh(W_xh*x_t + W_hh*h_(t-1) + b_h)
y_t = f(W_hy*h_t + b_y)
""")

print("""
Q2. WHY RNN FOR SEQUENTIAL DATA?
================================
A feed-forward network normally treats inputs independently and has no
natural recurrent memory. RNNs maintain a hidden state, so information
from earlier elements can influence later predictions.

Sentence processing:
Words arrive in order. The hidden state carries context from previous
words, helping the network use word order and surrounding context.

Time-series prediction:
Previous observations can influence future values. An RNN processes
historical observations sequentially and uses its hidden state to help
predict later values.
""")

print("""
Q3. HOW THE HIDDEN STATE WORKS
==============================
At every time step the RNN combines the current input x_t with the
previous hidden state h_(t-1):

h_t = tanh(W_xh*x_t + W_hh*h_(t-1) + b_h)

The resulting h_t becomes the hidden state passed to the next time step.
Therefore previous information is transferred through the recurrent
hidden-to-hidden connection.
""")

print("""
Q4. MEMORY IN RNN
=================
RNN memory means information about previously processed inputs is encoded
in the hidden state. The network does not keep a separate copy of every
past input; instead, each new hidden state is computed from the current
input and previous hidden state:

h_t = f(x_t, h_(t-1))

Thus h_t contains information influenced by the sequence seen so far.
Basic RNNs, however, can struggle to retain very long-term information.
""")

print("""
Q5. VANISHING GRADIENT PROBLEM
==============================
During Backpropagation Through Time, gradients are propagated across many
time steps. They repeatedly involve derivatives and recurrent weights.
If the factors are mostly smaller than 1, repeated multiplication makes
the gradient extremely small.

Consequences:
- Very small parameter updates at early time steps.
- Difficulty learning long-term dependencies.
- Important information from distant earlier inputs can be lost.
- Training may become slow or ineffective.

LSTM was introduced with a gated memory mechanism to make long-term
information flow easier.
""")

print("""
Q6. FEED-FORWARD NN vs CNN vs RNN
=================================
Feed-Forward Neural Network:
- Architecture: layered forward connections, no recurrent loop.
- Data: commonly fixed-size/tabular inputs.
- Uses: classification, regression and general prediction.

CNN:
- Architecture: convolution filters/kernels, usually pooling and dense
  layers.
- Data: exploits local/spatial structure, especially images.
- Uses: image classification, object detection, computer vision.

RNN:
- Architecture: recurrent connections plus hidden state.
- Data: ordered/sequential or time-dependent data.
- Uses: text, speech, time-series and sequence modelling.

Q7 is not present in the supplied PDF, which jumps directly from Q6 to Q8.
""")

print("""
Q8. REAL-WORLD RNN APPLICATIONS
===============================
1. NLP:
   Tokens are processed sequentially and hidden state carries contextual
   information for sequence classification or language modelling.

2. Speech recognition:
   Audio is represented as time-ordered feature frames; recurrent states
   capture information from previous frames.

3. Time-series forecasting:
   Historical sensor, temperature, demand or other observations are fed
   sequentially to predict future values.

4. Sentiment analysis:
   Words/tokens are processed as a sequence and a hidden representation
   can be used to classify sentiment.

5. Machine translation:
   RNN encoder-decoder architectures can encode a source sequence and
   generate target tokens sequentially. Modern systems often use
   Transformers, but RNNs are historically important here.

Other examples include handwriting recognition and sequence labelling.
""")

print("""
Q9. WHY LSTM WAS INTRODUCED
===========================
Basic RNNs can struggle with long-term dependencies because of vanishing
gradients during Backpropagation Through Time.

LSTM addresses this using:
- Cell state for long-term information flow.
- Forget gate to remove irrelevant information.
- Input gate to control new information entering memory.
- Output gate to control information exposed as hidden state.

This makes LSTM better suited than a basic RNN to many long-sequence
learning problems.
""")

print("""
Q10. COMPLETE LSTM ARCHITECTURE
================================
An LSTM receives x_t, h_(t-1), and C_(t-1).

Cell state C_t:
  Long-term memory pathway.

Hidden state h_t:
  Current output/state passed to the next time step.

Forget gate:
  Determines what old cell-state information to retain.

Input gate:
  Determines what new information should be written.

Output gate:
  Determines what part of the updated memory becomes the hidden state.

Conceptual flow:

x_t + h_(t-1)
      |
      +--> Forget Gate ----> old memory filtering
      |
      +--> Input Gate + Candidate --> new memory
      |
      +--> Output Gate -------------> h_t

The updated cell state is C_t, and h_t is generated from C_t through
the output gate.
""")

print("""
Q11. ROLE OF FORGET GATE
========================
The forget gate controls how much of the previous cell state is retained.

f_t = sigmoid(W_f [h_(t-1), x_t] + b_f)

Sigmoid gives values from 0 to 1:
- near 0 -> mostly forget
- near 1 -> mostly retain

The old memory contribution is:
f_t * C_(t-1)

Forgetting is important because old information is not always relevant.
Removing irrelevant information prevents memory from becoming overloaded
and lets the network focus on useful context.
""")

print("""
Q12. MATHEMATICAL LSTM MEMORY UPDATE
====================================
Forget gate:
f_t = sigmoid(W_f [h_(t-1), x_t] + b_f)

Input gate:
i_t = sigmoid(W_i [h_(t-1), x_t] + b_i)

Candidate memory:
C~_t = tanh(W_C [h_(t-1), x_t] + b_C)

Cell-state update:
C_t = f_t*C_(t-1) + i_t*C~_t

Output gate:
o_t = sigmoid(W_o [h_(t-1), x_t] + b_o)

Hidden state:
h_t = o_t*tanh(C_t)

Sigmoid produces values between 0 and 1 and is used for gates.
Tanh produces values between -1 and 1 and is used for candidate/state
transformations. The cell-state equation retains selected old memory and
adds selected new information.
""")

print("""
Q13. RNN vs LSTM
================
Architecture:
- RNN: recurrent hidden state with a comparatively simple update.
- LSTM: hidden state plus cell state and forget/input/output gates.

Complexity:
- RNN: simpler and generally fewer operations/parameters.
- LSTM: more complex because of multiple gates and states.

Performance:
- RNN can work well for shorter dependencies.
- LSTM is generally better for learning long-term dependencies.

Memory handling:
- RNN mainly carries information through its hidden state.
- LSTM uses a dedicated cell state with gates to control information flow.
""")

print("""
Q14. PRACTICAL LSTM PROJECT - STOCK PREDICTION
===============================================
Workflow:

1. Collect historical stock data such as Open, High, Low, Close and
   Volume.
2. Sort records by date and clean missing/invalid values.
3. Select the target, such as Close price.
4. Scale numerical values, commonly with MinMaxScaler.
5. Create sliding sequences, e.g. previous 60 days -> next-day target.
6. Split chronologically into training and testing data to reduce
   future-data leakage.
7. Build an LSTM model, for example:
       Input sequence -> LSTM -> optional Dropout -> Dense -> prediction
8. Train using a loss such as MSE and an optimizer such as Adam.
9. Evaluate with MAE, MSE or RMSE on unseen data.
10. Use the latest sequence for prediction.
11. Deploy/monitor and retrain when appropriate.

Stock prediction is uncertain; an LSTM prediction is not a guarantee of
future market performance.
""")

print("""
Q15. WHY LSTM IS BETTER FOR LONG-TERM DEPENDENCIES
==================================================
LSTM has a cell state that provides a controlled pathway for information
across many time steps. Its gates regulate that pathway:

Forget gate -> removes irrelevant old information.
Input gate  -> controls new information stored in memory.
Output gate -> controls information exposed as hidden state.

This architecture helps preserve useful information and makes gradient
flow across long sequences easier than in a basic RNN.

Therefore:
Basic RNN -> simple recurrent memory, more vulnerable to vanishing
             gradients and long-term dependency problems.
LSTM      -> gated memory mechanism, better suited to long-term
             dependencies.
""")

print("""
============================================================
ASSIGNMENT 72 COMPLETED
============================================================
Answered: Q1-Q6, Q8-Q15.
The supplied PDF contains no Question 7, so it was not invented.
""")
