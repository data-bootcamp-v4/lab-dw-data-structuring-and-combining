# THIS IS THE FILE WITH FUNCTIONS TO CLEAN

def clean_column_names(column_name)
    # Exercise 1: Cleaning Column Names
    df_cars_policies = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv") # Leer la database desde un CSV
    df_cars_policies.rename(columns={"ST": "STATE"}, inplace = True) #Cambiar nombre de columna
    df_cars_policies.columns = df_cars_policies.columns.str.lower().str.replace(" ", "_") # Poner todos los nombres de columna en minúscula
    df_cars_policies