"""
Deep Learning Assignment 73
Marvellous Infosystems

All 10 questions are answered in the exact sequence of the supplied PDF.
"""

# ============================================================
# QUESTION 1
# Why were Transformers introduced?
# What RNN/LSTM limitations are solved?
# ============================================================

print("""
QUESTION 1
==========

Transformers were introduced to process sequence data more efficiently
and to model relationships between tokens using attention rather than
depending on a recurrent step-by-step computation.

Important limitations of RNNs/LSTMs:

1. Sequential computation:
   RNN/LSTM processes tokens one time step after another. This makes
   training difficult to parallelize across sequence positions.

2. Long-range dependencies:
   Basic recurrent models can struggle to preserve information across
   very long sequences. LSTM improves this using gates, but long
   sequential computation is still required.

3. Training speed:
   Because recurrent steps depend on previous steps, the computation
   cannot be fully parallelized across the sequence during training.

4. Contextual relationships:
   Attention allows a token to directly consider information from other
   relevant tokens, including distant tokens.

Transformers therefore provide strong parallel processing during training
and an effective attention-based mechanism for capturing relationships
across a sequence.
""")


# ============================================================
# QUESTION 2
# Complete Transformer architecture.
# ============================================================

print(r"""
QUESTION 2
==========

A Transformer is based on an encoder-decoder architecture and attention.

High-level architecture:

Input Tokens
     |
Input Embeddings
     +
Positional Encoding
     |
     v
+-------------------+
|      ENCODER      |
| Multi-Head        |
| Self-Attention    |
| Add & Normalize   |
| Feed-Forward Net  |
| Add & Normalize   |
+-------------------+
     |
 Encoder representations
     |
     v
+-------------------+
|      DECODER      |
| Masked Multi-Head |
| Self-Attention    |
| Add & Normalize   |
| Cross-Attention   |
| Add & Normalize   |
| Feed-Forward Net  |
| Add & Normalize   |
+-------------------+
     |
Linear / Output layer
     |
Softmax
     |
Output probabilities


1. Input Embeddings
   Convert token IDs into dense numerical vectors.

2. Positional Encoding
   Adds information about the position/order of tokens because self-
   attention itself does not inherently know token order.

3. Encoder
   Processes the input sequence and creates contextual representations.
   Each encoder layer contains self-attention and a feed-forward network,
   with residual connections and normalization.

4. Decoder
   Generates the output sequence. It uses masked self-attention so that
   a position cannot use future target tokens, and cross-attention to
   use information produced by the encoder.

5. Attention Mechanism
   Determines which tokens should receive more focus when constructing
   contextual representations.

6. Feed-Forward Network
   Applies a learned nonlinear transformation independently to each
   sequence position after attention.

The encoder and decoder are composed of repeated layers in the original
Transformer architecture.
""")


# ============================================================
# QUESTION 3
# Explain Self-Attention and why it is the heart of Transformer.
# ============================================================

print("""
QUESTION 3
==========

Self-Attention allows every token in a sequence to examine other tokens
in the same sequence and determine how relevant they are.

For an input representation X:

    Q = XW_q
    K = XW_k
    V = XW_v

The attention calculation is:

    Attention(Q, K, V)
      = softmax(QK^T / sqrt(d_k)) V

Step-by-step:

1. Create Query, Key and Value representations.
2. Calculate similarity between each Query and every Key.
3. Scale the scores by sqrt(d_k).
4. Apply softmax to convert scores into attention weights.
5. Use those weights to calculate a weighted sum of Value vectors.

Why it is considered the heart of the Transformer:

- It creates context-aware token representations.
- It can connect distant tokens directly.
- It lets the model focus on the most relevant parts of the input.
- It avoids the need to pass information sequentially through every
  earlier time step as in an RNN.

Example:
In "The animal didn't cross the road because it was tired", attention
can help the model relate "it" to relevant earlier words based on learned
relationships.
""")


# ============================================================
# QUESTION 4
# Explain Q=XWq, K=XWk, V=XWv.
# ============================================================

print("""
QUESTION 4
==========

The Transformer creates three different representations from the same
input matrix X:

    Q = XW_q
    K = XW_k
    V = XW_v

1. Query (Q)
   Represents what information a token is looking for.

2. Key (K)
   Represents information that can be matched against a query. Similarity
   between a Query and Keys determines attention scores.

3. Value (V)
   Contains the information that is actually combined after attention
   weights have been calculated.

Why all three are required:

- Query asks: "What information do I need?"
- Key helps answer: "How relevant is this token to that query?"
- Value provides: "What information should be passed forward?"

The learned matrices W_q, W_k and W_v transform the original token
representations into task-specific query, key and value spaces.
""")


# ============================================================
# QUESTION 5
# Step-by-step attention score calculation.
# ============================================================

print("""
QUESTION 5
==========

Scaled dot-product attention is:

    Attention(Q,K,V)
    = softmax(QK^T / sqrt(d_k)) V

Step 1: Q x K^T
----------------
Calculate the dot product between each Query and each Key.

    Scores = QK^T

A larger dot product generally indicates that a Query and Key are more
strongly aligned.

Step 2: Scale by sqrt(d_k)
--------------------------
Divide the scores by:

    sqrt(d_k)

where d_k is the dimension of each Key vector.

This scaling prevents very large dot-product values when the vector
dimension is large, helping keep softmax gradients more stable.

    Scaled Scores = QK^T / sqrt(d_k)

Step 3: Softmax
---------------
Apply softmax to each row:

    Attention Weights =
        softmax(QK^T / sqrt(d_k))

Softmax converts the scores into non-negative weights whose values in a
row sum to 1.

Step 4: Weighted Sum with V
---------------------------
Multiply the attention weights by the Value matrix:

    Output = Attention Weights V

The output is therefore a weighted combination of Value vectors, where
more relevant tokens contribute more strongly.
""")


# ============================================================
# QUESTION 6
# Why Transformers support parallel processing better than RNN?
# ============================================================

print("""
QUESTION 6
==========

Transformers support parallel processing better than RNNs because
self-attention can process the representations of many sequence
positions simultaneously during training.

RNN:
    x1 -> RNN -> h1
             |
             v
    x2 -> RNN -> h2
             |
             v
    x3 -> RNN -> h3

Each step depends on the previous hidden state, so the sequence creates a
dependency chain.

Transformer:
    x1 ----+
    x2 ----+----> Self-Attention ----> outputs
    x3 ----+
    x4 ----+

The attention calculations for multiple positions can be performed in
parallel using matrix operations.

Advantages:
- Better hardware utilization during training.
- Faster training for long sequences compared with strictly sequential
  recurrent computation.
- Direct attention connections between tokens can help model long-range
  relationships.

Important qualification:
Autoregressive Transformer decoders still generate output tokens
sequentially during generation/inference, because the next token depends
on previously generated tokens. The major parallelism advantage is most
apparent in training and in processing the input sequence.
""")


# ============================================================
# QUESTION 7
# Explain Positional Encoding and why required.
# ============================================================

print("""
QUESTION 7
==========

Positional Encoding adds information about token position to the token
embeddings.

Why it is required:

Self-attention considers relationships between tokens, but by itself it
does not inherently encode the original sequential order. Without
positional information, sequences containing the same tokens in different
orders could be difficult to distinguish based only on token content.

The original Transformer uses sinusoidal positional encoding:

    PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
    PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

Where:
- pos = token position
- i = dimension index
- d_model = embedding dimension

The positional encoding is combined with the token embedding, commonly
by addition:

    Transformer Input = Token Embedding + Positional Encoding

This gives the Transformer information about where each token occurs in
the sequence.
""")


# ============================================================
# QUESTION 8
# What is Multi-Head Attention? Why multiple heads?
# ============================================================

print("""
QUESTION 8
==========

Multi-Head Attention runs several attention mechanisms, called heads,
in parallel.

Each head has its own learned projections for Query, Key and Value. Each
head can therefore learn to focus on different types of relationships.

For each head:

    head_i = Attention(Q_i, K_i, V_i)

The heads are concatenated and transformed:

    MultiHead(Q,K,V)
      = Concat(head_1, ..., head_h) W_o

Why use multiple heads?

1. Different relationships:
   Different heads can focus on different relationships between tokens.

2. Different representation subspaces:
   Each head works with learned projections, allowing different aspects
   of the representation to be examined.

3. Richer context:
   Combining multiple heads provides a richer representation than relying
   on a single attention calculation.

Example:
In a sentence, one head may learn relationships similar to grammatical
dependencies while another may focus on a different contextual relation.
The exact roles of heads are learned by the model rather than manually
assigned.
""")


# ============================================================
# QUESTION 9
# Explain Add & Normalize layer and problem it solves.
# ============================================================

print("""
QUESTION 9
==========

Add & Normalize consists of two main ideas:

1. Add (Residual Connection)
   The original input to a sub-layer is added to the sub-layer output:

       Output = Input + Sublayer(Input)

   This is called a residual or skip connection.

2. Normalize
   The result is normalized using Layer Normalization:

       LayerNorm(Input + Sublayer(Input))

In a Transformer, this structure is used around components such as
attention and feed-forward sub-layers.

Why it is useful:

- Residual connections make it easier for information and gradients to
  flow through deep networks.
- They help reduce the difficulty of training many stacked layers.
- Layer normalization helps stabilize the activations during training.
- Together, they improve optimization and training stability.

Conceptually:

Input
  |
  +----------------------+
  |                      |
  v                      |
Attention/FFN ----------> Add
                           |
                           v
                      LayerNorm
                           |
                         Output
""")


# ============================================================
# QUESTION 10
# Explain Encoder and Decoder in Transformers.
# ============================================================

print("""
QUESTION 10
===========

ENCODER
=======

The encoder processes the input sequence and creates contextual
representations.

A typical encoder layer contains:

1. Multi-Head Self-Attention
   Each input position can attend to other input positions.

2. Add & Normalize
   Residual connection followed by normalization.

3. Feed-Forward Network
   Applies a learned nonlinear transformation to each position.

4. Add & Normalize
   Another residual connection and normalization.

Repeated encoder layers progressively build richer contextual
representations of the input.

DECODER
=======

The decoder generates the output sequence.

A typical decoder layer contains:

1. Masked Multi-Head Self-Attention
   Prevents a target position from attending to future target tokens.

2. Add & Normalize
   Residual connection and normalization.

3. Cross-Attention
   Decoder representations attend to the encoder output so the decoder
   can use information from the input sequence.

4. Add & Normalize
   Residual connection and normalization.

5. Feed-Forward Network
   Applies a nonlinear transformation.

6. Add & Normalize
   Another residual connection and normalization.

Finally, a linear projection and softmax can convert the decoder output
into probabilities over the target vocabulary.

Overall:

Input
  |
Embedding + Position
  |
Encoder Stack
  |
Encoder Output
  |
Decoder <--- previous/generated target tokens
  |
Linear + Softmax
  |
Output Tokens

The encoder primarily builds representations of the input, while the
decoder uses those representations to generate the output sequence.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
============================================================
ASSIGNMENT 73 COMPLETED
============================================================

All 10 questions have been answered in the exact sequence of the PDF.

Topics covered:
- Why Transformers were introduced
- Complete Transformer architecture
- Self-Attention
- Query, Key and Value
- Attention score calculation
- Transformer parallel processing
- Positional Encoding
- Multi-Head Attention
- Add & Normalize
- Encoder and Decoder
============================================================
""")
