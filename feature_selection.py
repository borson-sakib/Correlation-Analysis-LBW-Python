import seaborn as sn
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


data=pd.read_csv('/Users/pcworld/Desktop/sample_25.csv')

#data=df.head(30)

corrmat=data.corr()

#print(corrmat)

#sn.heatmap(corrmat,annot=True)

top_corr_features= corrmat.index

plt.figure(figsize=(10,10))

g=sn.heatmap(data[top_corr_features].corr(),annot=True,cmap='RdYlGn')

plt.show()