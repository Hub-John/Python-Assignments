"""
Machine Learning Assignment 47
Marvellous Infosystems : Python - Automation & Machine Learning

All questions are answered in the same Question -> Answer sequence
as given in the assignment PDF.
"""

# ============================================================
# Q1. Explain in your own words what a coefficient represents
#     in regression. Give one simple real-life example.
# ============================================================

"""
Answer:
A coefficient in regression tells us how much the predicted output
changes when an input feature increases by one unit, while other
features are kept constant.

For example:
    Salary = 5000 * Experience + 20000

Here, 5000 is the coefficient of Experience. It means that, according
to this model, one additional year of experience increases the
predicted salary by 5000 units.

Therefore, a coefficient describes the direction and size of the
relationship between an input variable and the predicted output.
"""


# ============================================================
# Q2. Consider the regression model:
#     Y = 8X + 15
#
#     Identify coefficient and intercept.
#     Explain what the coefficient tells us.
# ============================================================

"""
Answer:
Regression equation:
    Y = 8X + 15

Coefficient = 8
Intercept = 15

The coefficient 8 means that when X increases by 1 unit, the
predicted value of Y increases by 8 units.

The positive coefficient shows a positive relationship between X
and Y.

When X = 0:
    Y = 8(0) + 15
      = 15

Therefore, the intercept is 15.
"""


# ============================================================
# Q3. Regression model:
#     Marks = 6 * StudyHours + 40
#
#     Explain coefficient 6, intercept 40, and the effect of
#     increasing study hours by 2 hours.
# ============================================================

"""
Answer:
Model:
    Marks = 6 * StudyHours + 40

Coefficient = 6
    For every additional 1 hour of study, predicted marks increase
    by 6 marks.

Intercept = 40
    When StudyHours = 0, the predicted marks are 40.

If study hours increase by 2:
    Change in predicted marks = 6 * 2
                              = 12 marks

Therefore, increasing study time by 2 hours increases the predicted
marks by 12 marks.
"""


# ============================================================
# Q4. Regression model:
#     Salary = 12 * Experience + 25
#
#     Calculate predicted salary for Experience = 2, 5, 7.
# ============================================================

def predict_salary(experience):
    return 12 * experience + 25


print("Q4. Predicted Salary")
for experience in [2, 5, 7]:
    salary = predict_salary(experience)
    print(f"Experience = {experience}")
    print(f"Salary = 12 * {experience} + 25 = {salary}")
    print()


# ============================================================
# Q5. Regression equation:
#     Y = -3X + 20
#
#     Explain negative coefficient, change in Y for X + 1,
#     and calculate Y when X = 4.
# ============================================================

"""
Answer:
Regression equation:
    Y = -3X + 20

1. Meaning of the negative coefficient:
   The coefficient is -3. It indicates a negative relationship
   between X and Y. As X increases, Y decreases.

2. What happens to Y when X increases by 1?
   Y decreases by 3 units.

3. Calculate Y when X = 4:

   Y = -3(4) + 20
     = -12 + 20
     = 8

Therefore:
    Y = 8 when X = 4.
"""


# ============================================================
# Q6. House-price regression model:
#
#     Price = 3000 * Size + 40000 * Bedrooms + 150000
#
#     Explain coefficients and identify the feature with larger
#     impact according to the equation.
# ============================================================

"""
Answer:
Model:
    Price = 3000 * Size + 40000 * Bedrooms + 150000

Coefficient of Size = 3000
    For every 1-unit increase in Size, predicted price increases
    by 3000 units, assuming Bedrooms remains constant.

Coefficient of Bedrooms = 40000
    For every additional bedroom, predicted price increases by
    40000 units, assuming Size remains constant.

According to the numerical coefficient values, Bedrooms has the
larger impact because:

    40000 > 3000

Important:
This direct comparison assumes the features are measured in the
units shown in the equation. In real datasets, feature scales and
units should also be considered before comparing coefficient
magnitudes.
"""


# ============================================================
# Q7. Train LinearRegression using:
#
# Study Hours : Marks
# 1           : 50
# 2           : 55
# 3           : 60
# 4           : 65
# 5           : 70
#
# Print coefficient and intercept.
# ============================================================

from sklearn.linear_model import LinearRegression

study_hours = [[1], [2], [3], [4], [5]]
marks = [50, 55, 60, 65, 70]

model = LinearRegression()
model.fit(study_hours, marks)

print("\nQ7. Linear Regression Model")
print("Coefficient =", model.coef_[0])
print("Intercept =", model.intercept__)


# ============================================================
# Q8. Using the regression model from Q7, predict marks for
#     6 study hours and display the predicted value.
# ============================================================

predicted_marks = model.predict([[6]])[0]

print("\nQ8. Prediction for 6 Study Hours")
print("Predicted Marks =", predicted_marks)


# ============================================================
# Q9. Dataset with two features:
#
# StudyHours  SleepHours  Marks
# 1           7           50
# 2           6           55
# 3           7           60
# 4           6           65
# 5           8           70
#
# Train a regression model, print both coefficients and intercept.
# ============================================================

X_multi = [
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
]

y_multi = [50, 55, 60, 65, 70]

multi_model = LinearRegression()
multi_model.fit(X_multi, y_multi)

print("\nQ9. Multiple Linear Regression Model")
print("Coefficient for StudyHours =", multi_model.coef_[0])
print("Coefficient for SleepHours =", multi_model.coef_[1])
print("All coefficients =", multi_model.coef_)
print("Intercept =", multi_model.intercept__)


# ============================================================
# Q10. Explain why coefficients are important in regression
#      models and how they help understand feature impact.
# ============================================================

"""
Answer:
Coefficients are important because they explain how each input
feature contributes to the predicted output.

For a regression model such as:

    Y = b1*X1 + b2*X2 + c

b1 and b2 are coefficients.

A coefficient helps us understand:

1. Direction:
   Positive coefficient -> increasing the feature tends to increase
   the prediction.
   Negative coefficient -> increasing the feature tends to decrease
   the prediction.

2. Magnitude:
   The coefficient indicates how much the prediction changes for a
   one-unit increase in the feature, assuming other features remain
   constant.

3. Feature impact:
   Coefficients can help compare the contribution of features, but
   their raw magnitudes should be interpreted carefully when features
   have different units or scales.

4. Model interpretation:
   Coefficients make linear regression relatively easy to interpret
   because we can explain how input features are related to the
   predicted value.

Therefore, coefficients connect the input features to the model's
predictions and make the regression model easier to understand.
"""


# ============================================================
# End of Assignment 47
# ============================================================
