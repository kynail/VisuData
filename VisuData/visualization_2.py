import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
import seaborn as sn

#  This means 2 different method of visualization
# (for instance a parallel coordinate plot and / or scatter plots / and or a hierarchical
# clustering).
# These progra

df = pd.read_csv('train.csv')
df.head()

sn.scatterplot(x='SalePrice', y='LotArea', data=df)
