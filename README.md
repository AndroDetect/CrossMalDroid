# AndroidDetect

## Dataset
We release a dataset consisting of 90,258 real-world malicious samples and 108,019 benign samples spanning from 2008 to 2022. 
The dataset was designed to be large-scale, balanced, and dependable, which comprises of more than 1,500 malware families and 
encompasses data from API Level 1 to 28.

According to the different purposes of the experiment, the dataset was divided into cross-version and robustness. In the cross-version dataset, we list the sha256 and Android Version of each app. In the robustness dataset, we list the modification time and sha256 of each app.

## Malware Families
The families of the dataset obtained by euphony are stored in a `JSON` file:
```
{"f7888a72146e173317ad88e417f8e85a044f9c8208e9d9cbef894c3ce57102d1": "artemis", "6d98e89888eb41c9a2c24d8dd4f292d4d84d7221c21efa101f13ab0dfa678a55": "jiagu", "8ccb4c212bf800b25937a05edd5aef0412ffd3ce47d51f9c70f97e6137f2376d": "skymobi", "02bc3f1eb1922eae9ec52068c4a9a2ec6391570f79acafa8c155e16936ac5327": "boqx", "89dcd81b007c3f0b8ea9f54393a7e4d0d5e28d9807ed5fc54377813d6a6aac12": "artemis"} 
```

## src
The folder src contains the main code of the feature selection process:

### featureimp.py
The `featureimp.py` file obtains the importance scores of the features, sorts them in descending order according to the importance scores of the features, and saves the results as a `CSV` file.

### get_top_k_features.py
The `get_top_k_features.py` uses the wrapper method to perform feature selection based on the results sorted by feature importance, and saves the results in a `JSON` file.

