"""
Machine Learning Assignment 54
Marvellous Infosystems : Python - Automation & Machine Learning
Topic: Random Forest and Boosting
"""

print("""
Q1. Why is Random Forest considered an Ensemble Learning algorithm?

Answer:
Random Forest is an ensemble because it combines predictions from many
decision trees instead of relying on a single tree. The trees are built
using bootstrap samples and random feature selection, and their
predictions are combined to produce the final result.
""")

print("""
Q2. Is Random Forest an example of Bagging or Boosting?

Answer:
Random Forest is an example of Bagging (Bootstrap Aggregating), not
Boosting. Its trees are generally trained independently using bootstrap
samples. Random Forest also adds random feature selection at tree splits.
""")

print("""
Q3. What is the relationship between Bagging and Random Forest?

Answer:
Bagging is a general ensemble technique. Random Forest is a specific
method based on Bagging with Decision Trees plus random feature
selection.

Therefore:
    Random Forest = Bagging of Decision Trees + Random Feature Selection
""")

print("""
Q4. What is the major difference between Bagging with Decision Trees
and Random Forest?

Answer:
The major difference is feature selection. Bagging with Decision Trees
uses bootstrap samples and a tree can generally consider all features
when selecting a split. Random Forest also uses bootstrap samples, but
at each split it considers only a random subset of features. This makes
the trees more diverse and less correlated.
""")

print("""
Q5. Can Random Forest be used for both classification and regression?

Answer:
Yes. Random Forest supports both tasks.

Classification:
Multiple trees predict class labels and their predictions are combined.

Regression:
Multiple trees predict numerical values and their predictions are
typically averaged.

Common implementations are:
    RandomForestClassifier
    RandomForestRegressor
""")

print("""
Q6. How is the final prediction generated in:

- Random Forest Classification?
- Random Forest Regression?

Answer:
Random Forest Classification:
Each tree predicts a class. The final prediction is commonly the class
receiving the majority of votes.

Example:
    Tree 1 -> A
    Tree 2 -> B
    Tree 3 -> A
    Tree 4 -> A
    Tree 5 -> B

Final prediction -> A, because A receives 3 of 5 votes.

Random Forest Regression:
Each tree predicts a numerical value and the predictions are typically
averaged.

Example:
    100, 110, 105, 115, 120

Average = (100 + 110 + 105 + 115 + 120) / 5 = 110

Therefore:
    Classification -> Majority vote
    Regression    -> Average prediction
""")

print("""
Q7. What is Boosting in Machine Learning?

Answer:
Boosting is an ensemble learning technique that combines multiple weak
learners to build a stronger predictive model. The learners are
generally trained sequentially, with later learners focusing on errors
or remaining prediction problems from earlier learners.

Examples include AdaBoost, Gradient Boosting, XGBoost, LightGBM, and
CatBoost.
""")

print("""
Q8. Explain the basic working principle of Boosting.

Answer:
The basic process is:

1. Start with the training data.
2. Train an initial weak learner.
3. Examine its errors or remaining prediction loss.
4. Train another learner that focuses on those errors.
5. Repeat for multiple learners.
6. Combine the learners to produce the final model.

Flow:
    Training Data
         |
         v
    Weak Learner 1
         |
         v
    Remaining Errors
         |
         v
    Weak Learner 2
         |
         v
        ...
         |
         v
    Combined Strong Model

The exact error-correction mechanism depends on the boosting algorithm.
""")

print("""
Q9. Are models in Boosting generally trained independently or sequentially?

Answer:
Boosting models are generally trained sequentially. Each new learner
uses information from earlier learners, such as their mistakes or
remaining residual error.

This differs from Bagging, where base learners are generally trained
independently on different bootstrap samples.

    Bagging  -> generally independent learners
    Boosting -> generally sequential learners
""")

print(r"""
Q10. What does it mean when we say:
"Every new learner tries to correct the mistakes made by the previous
learners." Explain with an example.

Answer:
It means that after an initial learner makes predictions, the boosting
process gives additional attention to errors or remaining prediction
problems. The next learner is trained to improve the combined model in
those areas.

Example:
Suppose there are 10 training examples.

Step 1:
The first weak learner correctly classifies 7 examples and incorrectly
classifies 3.

    Correct = 7
    Incorrect = 3

Step 2:
The boosting process gives more importance to the difficult examples
(or represents their remaining error, depending on the algorithm).

Step 3:
The second learner focuses more on those difficult examples and may
correct some of the previous errors.

Step 4:
Additional learners continue reducing the remaining error.

Conceptually:

    Learner 1 -> makes mistakes
                  |
                  v
            focus on errors
                  |
                  v
    Learner 2 -> improves those areas
                  |
                  v
            focus on remaining error
                  |
                  v
    Learner 3 -> further improves the combined model

The statement does not mean every new learner must correct every
individual mistake. It means the sequential process is directed toward
reducing errors left by earlier learners.
""")

print("""
============================================================
ASSIGNMENT 54 COMPLETED
============================================================
All 10 questions are answered in Question -> Answer sequence.
============================================================
""")
