

# import pandas
import pandas as pd

df = pd.read_csv('/DATASET 2 (2).csv', error_bad_lines=False)

df.head()

print(df.shape)

num_of_classes = len(df.SCORE.unique())
print(num_of_classes)

df.describe()

X = df.drop(axis=0, columns=['SCORE'])
Y = df.SCORE

print(X.shape)
print(Y.shape)

from sklearn.model_selection import train_test_split

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

#coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
#print(coeff_df)

y_pred = model.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df.head(50))

