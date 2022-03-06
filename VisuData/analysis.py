import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
import seaborn as sn

# — Histograms of quantitative variables with a comment on important statistical
# aspects, such as means , standard deviations , etc.
# — A study of potential outliers
# — Correlation matrices (maybe not for all variables)
# — Any interesting analysis : if you have categorical data, with categories are
# represented most ? To what extent ?

cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


df = pd.read_csv('train.csv')
df.drop('Id', axis=1, inplace=True)
df.head()

# Potential outliers
outliers = []
plt.boxplot(df, vert=False)
plt.title("Detecting outliers using Boxplot")
plt.xlabel('Sample')

# histogram of sale price
df['SalePrice'].plot(
    kind='hist',
    # bins=100,
    # xTitle='price',
    # linecolor='black',
    # yTitle='count',
    title='Histogram of Sale Price')


# Correlation matrix
corrMatrix = df.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()
















# df['SalePrice'].iplot(
#     kind='hist',
#     bins=100,
#     xTitle='Power',
#     linecolor='black',
#     yTitle='Acceleration',
#     title='Histogram of Acceleration per power')

# df['cal_per_cup'] = df.calories/df.cups # adding column to look at calorie content per cup rather than per serving