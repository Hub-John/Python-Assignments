"""
Marvellous Infosystems - Machine Learning Assignment 35

All 10 questions are answered in the same sequence as the PDF.
"""

# ============================================================
# QUESTION 1
# Define Machine Learning and compare it with rule-based programming.
# ============================================================

print("""
QUESTION 1
==========

Machine Learning (ML) is a method of building computer systems that learn
patterns from data and use those learned patterns to make predictions or
decisions.

Traditional rule-based programming:
- A programmer explicitly writes rules.
- The program follows those fixed rules for given inputs.

Machine Learning:
- The programmer provides data and an appropriate learning algorithm.
- The model learns patterns/relationships from examples.

Real-world example:
For email spam detection, a rule-based system might use manually written
rules such as "if the email contains certain words, mark it as spam."
A Machine Learning system can learn from many examples of spam and
non-spam emails and learn patterns that help classify new emails.
""")


# ============================================================
# QUESTION 2
# Independent and dependent variables in Ball classification.
# ============================================================

print("""
QUESTION 2
==========

Independent variables:
These are input variables/features used by the model to make a prediction.
They may describe properties of the ball, such as weight, size, diameter,
colour, or other measured characteristics used in the case study.

Dependent variable:
This is the target/output that the model tries to predict.

In the Ball classification case study:
- Independent variables (X) = measurable ball characteristics/features.
- Dependent variable (y) = ball class, such as Cricket or Tennis.

In simple form:

Ball Features (X) -> Machine Learning Model -> Ball Class (y)
                                           -> Cricket / Tennis
""")


# ============================================================
# QUESTION 3
# Features vs Labels and whether features are always numeric.
# ============================================================

print("""
QUESTION 3
==========

Features:
Features are the input variables/attributes used by a Machine Learning
model to learn patterns and make predictions.

Labels:
A label is the target/output value that the model is trying to predict
in supervised learning.

Example:
For ball classification:
- Features = ball properties such as weight, size, colour, etc.
- Label = Cricket or Tennis.

Are features always numeric?
No. Features can originally be numeric or categorical/text values.

Examples:
- Numeric feature: weight = 160 grams
- Categorical feature: colour = "Red"
- Categorical feature: material = "Leather"

Machine Learning algorithms often require categorical features to be
encoded into a suitable numeric representation before training.
""")


# ============================================================
# QUESTION 4
# Supervised Machine Learning and why labels are mandatory.
# ============================================================

print("""
QUESTION 4
==========

Supervised Machine Learning is a type of Machine Learning in which a model
learns from labelled training examples.

Each training example contains:
- Input features (X)
- Correct target/label (y)

Labels are mandatory because the model needs to know the expected answer
during training. The learning algorithm compares its predictions with the
known labels and adjusts its learned parameters to reduce prediction error.

Example:
Features describing a ball -> Label: Cricket or Tennis.

Without labels, the model cannot directly learn a supervised mapping from
the input features to the specified target.
""")


# ============================================================
# QUESTION 5
# Why cannot the same dataset be used for both training and testing?
# ============================================================

print("""
QUESTION 5
==========

A model should not normally be trained and tested on exactly the same
dataset because the model has already seen those examples during training.

If the same records are used for both:
1. The model may memorize the training examples.
2. Test performance can appear artificially high.
3. We cannot reliably measure how well the model generalizes to unseen data.

The main problem is called overfitting (or, more precisely, an unreliable
evaluation caused by testing on data used for fitting).

A separate test set provides unseen examples for a more realistic estimate
of model performance.
""")


# ============================================================
# QUESTION 6
# Purpose of train/test split and typical industry ratio.
# ============================================================

print("""
QUESTION 6
==========

Purpose of splitting:
A dataset is split so that one part can be used to train the model and
another unseen part can be used to evaluate how well the trained model
generalizes.

Training set:
- Used to learn model parameters/patterns.

Testing set:
- Used after training to estimate performance on unseen data.

Typical ratio:
An 80:20 train-test split is a common starting point:
- 80% training
- 20% testing

However, there is no single ratio that is mandatory for every project.
The appropriate split depends on dataset size, problem requirements and
validation strategy.
""")


# ============================================================
# QUESTION 7
# Explain X_train, X_test, y_train, y_test.
# ============================================================

print("""
QUESTION 7
==========

X_train:
Input features used for training the Machine Learning model.

X_test:
Input features kept aside for testing/evaluating the trained model.

y_train:
Correct target/label values corresponding to X_train. These are used
during model training.

y_test:
Correct target/label values corresponding to X_test. These are used to
compare against the model's predictions during evaluation.

Typical code:

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

Relationship:

X_train + y_train -> Training
X_test  + y_test  -> Testing/Evaluation
""")


# ============================================================
# QUESTION 8
# Explain test_size=0.2 and what happens with test_size=0.5.
# ============================================================

print("""
QUESTION 8
==========

test_size=0.2 means that 20% of the available dataset is placed in the
test set, while approximately 80% is used for training.

Example with 100 samples:
- Training = 80 samples
- Testing = 20 samples

If test_size=0.5:
- Approximately 50% of the data is used for training.
- Approximately 50% is used for testing.

Effect of changing from 0.2 to 0.5:
- The model gets less training data.
- The test set becomes larger.
- Training may become less effective, especially for a small dataset.
- The evaluation set becomes larger, which can provide a broader test
  sample, but the model has fewer examples from which to learn.
""")


# ============================================================
# QUESTION 9
# Explain random_state=42 and what happens without it.
# ============================================================

print("""
QUESTION 9
==========

random_state=42 is a fixed seed used by train_test_split() to make the
random train/test split reproducible.

When the same data and the same random_state are used:
- The same records are selected for training/testing.
- Results can be reproduced across runs.

The number 42 is not special. Any fixed integer can be used as a seed.

If random_state is not provided:
- The split is randomly generated using the current random state.
- Different runs can produce different train/test partitions.
- Model evaluation results such as accuracy may therefore change.

Example:

train_test_split(X, y, test_size=0.2, random_state=42)
""")


# ============================================================
# QUESTION 10
# Explain step-by-step what happens internally with
# model.fit(X_train, y_train).
# ============================================================

print("""
QUESTION 10
===========

When we execute:

model.fit(X_train, y_train)

the general training process is:

1. Input training data:
   X_train contains the input features and y_train contains the correct
   target labels.

2. The algorithm examines the training examples:
   It searches for useful relationships/patterns between X_train and y_train.

3. Model parameters are learned:
   The exact learning process depends on the algorithm. For example,
   a Decision Tree learns useful splitting rules, while a linear model
   learns coefficients.

4. Prediction and error/loss evaluation:
   During training, the algorithm evaluates how well its current learned
   representation/model explains the training targets.

5. Parameter/model updates:
   The algorithm adjusts its internal parameters or structure according
   to its learning procedure to improve performance on the training data.

6. Trained model is stored:
   After fitting, the model object contains the learned parameters or
   structure.

7. The model can then predict:
   model.predict(X_test)

Important:
fit() is the training operation. It does not mean that the model is
being tested on X_test. Testing/evaluation is performed separately using
unseen test data.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
============================================================
ASSIGNMENT 35 COMPLETED
============================================================

All 10 questions have been answered in the exact question-answer sequence.

Key flow:
Data -> Train/Test Split -> X_train/y_train -> model.fit()
                         -> X_test/y_test -> model.predict() -> Evaluation
============================================================
""")
