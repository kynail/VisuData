import pandas as pd
import numpy as np
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import cufflinks as cf
import seaborn as sn

# parallel coordinate plot

df = pd.read_csv('train.csv')
df.sort_values(by='SalePrice', inplace=True)
df.reset_index(inplace=True)
df.drop(columns=['Id'], inplace=True)
df.head(10)

plt.figure(figsize=(20, 5))
ax = plt.subplot(1,2,1)
ax = df[['SalePrice','LotArea']][:40].plot.bar(x='SalePrice', xlabel = '', ax=ax)
ax = plt.subplot(1,2,2)
df[['SalePrice','LotArea']][:40].plot.bar(x='SalePrice', xlabel = '', ax=ax)