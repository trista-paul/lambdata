"""
utility functions for working with dataframes.
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])

def outlier_cleaner(df):
  for label, col in df.iteritems():
    Q1 = col.quantile(0.25)
    Q3 = col.quantile(0.75)
    IQR = Q3 - Q1
    df = df[((Q1 -(IQR*1.5)) <= col) & (col <= (Q3 +(IQR*1.5)))]
  return df
  
def datetime_splitter(df, col): #accepts DataFrame and time column
  import datetime
  df[col] = pd.to_datetime(df[col])
  df['year'] = df[col].dt.year
  df['month'] = df[col].dt.month
  df['day'] = df[col].dt.day
  df = df.drop(columns = col)
  return df
  
