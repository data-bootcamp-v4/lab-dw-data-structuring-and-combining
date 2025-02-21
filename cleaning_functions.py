import pandas as pd

def standardize_cols_names(df):
    # Standardize the column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    # Rename columns for clarity
    df = df.rename(columns={
        "st": "state"
    })

    return df

def clean_inconsistencies(df):
    # Define a dictionary for each column to map inconsistent values to consistent ones
    gender_dict ={"Male": "M", "female": "F", "Female": "F", "Femal": "F"}
    education_dict = {"Bachelors": "Bachelor"}

    # Define a dictionary mapping state abbreviations to state names
    state_dict = {"AZ": "Arizona", "Cali": "California", "WA": "Washington"}

    # Create a dictionary to store the column-specific dictionaries
    column_dicts = {"gender": gender_dict, "education": education_dict, "state": state_dict}
    
    # Clean the data in 'Customer Lifetime Value'
    if df['customer_lifetime_value'].dtypes == "object":
        df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '')
    
    # This is not necessary, is an extra step
    luxury = ["Sports Car", "Luxury SUV", "Luxury Car"]
    df["vehicle_class"] = df["vehicle_class"].apply(lambda x: "Luxury" if x in luxury else x)
    
    # Loop through each column in the dataset and clean the inconsistent values using the corresponding dictionary mapping
    for col in column_dicts:
        df[col] = df[col].replace(column_dicts[col])

    # Verify that each column contains only consistent values
    for col in column_dicts:
        print(col + ":", df[col].unique())
    return df
def formatting_data_types(df):
    # Convert 'Customer Lifetime Value' column to numeric datatype
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')
    if df['number_of_open_complaints'].dtypes == "object":
        df['number_of_open_complaints'] = df['number_of_open_complaints'].str.split('/').str[1]

    df["number_of_open_complaints"] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce')
    # Select only the columns that contain numeric values
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    # Convert the numeric values to integers using applymap
    df = dealing_nulls(df) # need to call here dealing with nulls otherwise cant transform to int
    df[numeric_cols] = df[numeric_cols].map(int)


    return df

def dealing_nulls(df):
    # Identify any columns with null or missing values
    null_cols = df.columns[df.isnull().any()]

    # Print the columns with null or missing values
    print("Columns with null or missing values:")
    print(null_cols)

    # Separate categorical and numerical variables
    cat_vars = df.select_dtypes(include=["object"]).columns
    num_vars = df.select_dtypes(include=["float64", "int64"]).columns

    # Fill null values in categorical variables with the mode
    for col in null_cols:
        if col in cat_vars:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Fill null values in numerical variables with the mean
    for col in null_cols:
        if col in num_vars:
            df[col] = df[col].fillna(df[col].mean())

            # Verify that all null values have been handled
    null_cols = df.columns[df.isnull().any()]
    if len(null_cols) == 0:
        print("All null values have been successfully handled")
    else:
        print("Null values still exist in the following columns:")
        print(null_cols)
        
    return df

def dealing_duplicates(df):
    # drop duplicates
    df.drop_duplicates(inplace=True)

    # reset the index
    df.reset_index(drop=True, inplace=True)

    print(df.duplicated().sum()/df.shape[0])
    return df

def clean_format_main(df):
    df = standardize_cols_names(df)
    df = clean_inconsistencies(df)
    df = formatting_data_types(df)
    #df = dealing_nulls(df) its not called inside formatting
    df = dealing_duplicates(df)
    return df