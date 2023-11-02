# coding:utf-8

import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# load feature selection dataset
data = pd.read_csv("feature_selection.csv").iloc[:, 1:]
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
data.drop("label", axis=1), data["label"], test_size=0.2, random_state=True, shuffle=True, stratify=data["label"]
)

# get feature importance scores
importance = best_model.feature_importances_

# combine the feature with importance score
importance = pd.DataFrame({'feature': X_train.columns, 'importance': importance})

# Sort features in descending order of importance scores 
importance = importance.sort_values(by='importance', ascending=False)
importance.to_csv("feature_importance.csv", index=False)