import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load the Excel data
try:
    df = pd.read_excel('/content/sample_data/student_scores.xlsx')
except FileNotFoundError:
    print("Error: 'student_scores.xlsx' not found. Please run the generation script first.")
    exit()

# 2. Separate features (X) and target variable (y)
# We use the 6 exam scores as inputs to predict the 'Future_Exam' score
features = ['Exam_1', 'Exam_2', 'Exam_3', 'Exam_4', 'Exam_5', 'Exam_6']
X = df[features]
y = df['Future_Exam']

# 3. Split the data into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate the model on the test data
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Model Evaluation Metrics ---")
print(f"Mean Absolute Error (MAE): {mae:.2f} marks")
print(f"R-squared Score (Accuracy Variance): {r2 * 100:.2f}%\n")

# 6. Predict the score for a specific individual student
# Let's say a student scored: 75, 80, 85, 78, 88, 90 in their past 6 exams
new_student_scores = np.array([[30, 20, 45, 38, 48, 60]])

# Reshape input to match expected feature naming convention
new_student_df = pd.DataFrame(new_student_scores, columns=features)
predicted_mark = model.predict(new_student_df)[0]

# Already got 95 predicted_mark is what system predicted
mae = mean_absolute_error([95], [predicted_mark])


print("--- Real-time Prediction ---")
print(f"Mean Absolute Error (MAE): {mae:.2f} marks")
print(f"R-squared Score (Accuracy Variance): {r2 * 100:.2f}%\n")


print(f"Input scores: {list(new_student_scores[0])}")
print(f"Predicted Future Exam Score: {predicted_mark:.1f}")
