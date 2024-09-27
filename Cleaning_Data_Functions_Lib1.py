#!/usr/bin/env python
# coding: utf-8

# In[116]:


import pandas as pd 


# In[117]:


import numpy as np


# In[118]:


def rename_columns(df):
    df.columns = ['customer', 'state', 'gender', 'education', 'customer_lifetime_value', 'income', 'monthly_premium_auto',
       'number_of_open_complaints', 'policy_type', 'vehicle_class', 'total_claim_amount']
    return df


# In[119]:


def clean_gender_column(df):
    gender_mapping = {
    'F': 'F',
    'M': 'M',
    'Femal': 'F',
    'Male': 'M',
    'female': 'F',
}
    df['gender'] = df['gender'].map(gender_mapping)
    return df


# In[120]:


def clean_state_column(df):
    state_mapping = {
    'AZ': 'Arizona',
    'Cali': 'California',
    'WA': 'Washington',
    'Arizona': 'Arizona',
    'California': 'California',
    'Washington': 'Washington',
    'Nevada': 'Nevada',
    'Oregon': 'Oregon',
}
    df['state'] = df['state'].map(state_mapping)
    return df


# In[121]:


def clean_education_column(df):
    education_mapping = {
    'Master': 'Master',
    'Bachelor': 'Bachelor',
    'Bachelors': 'Bachelor',
    'High School or Below': 'High School or Below',
    'College': 'College',
    'Doctor': 'Doctor',
}
    df['education'] = df['education'].map(education_mapping)
    return df


# In[122]:


def clean_customer_lifetime_value_column(df):
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(str).str.replace('%', '')
    return df


# In[123]:


def clean_vehicle_class_column(df):
    vehicle_class_mapping = {
    'Four-Door Car': 'Four-Door Car',
    'Two-Door Car': 'Two-Door Car',
    'SUV': 'SUV',
    'Luxury SUV': 'Luxury',
    'Sports Car': 'Luxury',
    'Luxury Car': 'Luxury',
}
    df['vehicle_class'] = df['vehicle_class'].map(vehicle_class_mapping)
    return df


# In[124]:


def convert_customer_lifetime_value_to_float(df):
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(float)
    return df


# In[125]:


def format_number_of_open_complaints(df):
    import numpy as np
    def extract_middle_value(x):
        if isinstance(x, str):
            parts = x.split('/')
            return str(parts[1].strip()) if len(parts) == 3 else np.nan
        else:
            return np.nan
    df["Number of Open Complaints"] = df["Number of Open Complaints"].apply(extract_middle_value)
    return df


# In[126]:


def convert_number_of_open_complaints_to_int(df):
    df['number_of_open_complaints'] = df['number_of_open_complaints'].astype(float)
    df['number_of_open_complaints'] = df['number_of_open_complaints'].astype('Int64')
    return df


# In[127]:


def handle_nullvalues(df):
    categorical_columns = ['state', 'gender', 'education', 'policy_type', 'vehicle_class']
    for col in categorical_columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    numerical_columns = ['customer_lifetime_value', 'income', 'monthly_premium_auto', 'number_of_open_complaints', 'total_claim_amount']
    for col in numerical_columns:
        df[col].fillna(df[col].median(), inplace=True)
    return df


# In[128]:


def add_customer_identifier(df):
    df['customer'] = pd.factorize(df['customer'])[0] + 1
    return df


# In[129]:


#def convert_numerical_columns_to_int(df):
    #numerical_columns = ['customer_lifetime_value', 'income', 'monthly_premium_auto', 'number_of_open_complaints', 'total_claim_amount']
    #df[numerical_columns] = df[numerical_columns].astype(int)
    #return df


# In[130]:


def deal_with_duplicates(df):
    cleaned_df = df.drop_duplicates()
    cleaned_df.reset_index(drop=True, inplace=True)
    df = cleaned_df
    return df


# In[131]:


def clean_data(df):
    rename_columns(df)
    clean_gender_column(df)
    clean_state_column(df)
    clean_education_column(df)
    clean_customer_lifetime_value_column(df)
    clean_vehicle_class_column(df)
    convert_customer_lifetime_value_to_float(df)
    format_number_of_open_complaints(df)
    convert_number_of_open_complaints_to_int(df)
    handle_nullvalues(df)
    add_customer_identifier(df)
    #convert_numerical_columns_to_int(df)
    deal_with_duplicates(df)
    return df


# In[ ]:




