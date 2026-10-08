"""
Deep Learning Assignment 70
Marvellous Infosystems

All 8 questions are answered in the exact sequence of the supplied PDF.
"""

# ============================================================
# QUESTION 1
# Explain why RNN is widely used in Natural Language Processing.
# ============================================================

print("""
QUESTION 1
==========

RNN (Recurrent Neural Network) is widely used in Natural Language
Processing (NLP) because language is sequential data. The order of words
and the context of previous words can affect the meaning of a sentence.

Important reasons:

1. Sequential processing:
   RNN processes words/tokens one after another.

2. Hidden-state memory:
   The hidden state carries information from previous words to later
   time steps.

3. Word order:
   RNN can use the order in which words appear.

4. Variable-length sequences:
   RNN architectures can process sequences containing different numbers
   of tokens.

5. Context:
   Earlier words can influence the interpretation of later words.

Example:
    "The movie was not good."

When the RNN reaches "good", information carried in its hidden state can
include the earlier word "not", which is important for sentiment analysis.
""")


# ============================================================
# QUESTION 2
# Complete pipeline of sentiment analysis using RNN.
# ============================================================

print("""
QUESTION 2
==========

A typical sentiment-analysis pipeline using an RNN is:

1. Collect text data
   Obtain sentences/documents together with sentiment labels such as
   Positive and Negative.

2. Text preprocessing
   Clean the text as required, such as normalizing text and handling
   unnecessary characters.

3. Tokenization
   Split each sentence into tokens and map tokens to integer IDs.

4. Create vocabulary
   Build a word-to-index mapping from the training text.

5. Padding
   Make sequences equal in length so they can be processed as batches.

6. Embedding
   Convert integer token IDs into dense numerical vectors that the RNN
   can learn from.

7. RNN processing
   The RNN reads the embedded sequence step by step and maintains a
   hidden state containing contextual information.

8. Output layer
   For binary sentiment, a final sigmoid unit can produce a value between
   0 and 1.

9. Prediction
   A threshold such as 0.5 can convert the probability into a class:
       >= 0.5 -> Positive
       <  0.5 -> Negative

Pipeline:

Raw Text
   |
Preprocessing
   |
Tokenization
   |
Integer Sequences
   |
Padding
   |
Embedding
   |
RNN
   |
Output Layer
   |
Sentiment Prediction
""")


# ============================================================
# QUESTION 3
# Explain tokenization with suitable example.
# ============================================================

print("""
QUESTION 3
==========

Tokenization is the process of breaking text into smaller units called
tokens. In word-level tokenization, the tokens are usually individual
words.

Example sentence:
    "food was not good"

Word tokens:
    ["food", "was", "not", "good"]

A tokenizer can assign each unique word an integer ID.

For example, suppose the tokenizer creates:
    food -> 1
    was  -> 2
    not  -> 3
    good -> 4

Then:

    ["food", "was", "not", "good"]
        ->
    [1, 2, 3, 4]

These integer sequences can then be padded and passed to an embedding
layer before being processed by an RNN.
""")


# ============================================================
# QUESTION 4
# Explain padding and why equal sequence length is required.
# ============================================================

print("""
QUESTION 4
==========

Padding means adding special padding tokens, commonly represented by 0,
to shorter sequences so that all sequences in a batch have the same
length.

Example:

Sentence 1:
    "food was good"
    -> [1, 2, 4]

Sentence 2:
    "food was not good"
    -> [1, 2, 3, 4]

Maximum length = 4

After padding:

Sentence 1:
    [1, 2, 4, 0]

Sentence 2:
    [1, 2, 3, 4]

Why equal sequence length is required:

Neural networks normally process a batch as a rectangular tensor. Every
sequence in the same batch therefore needs the same number of time-step
positions.

Padding provides those missing positions.

Important:
Padding values do not represent actual words. During model processing,
padding can be ignored using masking where appropriate.
""")


# ============================================================
# QUESTION 5
# Explain vocabulary size and how tokenizer creates word index.
# ============================================================

print("""
QUESTION 5
==========

Vocabulary size is the number of unique tokens/words represented in the
model's vocabulary.

Example training text:

    "food was good"
    "food was not good"

Unique words:
    food
    was
    good
    not

Vocabulary size = 4 (excluding any special tokens).

A tokenizer creates a word index by assigning a unique integer ID to each
word.

Example:

    food -> 1
    was  -> 2
    good -> 3
    not  -> 4

Then:

    "food was not good"
        ->
    [1, 2, 4, 3]

In practical NLP systems, the vocabulary can also include special tokens
such as padding or unknown-word tokens. Therefore the final vocabulary
size may be larger than the number of ordinary words.
""")


# ============================================================
# QUESTION 6
# Explain embedding layer and why token IDs are not enough.
# ============================================================

print("""
QUESTION 6
==========

An embedding layer converts integer token IDs into dense numerical
vectors.

Example:

Token IDs:
    food -> 1
    was  -> 2
    not  -> 3
    good -> 4

Instead of giving the RNN only the integer 1, 2, 3 or 4, the embedding
layer may represent each token as a vector such as:

    food -> [0.21, -0.13, 0.47, ...]
    was  -> [0.05,  0.31, 0.12, ...]
    not  -> [-0.22, 0.17, 0.41, ...]
    good -> [0.36, -0.04, 0.29, ...]

Why token IDs are not enough:

1. Token IDs are categorical identifiers.
   ID 4 is not mathematically "twice" ID 2 in meaning.

2. Integer distance has no semantic meaning.
   For example, assigning IDs 1 and 2 does not mean those words are
   semantically closer than IDs 1 and 10.

3. Embeddings provide learnable dense representations.
   During training, the embedding vectors can learn useful relationships
   between words.

Therefore:
Token ID -> Embedding vector -> RNN
""")


# ============================================================
# QUESTION 7
# Differentiate one-hot encoding and embedding vectors.
# ============================================================

print("""
QUESTION 7
==========

One-Hot Encoding:
- Represents each word using a vector whose length equals the vocabulary
  size.
- Exactly one position contains 1 and all other positions contain 0.
- Vectors are sparse.
- Does not automatically encode semantic similarity.

Example with vocabulary:
    [food, was, not, good]

One-hot representation:
    food -> [1, 0, 0, 0]
    was  -> [0, 1, 0, 0]
    not  -> [0, 0, 1, 0]
    good -> [0, 0, 0, 1]


Embedding Vector:
- Represents each word using a dense vector with a chosen embedding
  dimension.
- Values are learned during training.
- Can capture useful semantic/syntactic relationships.
- Usually requires far fewer dimensions than vocabulary size.

Example:
    food -> [0.21, -0.13, 0.47]
    good -> [0.36, -0.04, 0.29]

Main difference:

One-hot:
    sparse + vocabulary-sized + no learned semantic representation

Embedding:
    dense + fixed embedding dimension + learnable representation
""")


# ============================================================
# QUESTION 8
# Explain how "food was not good" is processed by RNN.
# ============================================================

print("""
QUESTION 8
==========

Sentence:
    "food was not good"

Step 1: Tokenization

    ["food", "was", "not", "good"]

Step 2: Token IDs

For example, if the tokenizer creates:
    food -> 1
    was  -> 2
    not  -> 3
    good -> 4

Then:
    [1, 2, 3, 4]

Step 3: Embedding

Each ID is converted into a dense vector:

    1 -> embedding(food)
    2 -> embedding(was)
    3 -> embedding(not)
    4 -> embedding(good)

Step 4: RNN processes the sequence

Time step 1:
    food + h0 -> RNN -> h1

Time step 2:
    was + h1 -> RNN -> h2

Time step 3:
    not + h2 -> RNN -> h3

Time step 4:
    good + h3 -> RNN -> h4

The hidden state carries information from earlier words. Therefore, when
the RNN processes "good", the current hidden state can contain information
about "not" and the earlier context.

Step 5: Sentiment output

For binary sentiment classification, a final sigmoid output can produce
a probability:

    h4 -> Dense/Sigmoid -> sentiment probability

For example:
    probability >= 0.5 -> Positive
    probability <  0.5 -> Negative

The exact probability is learned by the trained model; it cannot be
determined from the sentence alone without model parameters.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
============================================================
ASSIGNMENT 70 COMPLETED
============================================================

All 8 questions have been answered in the exact sequence of the PDF.

Topics covered:
- RNN and NLP
- Sentiment-analysis pipeline
- Tokenization
- Padding
- Vocabulary and word index
- Embedding layer
- One-hot encoding vs embeddings
- Processing "food was not good" with an RNN
============================================================
""")
