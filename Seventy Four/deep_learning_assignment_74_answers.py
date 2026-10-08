"""
Deep Learning Assignment 74
Marvellous Infosystems

All 5 questions are answered in the exact sequence of the supplied PDF.
"""

# ============================================================
# QUESTION 1
# Explain Encoder-Only architecture.
# Examples: BERT, Sentiment analysis.
# Why is it good for understanding tasks?
# ============================================================

print("""
QUESTION 1
==========

Encoder-Only Architecture
--------------------------

An Encoder-Only Transformer uses the encoder part of the Transformer
architecture without a decoder.

Basic flow:

    Input Text
        |
    Tokenization
        |
    Token Embeddings + Positional Information
        |
    Encoder Layers
        |
    Contextual Representations
        |
    Task-Specific Output

The encoder uses self-attention so that each token can consider other
tokens in the input and build a context-aware representation.

Example: BERT
- BERT is an encoder-based Transformer model.
- It creates contextual representations of input text.
- The representation of a word can depend on both the words before and
  after it in the input.

Example: Sentiment Analysis
- Input: "The movie was excellent."
- The encoder processes the complete sentence.
- A classification layer can use the resulting representation to predict
  Positive or Negative sentiment.

Why Encoder-Only is good for understanding tasks:
1. It can use context from the whole input sequence.
2. Self-attention captures relationships between tokens.
3. It produces rich contextual representations.
4. It is suitable for classification, question answering, text
   understanding and other tasks where the main goal is to understand
   existing input rather than generate a new sequence.
""")


# ============================================================
# QUESTION 2
# Explain Decoder-Only architecture.
# Examples: GPT, ChatGPT, Llama.
# Why is it suitable for text generation?
# ============================================================

print("""
QUESTION 2
==========

Decoder-Only Architecture
--------------------------

A Decoder-Only Transformer uses the decoder-style stack for autoregressive
sequence generation.

Basic flow:

    Input Tokens
        |
    Token Embeddings + Positional Information
        |
    Masked Self-Attention
        |
    Feed-Forward Network
        |
    Repeated Decoder Layers
        |
    Linear Output Layer
        |
    Softmax
        |
    Next-Token Probability

The important feature is masked self-attention. A token is prevented from
looking at future tokens during autoregressive generation.

Examples:
- GPT
- ChatGPT
- Llama

Why it is suitable for text generation:
1. It predicts the next token from the tokens already available.
2. Masking prevents the model from using future target tokens.
3. After predicting one token, that token can be added to the context
   and the model can predict the next token.
4. Repeating this process generates a complete sequence.

Example:

    "The cat is"
          |
      predict "sleeping"
          |
    "The cat is sleeping"
          |
      predict next token
          |
        ...

This next-token prediction approach makes decoder-only Transformers
naturally suited to autoregressive text generation.
""")


# ============================================================
# QUESTION 3
# Explain Encoder-Decoder architecture.
# Examples: Translation systems, T5.
# Why are both encoder and decoder required?
# ============================================================

print("""
QUESTION 3
==========

Encoder-Decoder Architecture
-----------------------------

An Encoder-Decoder Transformer contains both an encoder stack and a
decoder stack.

Basic flow:

    Source Input
         |
    Input Embedding
         |
       ENCODER
         |
    Contextual Representations
         |
         +----------------------+
                                |
                         Cross-Attention
                                |
    Target/Previous Output -> DECODER
                                |
                         Linear + Softmax
                                |
                          Generated Output

Encoder:
- Reads and represents the source sequence.
- Uses self-attention to understand relationships within the source.

Decoder:
- Generates the target sequence step by step.
- Uses masked self-attention for the already generated target context.
- Uses cross-attention to access the encoder's representations of the
  source sequence.

Examples:
- Machine translation systems
- T5

Why both are required:
1. The encoder understands and represents the source input.
2. The decoder generates the required target output.
3. Cross-attention allows the decoder to use information from the
   encoder while generating each target token.

Example of translation:

    English sentence
          |
       Encoder
          |
    Source representation
          |
       Decoder
          |
    Marathi/Hindi/etc. translation

Therefore, the encoder focuses on understanding the source while the
decoder focuses on generating the target sequence.
""")


# ============================================================
# QUESTION 4
# Differentiate Encoder-Only, Decoder-Only and Encoder-Decoder.
# Compare architecture, working and use cases.
# ============================================================

print("""
QUESTION 4
==========

Comparison of Transformer Architectures
========================================

+----------------+----------------------+----------------------+----------------------+
| Basis          | Encoder-Only         | Decoder-Only         | Encoder-Decoder      |
+----------------+----------------------+----------------------+----------------------+
| Architecture   | Encoder stack only   | Decoder-style stack  | Encoder + Decoder    |
|                | with self-attention  | with masked          | stacks               |
|                |                      | self-attention       |                      |
+----------------+----------------------+----------------------+----------------------+
| Working        | Reads input and      | Predicts next token  | Encoder represents   |
|                | builds contextual    | autoregressively     | source; decoder uses |
|                | representations.     | from previous tokens. | it to generate target|
+----------------+----------------------+----------------------+----------------------+
| Attention      | Self-attention       | Causal/masked        | Encoder self-attn,   |
|                |                      | self-attention       | decoder self-attn +  |
|                |                      |                      | cross-attention      |
+----------------+----------------------+----------------------+----------------------+
| Main purpose   | Understanding input  | Generating text      | Transforming one     |
|                |                      | sequences            | sequence into another|
+----------------+----------------------+----------------------+----------------------+
| Examples       | BERT                 | GPT, ChatGPT, Llama  | T5, translation      |
+----------------+----------------------+----------------------+----------------------+
| Use cases      | Classification,      | Text generation,     | Translation,         |
|                | sentiment analysis,  | completion, dialogue | summarization and    |
|                | understanding        | and code generation  | sequence-to-sequence |
+----------------+----------------------+----------------------+----------------------+

In simple terms:

Encoder-Only:
    Understand the input.

Decoder-Only:
    Generate the next token/output.

Encoder-Decoder:
    Understand a source input and generate a related target sequence.
""")


# ============================================================
# QUESTION 5
# Which Transformer architecture is used in ChatGPT and why?
# ============================================================

print("""
QUESTION 5
==========

ChatGPT uses a decoder-only Transformer architecture for its core
autoregressive language-modeling approach.

Why decoder-only is suitable:

1. Next-token prediction:
   The model predicts the next token based on the preceding context.

2. Causal/Masked Attention:
   During autoregressive generation, the model attends to available
   previous context rather than future tokens.

3. Natural text generation:
   Once a token is predicted, it becomes part of the context for the
   next prediction.

4. Long-context processing:
   Self-attention allows the model to consider relationships among tokens
   in its available context.

Simplified generation:

    Prompt
      |
      v
    Decoder-only Transformer
      |
    Next-token prediction
      |
    Add predicted token to context
      |
      v
    Repeat
      |
    Generated response

Therefore, a decoder-only Transformer is well suited to ChatGPT's
autoregressive text-generation behavior.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
============================================================
ASSIGNMENT 74 COMPLETED
============================================================

All 5 questions have been answered in the exact sequence of the PDF.

Topics covered:
- Encoder-Only architecture
- BERT and sentiment analysis
- Decoder-Only architecture
- GPT, ChatGPT and Llama
- Encoder-Decoder architecture
- Translation and T5
- Architecture comparison
- ChatGPT Transformer architecture
============================================================
""")
