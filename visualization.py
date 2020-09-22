import numpy as np
import pandas as pd
import scipy as sp
import matplotlib as mpl
import seaborn as sns
import pyreadstat
import matplotlib.pyplot as plt

temp1 = pd.read_csv('/Users/pcworld/Desktop/g11_14nn_2.csv')

print(temp1.head())

temp1[['V012']].plot(kind='hist')

plt.show()

#plt.figure();

#temp1['']