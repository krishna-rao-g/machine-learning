import pandas as pd
import numpy as np

# Set random seed for reproducible scores
np.random.seed(42)

# Generate synthetic dataset for 100 students
num_students = 100

data = {
    'Student_ID': [f'STU_{i:03d}' for i in range(1, num_students + 1)],
    'Exam_1': np.random.randint(50, 100, num_students),
    'Exam_2': np.random.randint(52, 100, num_students),
    'Exam_3': np.random.randint(55, 100, num_students),
    'Exam_4': np.random.randint(58, 100, num_students),
    'Exam_5': np.random.randint(60, 100, num_students),
    'Exam_6': np.random.randint(62, 100, num_students),
}

# Generate a final target exam score that correlates naturally with the past performance
df_sample = pd.DataFrame(data)
df_sample['Future_Exam'] = (df_sample[['Exam_1', 'Exam_2', 'Exam_3', 'Exam_4', 'Exam_5', 'Exam_6']].mean(axis=1) * 1.05).clip(50, 100).astype(int)

# Save to Excel
df_sample.to_excel('student_scores.xlsx', index=False)
print("Sample file 'student_scores.xlsx' generated successfully!")
