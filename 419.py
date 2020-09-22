import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mpl
import seaborn as sns
import pyreadstat
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/pcworld/Documents/Research/Files/low_birth_weight_BDHS_combined.csv")

print('hello')

#print(df.head(10))

#print(df.isnull().sum())

ndrop=df.dropna(axis='columns',how='all')             #dropping columns with all null values

#print(ndrop.isnull().sum())

#print(ndrop.shape)

ndrop=ndrop.drop(columns=['M57A_1','M57E_1'])

#print(ndrop.isnull().sum())

ndrop.to_csv("/Users/pcworld/Documents/Research/Files/ndropped.csv")

selected=ndrop[['V007','V012','V013','V020','V201','V212','V213','V214','V215','V216','V218','V225','V229','V233','V445','V446','V501','V716','B4_01','B5_01','B8_01','M1_1','M17_1','M18_1','M18_2','M18_3','H10_1','HW1_1','HW2_1','HW3_1']]

selected.to_csv("/Users/pcworld/Documents/Research/Files/sliced_horiz.csv")

print(selected.head())


year1114=selected.iloc[21034:54506]

print(year1114.head())

year1114.to_csv("/Users/pcworld/Documents/Research/Files/g11_14.csv")                   #2011 and 2014 data

g1114=pd.read_csv("/Users/pcworld/Documents/Research/Files/g11_14.csv")


#print(g1114.isnull().sum())

temp=g1114.dropna(subset=['M18_1'])

#print(temp.isnull().sum())

temp.to_csv("/Users/pcworld/Documents/Research/Files/g11_14nn.csv")

temp1=pd.read_csv("/Users/pcworld/Documents/Research/Files/g11_14nn.csv")

#print(temp1.head())

temp2=temp1.drop(df.iloc[:, 1:2], axis=1)

print(temp2.head())