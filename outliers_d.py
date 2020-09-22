import pandas as pd

data=pd.read_csv('/Users/pcworld/Desktop/binarized.csv')

data.drop(data.index[data['V445'] == 9.999], inplace = True)

print(data)

data.to_csv('/Users/pcworld/Desktop/outlier_del.csv')