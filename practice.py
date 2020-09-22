import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data=pd.read_csv('/Users/pcworld/Desktop/g11_14nn.csv')

x=data.iloc[:,0:5]
y=data.iloc[:,-1]

bestfeatures= SelectKBest(score_func=chi2,k=5)
fit=bestfeatures.fit(x,y)

dfscores=pd.DataFrame(fit.scores_)
dfcolumns=pd.DataFrame(x.columns)

featureScores=pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns=['Specs','Score']

print(featureScores)