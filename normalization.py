import pandas as pd
import matplotlib as mpl


data=pd.read_csv('/Users/pcworld/Desktop/g11_14nn_2.csv')

data['V012']=data['V012']/100
data['V212']=data['V212']/100
data['V445']=data['V445']/1000
data['V446']=data['V446']/1000


print(data.head())

print(data.info())

