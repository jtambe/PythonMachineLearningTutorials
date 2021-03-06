import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL")

#print(df.head())
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / (df['Adj. Close']) * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / (df['Adj. Open']) * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
#print(df.head())

forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)

forecast_out = int( math.ceil(0.01*len(df)) )

df['label'] = df[forecast_col].shift(-forecast_out)

print(df.head())
#tutorial 3 done

#features are X
#drops label and converts in numpy array
X = np.array(df.drop(['label',1]))
#labels are y
y = np.array(df(['label']))

X = preprocessing.scale(X)