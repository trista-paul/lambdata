"""
utility functions for working with dataframes.
"""


import pandas as pd
import numpy as np
import os


"""import, load dataset from UCI with datetime, string and int columns"""
os.system("wget http://archive.ics.uci.edu/ml/machine-learning-databases/00482/dataset.zip")
os.system("unzip dataset.zip")
TEST_DF = pd.read_csv('dataset.csv')


def outlier_cleaner(df):
    """removes float more than Q3+IQR*1.5 or less than Q1-IQR*1.5"""
    """accepts DataFrame"""
    num = df.select_dtypes(include=np.number)
    for label, col in num.iteritems():
        Q1 = col.quantile(0.25)
        Q3 = col.quantile(0.75)
        IQR = Q3 - Q1
        clean = num[((Q1 - (IQR*1.5)) <= col) & (col <= (Q3 + (IQR*1.5)))]
        df = pd.concat([df, clean], axis=1)
        df = df.dropna()
        df = df.drop(columns=num)
    return df


def datetime_splitter(df, col):
    """splits date format column into year, month, day columns"""
    """accepts DataFrame and date format column"""
    import datetime
    if col.dtype != np.datetime64:
        col = pd.to_datetime(col)
    df['year'] = col.dt.year
    df['month'] = col.dt.month
    df['day'] = col.dt.day
    return df
