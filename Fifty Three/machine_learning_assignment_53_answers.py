"""
Machine Learning Assignment 53
Topic: Bagging in Machine Learning
"""

print("""
Q1. What is Bagging in Machine Learning?

Answer:
Bagging means Bootstrap Aggregating. It is an ensemble technique that
trains multiple models on different bootstrap samples of the training
data and combines their predictions. It primarily helps reduce variance
and make predictions more stable.
""")

print("""
Q2. Explain the basic working principle of Bagging.

Answer:
1. Start with the training dataset.
2. Create multiple bootstrap samples by sampling with replacement.
3. Train one base model on each sample.
4. Train the models independently.
5. Combine predictions: majority voting for classification and averaging
   for regression.
6. Use the combined prediction as the final result.
""")

print("""
Q3. Why is sampling performed with replacement in Bagging?

Answer:
Sampling with replacement creates different bootstrap samples from the
same dataset. A selected record is returned before the next selection,
so different models receive different combinations of records. This
creates model diversity and helps reduce variance when predictions are
combined.
""")

print("""
Q4. Can the same training record appear multiple times in a bootstrap sample?

Answer:
Yes. Because sampling is performed with replacement, the same record can
appear multiple times in one bootstrap sample.

Example:
Original: A, B, C, D, E
Bootstrap sample: B, D, B, E, A

Here B appears twice and C does not appear.
""")

print("""
Q5. Are the individual models in Bagging trained sequentially or independently?

Answer:
They are generally trained independently. Each model uses its own
bootstrap sample and normally does not depend on the predictions or
errors of another model.
""")

print("""
Q6. Can Bagging models be trained in parallel? Why?

Answer:
Yes. Since Bagging models are trained independently, multiple models can
be trained at the same time on different CPU cores or processors. After
training is complete, their predictions are combined.
""")

print("""
Q7. How are predictions combined in Bagging for regression?

Answer:
For regression, the predictions from the individual models are
typically averaged.

Example:
Model predictions = 100, 110, 105, 115

Final prediction = (100 + 110 + 105 + 115) / 4 = 107.5
""")

print("""
Q8. Which problem does Bagging primarily try to reduce: bias or variance?

Answer:
Bagging primarily reduces variance. It combines predictions from
multiple models trained on different bootstrap samples, making the
overall model less sensitive to changes in the training data.

Bagging is especially useful with high-variance learners such as
Decision Trees.
""")

print("""
Q9. Why are Decision Trees commonly used as base estimators in Bagging?

Answer:
Decision Trees can have high variance and can change substantially when
the training data changes. Bagging combines many different trees, which
helps reduce this instability. Decision Trees can also model non-linear
relationships and generally do not require feature scaling.
""")

print("""
Q10. Can Logistic Regression be used as a base estimator inside a Bagging ensemble?

Answer:
Yes. Bagging can use Logistic Regression as its base estimator; it is
not restricted to Decision Trees.

Example in scikit-learn:

    from sklearn.ensemble import BaggingClassifier
    from sklearn.linear_model import LogisticRegression

    model = BaggingClassifier(
        estimator=LogisticRegression(),
        n_estimators=10,
        random_state=42
    )

Each Logistic Regression model is trained on a different bootstrap
sample and their predictions are combined. The benefit may be smaller
than with high-variance models because Logistic Regression is generally
more stable.
""")

print("""
============================================================
ASSIGNMENT 53 COMPLETED
============================================================
All 10 questions are answered in Question -> Answer sequence.
============================================================
""")
