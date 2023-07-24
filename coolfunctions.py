#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def lower_snake(df):

    lower_and_snake = lambda x: x.lower().replace(" ","_")

    df.columns = list(map(lower_and_snake,list(df.columns)))
    
    return df

def correct_null(df):

    for x in list(df.columns):
        if df[x].dtype == object:
            df[x] = df[x].fillna('unknown')
    
        else:
            df[x]= df[x].fillna("0")

    return df