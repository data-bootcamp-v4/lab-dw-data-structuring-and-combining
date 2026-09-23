import pandas as pd


def clean_column_names(df):
    df = df.rename(columns={'ST': 'state'})
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def clean_invalid_values(df):
    df['gender'] = df['gender'].replace({'Femal': 'F', 'female': 'F', 'Male': 'M'})
    df['state'] = df['state'].replace({'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'})
    df['education'] = df['education'].replace({'Bachelors': 'Bachelor'})
    df['vehicle_class'] = df['vehicle_class'].replace(
        {'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'}
    )
    return df


def format_data_types(df):
    if df['customer_lifetime_value'].dtype == 'object':
        df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '')
        df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(float)
    else:
        pass

    if df['number_of_open_complaints'].dtype == 'object':
        df['number_of_open_complaints'] = df['number_of_open_complaints'].str.split('/').str[1]
        df['number_of_open_complaints'] = df['number_of_open_complaints'].astype(float)
    else:
        pass
   
    
    return df


def handle_nulls(df):
    gender_mode = df['gender'].mode()[0]
    df['gender'] = df['gender'].fillna(gender_mode)

    clv_median = df['customer_lifetime_value'].median()
    df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(clv_median)

    income_median = df['income'].median()
    df['income'] = df['income'].fillna(income_median)

    premium_median = df['monthly_premium_auto'].median()
    df['monthly_premium_auto'] = df['monthly_premium_auto'].fillna(premium_median)

    complaints_median = df['number_of_open_complaints'].median()
    df['number_of_open_complaints'] = df['number_of_open_complaints'].fillna(complaints_median)

    df = df.dropna(how='all')

    df['income'] = df['income'].astype(int)
    df['monthly_premium_auto'] = df['monthly_premium_auto'].astype(int)
    df['number_of_open_complaints'] = df['number_of_open_complaints'].astype(int)
    return df


def remove_duplicates(df):
    df = df.drop_duplicates()
    return df
