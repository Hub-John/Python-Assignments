"""
Machine Learning Assignment 48
Marvellous Infosystems : Python - Automation & Machine Learning

All questions are answered in the same Question -> Answer sequence
as given in the assignment PDF.
"""

# Q1. Implement Simple Linear Regression manually without using any ML library.
# Dataset: X = [1,2,3,4,5], Y = [3,4,2,4,5]
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]
n = len(X)
mean_x = sum(X) / n
mean_y = sum(Y) / n
numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y))
denominator = sum((x - mean_x) ** 2 for x in X)
m = numerator / denominator
c = mean_y - m * mean_x
predicted_y_6 = m * 6 + c

print("Q1. Simple Linear Regression")
print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)
print("Slope (m) =", m)
print("Intercept (c) =", c)
print(f"Regression Equation: Y = {m:.1f}X + {c:.1f}")
print("Predicted Y for X = 6:", predicted_y_6)

# Q2. Using the same dataset, calculate model performance.
predicted_y = [m * x + c for x in X]
squared_errors = [(actual - predicted) ** 2 for actual, predicted in zip(Y, predicted_y)]
sum_squared_errors = sum(squared_errors)
mse = sum_squared_errors / n
ss_total = sum((actual - mean_y) ** 2 for actual in Y)
r2 = 1 - (sum_squared_errors / ss_total)

print("\nQ2. Model Performance")
print("Actual Y values    :", Y)
print("Predicted Y values :", [round(v, 2) for v in predicted_y])
print("\nIntermediate MSE calculations:")
for i, (actual, predicted, error) in enumerate(zip(Y, predicted_y, squared_errors), 1):
    print(f"Record {i}: ({actual} - {predicted:.2f})^2 = {error:.4f}")
print("Sum of squared errors =", round(sum_squared_errors, 4))
print("MSE =", round(mse, 4))
print("\nIntermediate R^2 calculations:")
print("Mean of Y =", mean_y)
print("SS_total =", round(ss_total, 4))
print("SS_residual =", round(sum_squared_errors, 4))
print("R^2 = 1 - (SS_residual / SS_total)")
print("R^2 =", round(r2, 4))

# Q3. Train linear regression, predict salary for 6 years, and plot regression line.
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

experience = [[1], [2], [3], [4], [5]]
salary = [20000, 25000, 30000, 35000, 40000]
salary_model = LinearRegression()
salary_model.fit(experience, salary)
predicted_salary = salary_model.predict([[6]])[0]

print("\nQ3. Salary Prediction")
print("Slope =", salary_model.coef_[0])
print("Intercept =", salary_model.intercept_)
print("Predicted Salary for 6 Years Experience: Rs.", int(predicted_salary))

salary_predictions = salary_model.predict(experience)
plt.scatter([row[0] for row in experience], salary, label="Data Points")
plt.plot([row[0] for row in experience], salary_predictions, label="Regression Line")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Experience vs Salary - Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

# Q4. Why is KNN called a lazy learner?
# Answer: KNN does not build an explicit model during training. It stores
# the training data and performs distance calculations mainly at prediction time.

# Q5. What happens if K is too small?
# Answer: The model becomes sensitive to noise and individual observations,
# causing high variance and possible overfitting. K=1 is an extreme example.

# Q6. What happens if K is too large?
# Answer: The model considers many distant points, loses local patterns,
# and may underfit. It has higher bias and an overly smooth decision boundary.

# Q7. Why does linear regression minimize squared error?
# Answer: Squaring prevents positive and negative errors from cancelling,
# penalizes large errors more strongly, and gives a smooth differentiable
# objective that can be efficiently optimized.
# SSE = sum((Actual - Predicted)^2), MSE = SSE / n

# Q8. What is the difference between MSE and R^2?
# Answer: MSE measures the average squared prediction error (lower is better)
# and is in squared target units. R^2 measures the proportion of target
# variance explained relative to a mean-only baseline (closer to 1 is better).
# MSE = sum((Y_actual - Y_predicted)^2) / n
# R^2 = 1 - (SS_res / SS_tot)

# Q9. Why R^2 cannot be greater than 1?
# Answer: For ordinary least-squares regression with an intercept,
# R^2 = 1 - SS_res/SS_tot. Since SS_res >= 0, R^2 <= 1.
# R^2 = 1 represents a perfect fit. On some unusual test-set evaluations,
# R^2 can be negative, but the standard OLS R^2 does not exceed 1.

# Q10. Can KNN be used for regression?
# Answer: Yes. KNN regression finds the K nearest observations and commonly
# predicts the mean of their continuous target values. For example, neighbors
# with salaries 30000, 35000, and 40000 give a prediction of 35000 for K=3.
