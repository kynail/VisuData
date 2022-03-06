import pandas as pd
import numpy as np
import random
from faker import Faker
from random import randrange
from datetime import datetime
import csv
import matplotlib.pyplot as plt

nr_of_customers = 300
fake = Faker('de_DE')
customers = []
amount = []

for customers_id in range(nr_of_customers):

    d1 = datetime.strptime(f'1/1/2021', '%m/%d/%Y')
    d2 = datetime.strptime(f'8/10/2021', '%m/%d/%Y')
    transaction_date = fake.date_between(d1, d2)

    mena = fake.name()
    
    name = fake.pydecimal(right_digits=0, positive=True, min_value=1, max_value=100)

    gender = random.choice(["M", "F"])

    amount1 = fake.pyfloat(right_digits=2, positive=True, min_value=10, max_value=1000)
    a1 = amount1
    
    product_ID = fake.ean(length=8)
    
    amount2 = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=500)
    
    amount3 = fake.pyfloat(right_digits=4, positive=True, min_value=2, max_value=3)
    
    a2 = amount2

    customers.append([transaction_date,mena, name, gender, amount1, product_ID, amount2, amount3])
    amount.append([name, product_ID])
    
customers_df = pd.DataFrame(customers, columns=['Transaction_date', 'Name', 'Age', 'Gender','Amount_earn', 'ID_T', 'Amount_spent', 'Coefficient'])                
pd.pandas.set_option('display.max_columns', None)
print(customers_df)

# rho = np.corrcoef(a1, a2)
coef = np.vstack((a1, a1*2+1))
coef = np.vstack((coef,-coef[0,]*2+1))
# coef = np.vstack((coef,random.normal(1,3,100)))
# print ("hum okay\n ")
# print (coef)

df = pd.DataFrame(customers_df) 
df.to_csv('artificial_dataset.csv')