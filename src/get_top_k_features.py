# coding:utf-8

import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import json
from sys import argv
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
from sklearn.model_selection import StratifiedKFold
from tqdm import tqdm


# select top k features by wrapper
def wrapper_select(X_train, y_train, X_test, y_test, fold_index):

	print("cv=".format(fold_index))
	
	params = {
		"booster":'gbtree',
		"max_depth": 12, 
		"n_estimators":100, 
		"subsample":0.8, 
		"learning_rate":0.01,
		"importance_type":"gain",
		"objective":'binary:logistic'
	}
	model = xgb.XGBClassifier(verbosity=0, params=params, use_label_encoder=False)

	importance = pd.read_csv('feature_importance.csv')

	top_k_dict = {}
	
	for n in tqdm(range(1, 501)):
		top_n_features = importance['feature'][:n].tolist()
		# get train and test dataset by selected features
		X_train_selected = X_train[top_n_features]

		X_test_selected = X_test[top_n_features]

		# retrain the model
		model.fit(X_train_selected, y_train)

		y_pre = model.predict(X_test_selected)

		acc = accuracy_score(y_true=y_test, y_pred=y_pre)
		# precision
		precision = precision_score(y_true=y_test, y_pred=y_pre, pos_label=1)
		# recall
		recall = recall_score(y_true=y_test, y_pred=y_pre, pos_label=1)
		# f1-score
		f1 = f1_score(y_true=y_test, y_pred=y_pre, pos_label=1)


		#print("type of f1: ", type(f1))
		top_k_dict[n] = {
			"acc":"{:.4f}".format(acc),
			"precision_mal":"{:.4f}".format(precision),
			"recall_mal":"{:.4f}".format(recall),
			"f1":"{:.4f}".format(f1),
		}
		print(top_k_dict)
	with open('top_k_metrics_in_fold_{}.json'.format(str(fold_index)), 'w') as f:
		json.dump(top_k_dict, f)

# 5-fold
def get_top_k_features_cv(dataset):

	data = pd.read_csv(dataset, dtype=np.int8)
	
	X = data.drop("label", axis=1)
	y = data["label"]

	# 5-fold cross validation
	skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=True).split(X, y)
	
	fold_index = 0
	for train_index, test_index in skf:
		print("Fold {}".format(fold_index))
		X_train, X_test = X.loc[train_index], X.loc[test_index]
		y_train, y_test = y.loc[train_index], y.loc[test_index]
		wrapper_select(X_train, y_train, X_test, y_test, fold_index)
		fold_index += 1

if __name__ == "__main__":
	get_top_k_features_cv("feature_selection.csv")
