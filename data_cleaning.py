def load_df(url):
   import pandas as pd
   df_name = pd.read_csv(url)
   return df_name

def column_names(df_name):
    import pandas as pd
    for column in df_name.columns:
        df_name = column.strip().lower().replace(" ","_")
        return df_name
    
def column_names(df_name):
    #the column names of a DF to lowercase and replace 
    # spaces with underscores
    import pandas as pd
    new_column_name = [col.strip().lower().replace(" ", "_") for col in df_name.columns]
    df_name.columns = new_column_name

def dimensions(df):
    #dimesions of the dataframe
    return(print(f"Rows and columns in data frame: {df.shape}"))


def df_concat(df1, df2, df3):
    #to concatenate three DF
    import pandas as pd
    new_df = pd.concat([df1, df2, df3], axis=0)
    return new_df

#get the value of each column values
def unique_value_col(df_mkt, col):
    unique_values = df_mkt[col].unique()
    return(f"Unique values in column '{col}': {unique_values}\n")