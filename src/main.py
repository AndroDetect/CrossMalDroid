import pandas as pd
import os
from os.path import join
import predict

def merge_testset():
	# Benign test samples
	df_1 = pd.read_csv("../dataset/test/Benign_test.csv", index_col="apk_sha256")
	# Malware test samples
	df_2 = pd.read_csv("../dataset/test/Malware_test.csv", index_col="apk_sha256")
	# merge the samples for predicting
	data = pd.concat([df_1, df_2], ignore_index=True)
	X_test = data.drop("label", axis=1)
	# y_true is the real label
	# Malware: 1
	# Benign: 0
	y_true = data["label"]
	return X_test, y_true

def model_predictions():
	X_test, y_true = merge_testset()
	models_dir = "../models"
	models = os.listdir(models_dir)
	for model in models:
		predict.predict(models_dir, model, X_test, y_true)

if __name__ == '__main__':
	# test the machine learning models and print the metrics
	model_predictions()