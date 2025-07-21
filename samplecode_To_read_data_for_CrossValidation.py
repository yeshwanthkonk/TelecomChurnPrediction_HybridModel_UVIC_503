import pandas as pd
import json

# load dataset from CSV
df = pd.read_csv('/content/WA_Fn-UseC_-Telco-Customer-Churn.csv')
X = df.drop(columns="Churn").values
y = df["Churn"].values

with open("cross_validation_split.json", "r") as f: # ./data_files/cross_validation_split.json
    cv_data = json.load(f)

folds = cv_data["folds"]
test_indices = cv_data["test_indices"]
# use i for each fold
i = 0  # Change this to run through all folds

train_idx = folds[i][0]
val_idx = folds[i][1]

X_train = X[train_idx]
y_train = y[train_idx]

X_val = X[val_idx]
y_val = y[val_idx]

# we can use below logic as well, instead of using i to update manually
for fold_i in range(len(folds)):
  pass # do training and validation on each fold


# ------ after all fold training finished use below for testing
X_test = X[test_indices]
y_test = y[test_indices]