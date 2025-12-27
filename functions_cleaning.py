import pandas as pd 
import numpy as np
from functions_cleaning import clean_column_names
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame: 
    df = df.copy() 
    df.columns = ( 
    df.columns 
    .str.strip() 
    .str.lower() 
    .str.replace(' ', '_') 
    .str.replace('%', '', regex=False) ) 
return df 

def clean_types(df: pd.DataFrame) -> pd.DataFrame: 
    df1 = df.copy() 
    # Conversion des colonnes 
    numériques num_cols = ['customer_lifetime_value', 'income', 'monthly_premium_auto', 'total_claim_amount'] 
    for col in num_cols: 
        if col in df1.columns: 
            df1[col] = pd.to_numeric(df1[col], errors='coerce') 
    # Conversion des plaintes ouvertes 
    if 'number_of_open_complaints' in df1.columns: 
        df1['number_of_open_complaints'] = pd.to_numeric(df1['number_of_open_complaints'], errors='coerce') 
        return df1 
        
def clean_values(df: pd.DataFrame) -> pd.DataFrame: 
    df1 = df.copy() 
    # Nettoyage de la colonne gender 
    if 'gender' in df1.columns: 
        df1['gender'] = df1['gender'].str.strip().str.upper() 
        df1['gender'] = df1['gender'].map({'F': 0, 'M': 1}) 
    return df1 
    
def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame: 
    df1 = df.copy() 
    # Exemple : remplir les NaN dans gender avec -1 
    if 'gender' in df1.columns: 
        df1['gender'] = df1['gender'].fillna(-1) 
        # Autres colonnes numériques : remplir avec médiane 
        num_cols = ['income', 'customer_lifetime_value', 'monthly_premium_auto', 'total_claim_amount'] 
        for col in num_cols: 
            if col in df1.columns: 
                median = df1[col].median() 
                df1[col] = df1[col].fillna(median) 
        return df1


def clean_duplicates(df: pd.DataFrame) -> pd.DataFrame: 
    df1 = df.copy() 
    # Supprimer colonnes dupliquées 
    df1 = df1.loc[:, ~df1.columns.duplicated()] 
    # Supprimer lignes dupliquées 
    df1 = df1.drop_duplicates().reset_index(drop=True) 
    return df1 
    
    
def clean_df(df: pd.DataFrame) -> pd.DataFrame: 
    df1 = df.copy() 
    df1 = clean_column_names(df1) 
    df1 = clean_types(df1) 
    df1 = clean_values(df1) 
    df1 = clean_duplicates(df1) 
    return df1


    
df1 = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv") 
df2 = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file2.csv") 
df3 = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file3.csv") 
df1_clean = clean_df(df1) 
df2_clean = clean_df(df2) 
df3_clean = clean_df(df3)