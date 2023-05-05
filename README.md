# AndroidDetect

## Dataset
We release a dataset consisting of 90,258 realworld malicious samples and 108,019 benign samples spanning from 2008 to 2022. 
The dataset was designed to be large-scale, balanced, and dependable, which comprises of more than 1,500 malware families and 
encompasses data from API level 1 to 28.

The dataset was divided into a train set and a test set. There are 455 columns: "apk_sha256", "label" and 453 features extracted by androguard. The malwares were marked as 1 and the benigns were marked as 0.

## Malware Families
The families of the dataset obtained by euphony are stored in a `json` file:
```
"f7888a72146e173317ad88e417f8e85a044f9c8208e9d9cbef894c3ce57102d1": "artemis", "6d98e89888eb41c9a2c24d8dd4f292d4d84d7221c21efa101f13ab0dfa678a55": "jiagu", "8ccb4c212bf800b25937a05edd5aef0412ffd3ce47d51f9c70f97e6137f2376d": "skymobi", "02bc3f1eb1922eae9ec52068c4a9a2ec6391570f79acafa8c155e16936ac5327": "boqx", "89dcd81b007c3f0b8ea9f54393a7e4d0d5e28d9807ed5fc54377813d6a6aac12": "artemis", 
```

## Models
DT(Decision Tree), KNN, RF(Random Forest) and SVM are four models trained by the train set, all the models achieved over 96% F1-score, and the random forest model reached over 98.5% in precision, recall, accuracy and F1.

## Example
For instance, to evaluate the models on the test set, run as:

### Installation
```shell
pip install -r requirements.txt 
```

### Evaluate
Enter the src directory:
```shell
cd src
```

Run evaluation:
```shell
python main.py
```

Waiting for a while and the cmd will print the metrics on test set of every model:
```
{'KNN': {'accuracy': '0.9803', 'recall': '0.9715', 'precision': '0.9851', 'f1': '0.9783'}}
{'SVM': {'accuracy': '0.9713', 'recall': '0.9624', 'precision': '0.9743', 'f1': '0.9683'}}
{'DT': {'accuracy': '0.9773', 'recall': '0.9761', 'precision': '0.9741', 'f1': '0.9751'}}
{'RF': {'accuracy': '0.9878', 'recall': '0.9853', 'precision': '0.9878', 'f1': '0.9866'}}
```
