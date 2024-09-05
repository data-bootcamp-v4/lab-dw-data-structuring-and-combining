import pandas as pd

def read_csv_file(url):
    file_path = url
    df = pd.read_csv(file_path)
    return df

def clean_columns_names(dataframe):

    dataframe.columns = dataframe.columns.str.lower().str.replace(' ', '_')

    return dataframe

def clean_values(dataframe):

    replacements = {
        'F': 'F', 'M': 'M', 'Femal': 'F', 'Male': 'M', 'female': 'F',
        'WA': 'Washington', 'AZ': 'Arizona', 'Cali': 'California',
        'Bachelors': 'Bachelor', 'Sports Car' : 'Luxury', 'Luxury Car' : 'Luxury',
        'Luxury SUV' : 'Luxury'
    }

    cleaning_data = dataframe.replace(replacements)

    cleaning_data = cleaning_data.replace('%', '', regex=True)

    return cleaning_data


def clean_number_of_complaints(dataframe, column_name):

    dataframe[column_name] = dataframe[column_name].apply(lambda x: (x.split('/')[1] if '/' in x else x) if isinstance(x, str) else x)

    return dataframe


def to_numeric_values(dataframe, column_name):

    dataframe[column_name] = pd.to_numeric(dataframe[column_name], errors='coerce')

    dataframe[column_name] = dataframe[column_name].reindex(dataframe.index)

    return dataframe


def clean_nulls(dataframe):

    dataframe = dataframe.dropna(how='all')

    return dataframe

def change_dtype_str(dataframe):

    dataframe = dataframe.astype(str)

    return dataframe

def fill_categorical_columns(dataframe, columns):

    for col in columns:
        if dataframe[col].dtype == 'object':
            dataframe[col].fillna(dataframe[col].mode()[0], inplace=True)

    return dataframe

def fill_numerical_columns(dataframe, columns):

    for col in columns:
        if pd.api.types.is_numeric_dtype(dataframe[col]):
            dataframe[col].fillna(dataframe[col].mean(), inplace=True)

    return dataframe