"""
os.listdir("./data_files")

['Churn_simple_approach.csv',
 'Customer-churn-prediction.csv',
 'WA_Fn-UseC_-Telco-Customer-Churn.csv']

"""
import pandas as pd

files = [
 'Churn_simple_approach.csv',
 'Customer-churn-prediction.csv',
 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
]

i=0; df0 = pd.read_csv(f"./data_files/{files[i]}")
i=1; df1 = pd.read_csv(f"./data_files/{files[i]}")
i=2; df2 = pd.read_csv(f"./data_files/{files[i]}")

df0.info()
df1.info()
df2.info()
