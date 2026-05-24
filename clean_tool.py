import pandas as pd
import numpy as np

def clean_col_name(df_origin):
    df=df_origin.copy()

    df.columns=(df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ","_")
    )

    df = df.rename(columns={
        "st": "state"
        }
    )

    return df

def formatting(df_origin):
    df=df_origin.copy()
    # customer_lifetime_value remove "%"
    if df["customer_lifetime_value"].dtypes == "object":
        df["customer_lifetime_value"]= (df["customer_lifetime_value"].map(
            lambda x:  round(float(x.strip().replace("%",""))/100,2) if pd.notna(x) else x
            )
        )
    elif df["customer_lifetime_value"].dtypes == "float64":
        df["customer_lifetime_value"]= df["customer_lifetime_value"].round(2)
     # number_of_open_complaints 1/0/00 keep only middle number
    if df["number_of_open_complaints"].dtypes == "object":
        df["number_of_open_complaints"]= (df["number_of_open_complaints"].map(
            lambda x:  int(x.strip().split("/")[1]) if pd.notna(x) else x
            )
        )
    df.education=df.education.replace({"Bachelors":"Bachelor"})
    # all numerical to int?

    return df

def clean_duplicates(df_origin):
    df=df_origin.copy()
    df=df.dropna(how="all")
    df=df.dropna(axis=1,how="all")
    df=df.drop_duplicates()
    df=df.reset_index(drop=True)
    return df

def clean_all(df_origin):
    df=df_origin.copy()

    df=clean_col_name(df)
    df=clean_duplicates(df)
    df=formatting(df)

    return df