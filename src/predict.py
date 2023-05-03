import joblib
from os.path import join
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score

def compute_metrics(model_name, y_true, y_pre):
	metrics_dict = {}
	accuracy = accuracy_score(y_true=y_true, y_pred=y_pre)
	precision = precision_score(y_true=y_true, y_pred=y_pre, pos_label=1)
	recall = recall_score(y_true=y_true, y_pred=y_pre, pos_label=1)
	f1 = f1_score(y_true=y_true, y_pred=y_pre, pos_label=1)
	
	metrics_dict[model_name] = {
		"accuracy":"{:.4f}".format(accuracy),
		"recall":"{:.4f}".format(recall),
		"precision":"{:.4f}".format(precision),
		"f1":"{:.4f}".format(f1)
	}
	print(metrics_dict)

# predictions of SVM, RF, KNN, DT
def predict(ml_models_dir, model_name, X_test, y_true):
	model = joblib.load(join(ml_models_dir, model_name))
	y_pre = model.predict(X_test)
	compute_metrics(model_name, y_true=y_true, y_pre=y_pre)

	