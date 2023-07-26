
from datetime import datetime as dt
from datetime import timedelta
import re
import pandas as pd
def low_clean_columns(column_name):
    column_name = re.sub(r"[^\w\s\%]", " ", str(column_name).lower())
    return column_name
def types_setting(df):
    df["customer lifetime value"] = df["customer lifetime value"].str.replace("N/A","0")
    df["customer lifetime value"] = df["customer lifetime value"].str.rstrip("%")#Elitminates all the strings
    df["customer lifetime value"] = df["customer lifetime value"].astype(float)
    return df
def spell_checks(df):
    df["gender"].replace(r"(?i)\bM\w*\b",regex=True,value="M",inplace=True)
    df["gender"].replace(r"(?i)\bF\w*\b",regex=True,value="F",inplace=True)
    return df
def cleaning_nulls(df):
    df.dropna(axis=0,how="all",inplace=True) #Cleaning Null Values in the Dataframe
    df.fillna(axis=0,value="N/A",inplace=True)
    return df
def checking_dup(df,column):
    df.drop_duplicates(subset="customer",inplace=True)
    return df
def date_convert(df,column,new_column):
    df[column] = pd.to_datetime(df[column],format="mixed")
    df[new_column] = pd.DatetimeIndex(df[column]).month_name()
    return df

def cleaning_dataframes(df,column):
    df.columns = [low_clean_columns(i) for i in df.columns]
    df=spell_checks(df)
    df=types_setting(df)
    df=cleaning_nulls(df)
    df=checking_dup(df,column)
    df.rename(columns = {'st':'state'}, inplace = True)
    return df