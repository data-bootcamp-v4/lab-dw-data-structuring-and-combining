import pandas as pd
import numpy as np

def clean_column_names(df):
    df_columns = [ 'customer', 'state', 'customer_lifetime_value', 'education', 'gender',  'income', 'monthly_premium', 'number_open_complaints','policy_type', 'total_claim_amount',  'vehicle_class']

    df.columns = df_columns
    return df

def clean_and_convert_customer_lifetime_value(df):
    # Ensure the column is treated as a string before cleansing
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(str)

    # Remove non-numeric symbols (%, commas)
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('[^0-9.]', '', regex=True)

    # Convert to numeric, coercing errors to NaN
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')
    return df

def extract_middle_value(df):
    
    def get_middle_value(value):
   
        if isinstance(value, str):
            parts = value.split('/')  # Split the string by '/'
            return int(parts[1]) if len(parts) > 1 else 0  # Return the middle value if it exists, otherwise return 0.
        else:
            return 0
    # Apply the function to convert the entire column.
    df['number_open_complaints'] = df['number_open_complaints'].apply(get_middle_value)
    return df

def fill_missing_values(df):
    df['state'] = df['state'].fillna('Unknown')
    df['customer'] = df['customer'].fillna('Invalid')
    df['gender'] = df['gender'].fillna('Divers')
    df['education'] = df['education'].fillna('Unknown')
    df['policy_type'] = df['policy_type'].fillna('Invalid')
    return df

#def replace_zero_with_nan(df, column_name):
 #   mask_all_null_except = df.drop(columns=[column_name]).isnull().all(axis=1)
  #  df.loc[mask_all_null_except, column_name] = df.loc[mask_all_null_except, column_name].replace(0, np.nan)
   # return df
#make function (nested if statements)


def fill_missing_income(df):
    vehicle_classes = ['Luxury', 'Four-Door Car', 'Two-Door Car', 'SUV']
    mean_incomes = {}
    #calculate mean incomes
    for vehicle_class in vehicle_classes:
        class_df = df[df['vehicle_class'] == vehicle_class]
        mean_incomes[vehicle_class] = class_df['income'].mean()
    #define row wise function
    def fill_value(row):
        if pd.isnull(row['income']):
            return mean_incomes.get(row['vehicle_class'], row['income'])
        return row['income']
    
    df['income'] = df.apply(fill_value, axis=1)
    return df

def fill_missing_customer_life_value(df):
    vehicle_classes = ['Luxury', 'Four-Door Car', 'Two-Door Car', 'SUV']
    
    # Calculate means
    mean_values = {}
    for vc in vehicle_classes:
        non_nan_values = df[df['vehicle_class'] == vc]['customer_lifetime_value'].dropna()
        mean_values[vc] = non_nan_values.mean() if not non_nan_values.empty else 0
        print(f"Mean for {vc}: {mean_values[vc]} based on {len(non_nan_values)} records")

    # Define row-wise filling function
    def fill_value(row):
        if pd.isnull(row['customer_lifetime_value']):
            return mean_values.get(row['vehicle_class'], 0)
        return row['customer_lifetime_value']
    
    df['customer_lifetime_value'] = df.apply(fill_value, axis=1)
    return df


def drop_duplicate_rows(df, subset=None):
    return df.drop_duplicates(subset=subset)

# Main function to perform all cleaning steps
def clean_data(df):
    df = clean_column_names(df)
    df = clean_and_convert_customer_lifetime_value(df)
    df = extract_middle_value(df)
    df = fill_missing_values(df)
    df = fill_missing_income(df)
    df = fill_missing_customer_life_value(df)
    df = drop_duplicate_rows(df)
    return df