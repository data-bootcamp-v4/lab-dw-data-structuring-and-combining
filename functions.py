import pandas as pd
import sys

def load_data(url):
    """Load dataset from a given URL."""
    return pd.read_csv(url)

def standardize_column_names(df):
    """Standardize column names: lower case, replace spaces with underscores, rename 'st' to 'state'."""
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.rename(columns={'st': 'state'}, inplace=True)
    return df

def clean_invalid_values(df):
    """Clean inconsistent values in the dataset."""
    df['gender'] = df['gender'].replace({'Femal': 'F', 'Male': 'M', 'female': 'F'})
    df['state'] = df['state'].replace({'Cali': 'California', 'AZ': 'Arizona', 'WA': 'Washington'})
    df['education'] = df['education'].replace('Bachelors', 'Bachelor')
    if df['customer_lifetime_value'].dtype == 'object':
        df['customer_lifetime_value'] = df['customer_lifetime_value'].str.rstrip('%')
    df['vehicle_class'] = df['vehicle_class'].replace({'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'})
    return df

def format_data_types(df):
    """Format the data types of specific columns."""
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(float)
    if df['number_of_open_complaints'].dtype == 'object':
        df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'].str.split('/').str[1], errors='coerce')
    return df

def handle_null_values(df):
    """Handle null values by dropping rows with all null values and filling remaining NaNs."""
    df.dropna(how='all', inplace=True)
    df['gender'].fillna('U', inplace=True)
    customer_lifetime_value_mean = df['customer_lifetime_value'].mean()
    df['customer_lifetime_value'].fillna(customer_lifetime_value_mean, inplace=True)
    df.dropna(inplace=True)
    return df

def remove_duplicates(df):
    """Remove duplicate rows from the dataset."""
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def save_cleaned_data(df, file_name='cleaned_data.csv'):
    """Save the cleaned dataset to a CSV file."""
    df.to_csv(file_name, index=False)

# Main script
def main_clean_data(url, output_file='cleaned_data.csv'):
    data = load_data(url)
    
    data = standardize_column_names(data)
    data = clean_invalid_values(data)
    data = format_data_types(data)
    data = handle_null_values(data)
    data = remove_duplicates(data)
    
    save_cleaned_data(data, output_file)

    # Display the cleaned data (optional)
    print(data.head())

def show_unique_values(df, threshold=10):
    """
    Prints the unique values in each column of a DataFrame if the number of unique values is less than a specified threshold.

    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.
    threshold (int): The maximum number of unique values a column can have to be printed. Default is 10.
    """
    for column in df.columns:
        if df.nunique()[column] < threshold:
            print(f"Column '{column}': {df[column].unique()}")
