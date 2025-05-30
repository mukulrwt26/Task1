import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

def transform_data(df):
    print("Transforming data.")
    df.rename(columns={'Purchase Amount (USD)':'Purchase Amount'},inplace=True)

    #filling missing valuues

    df['Review Rating']=df['Review Rating'].fillna(df['Review Rating'].mean())

    df['Purchase Amount']=df['Purchase Amount'].fillna(df['Purchase Amount'].median())

    #handdling outliers
    df['Purchase Amount']=df['Purchase Amount'].astype('float')

    Q1=df['Purchase Amount'].quantile(0.25)
    Q3=df['Purchase Amount'].quantile(0.75)

    IQR=Q3-Q1
    lower_fence=Q1-1.5*IQR
    high_fence=Q3+1.5*IQR
    outliers=df[(df['Purchase Amount']<lower_fence) | (df['Purchase Amount']>high_fence)]

    df['Purchase Amount']=df['Purchase Amount'].clip(upper=high_fence)

    #encoding
    label=LabelEncoder()
    df['Item Purchased']=label.fit_transform(df['Item Purchased'])
    df['Payment Method']=label.fit_transform(df['Payment Method'])

    

    #feature construction 
    df['Date']=df['Date Purchase'].str.split('-').str[0].astype('int')
    df['Month']=df['Date Purchase'].str.split('-').str[1].astype('int')
    df['Year']=df['Date Purchase'].str.split('-').str[2].astype('int')
    
    #dropping the column for more intrest
    df.drop('Date Purchase', axis=1, inplace=True)
    
    #standardization 
    scale=StandardScaler()
    df['Purchase Amount Scaled']=scale.fit_transform(df[['Purchase Amount']])

    print('Data Transformed.')

    return df






