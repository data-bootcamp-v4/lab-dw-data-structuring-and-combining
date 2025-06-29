def clean_column_names(df):
    """
    Cleans column names by:
    - Replacing spaces with underscores
    - Converting all column names to lowercase
    """
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = [col.lower() for col in df.columns]
    return df

def clean_gender(df):
    """
    Cleans and standardizes gender values in the 'gender' column of the DataFrame.
    - Strips spaces, converts to lowercase, and fixes common typos.
    - Replaces 'f' and 'm' with 'female' and 'male', then converts back to 'F' and 'M'.
    """
    # Clean original gender values
    df['gender_cleaned'] = df['gender'].str.strip().str.lower()

    # Fix typos in gender values F and M
    df['gender_cleaned'] = df['gender_cleaned'].replace({
        'f': 'female',
        'femal': 'female',
        'm': 'male'})

    df['gender_cleaned'] = df['gender_cleaned'].replace({
        'female': 'F',
        'male': 'M'})

    df['gender'] = df['gender_cleaned']
    df.drop(['gender_cleaned'], axis='columns', inplace=True)

    return df

def clean_state_names(df):    
    df['state'] = df['state'].replace({
        'Cali': 'California',
        'AZ': 'Arizona',
        'WA': 'Washington'})
    return df