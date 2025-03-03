
import pandas as pd


url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file3.csv"
df = pd.read_csv(url)
 
def show_columns(df):
    print(f"Data Frame columns are: {df.columns}")
    return
   

def format_column_names(df):
    df.columns = df.columns.str.lower() # To make all column names in lower case
    df.columns = df.columns.str.replace(" ", "_") #To replace spaces in column names with "_"
    print(f"Date Frame columns names modified are: {df.columns}")
    return df

def rename_column_st(df):
    df = df.rename(columns={'st': 'state'})
    return df


def clean_invalid_data(df):
    df['gender'] = df['gender'].str.replace("female", "F").replace("Femal", "F").replace("Male", "M")
    df['state'] = df['state'].str.replace("AZ", "Arizona").replace("WA", "Washington").replace("").replace("California", "Cali")
    df['state'] = df['state'].str.replace("Cali", "California")
    df['education'] = df['education'].str.replace("Bachelors", "Bachelor")
    
    # Verificar si 'customer_lifetime_value' es numérico antes de convertir a string
    if df["customer_lifetime_value"].dtype != "O":  
        df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(str)

    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "", regex=False)
    df["vehicle_class"] = df["vehicle_class"].str.replace("Sports Car", "Luxury").replace("Luxury SUV", "Luxury").replace("Luxury Car", "Luxury")

    return df



def format_data_types(df):
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"], errors="coerce")

    # Verificar si 'number_of_open_complaints' es numérico antes de convertir a string
    if df["number_of_open_complaints"].dtype != "O":
        df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(str)

    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.replace('/00', '', regex=False)
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.replace('1/', '', regex=False)
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors="coerce")  # Convertir a número
    return df



def deal_with_null_values(df):
    df.dropna(how = "all")
    df = df.dropna(how = "all")
    df.dropna(subset=["customer_lifetime_value"], inplace = True)
    df["gender"] = df["gender"].fillna(method = 'ffill')
    return df


def reset_indexes(df):
    df.reset_index(drop=True)
    return df


def clean_dataset(df, output_name):
    df = format_column_names(df)
    df = rename_column_st(df)
    df = clean_invalid_data(df)
    df = format_data_types(df)
    df = deal_with_null_values(df)
    df = reset_indexes(df)
    
    globals()[output_name] = df  # Asigna el DataFrame a una variable con el nombre deseado
    return df

# nombre  para el DataFrame limpio:
nombre_df = "df_limpio3"

# Llamas a la función con el nombre elegido
df_limpio3 = clean_dataset(df, nombre_df)

# Muestra el DataFrame limpio
print(df_limpio3.head())
