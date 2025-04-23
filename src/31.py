import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Generate some random data
data = {
    'age': [18, 20, 25, 30],
    'gender': ['male', 'female', 'male', 'female']
}

df = pd.DataFrame(data)

# Split the data into features and target variable
X = df[['age']]
y = df['gender']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
