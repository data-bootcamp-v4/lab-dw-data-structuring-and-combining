def merge_df(df1,df2):
    import pandas as pd
    df=df1.merge(df2,how="outer")
    return df

def improve_title_columns(df):
    import pandas as pd
    df=df.rename(columns={df.columns[n]:df.columns[n].strip().replace(" ","_").lower() for n in range(len(df.columns))})
    #rename column st to state
    df=df.rename(columns={"st":"state"})
    df.columns
    return df

def data_standarization(df):
    import pandas as pd

    gender_values={ #creates a dictionary with the values and corrections
    "F":"F",
    "Femal":"F",
    "female":"F",
    "Male":"M"}

    state_values={ #creates a dictionary with the values and corrections
        "Oregon":"Oregon",
        "California":"California",
        "Cali":"California",
        "Arizona":"Arizona",
        "AZ":"Arizona",
        "Washington":"Washington",
        "WA":"Washington",
        "Nevada":"Nevada",
        }

    education_values={ #creates a dictionary with the values and corrections
        "Bachelors":"Bachelor"
            }

    vehicle_class_values={ #creates a dictionary with the values and corrections
        "Sports Car":"Luxury",
        "Luxury SUV":"Luxury",
        "Luxury Car":"Luxury",
        }

    df["gender"]=df["gender"].replace(gender_values)
    df["state"]=df["state"].replace(state_values) #replace with correct values 
    df["state"]=df["state"].replace(state_values) #replace with correct values 
    df["vehicle_class"]=df["vehicle_class"].replace(vehicle_class_values) #replace with correct values 

    #Replace % caracter with none in customer_lifetime_value 
    df["customer_lifetime_value"]=df["customer_lifetime_value"].str.replace("%","")

    #Cleaning NaN and null values}

    #First cleaning

    datos_iniciales=df.shape[0] #valor del total de filas antes de limpieza
    df=df.dropna(how="all")
    df.fillna(0, inplace=True)
    datos_finales=df.shape[0]

    #complains open format manage
    list_complains_types=df["number_of_open_complaints"].unique()
    list_complains_types=list(list_complains_types)
    list_complains=[list_complains_types[n][2].split("/") for n in range(len(list_complains_types))]
    dict_complains=dict(zip(list_complains_types,list_complains))

    df["number_of_open_complaints"]=df["number_of_open_complaints"].replace(dict_complains)

    #changing data type
    df["vehicle_class"]=df["vehicle_class"].astype("object")
    df["customer_lifetime_value"]=df["customer_lifetime_value"].astype("float64")
    df["number_of_open_complaints"]=df["number_of_open_complaints"].astype(int)

    print(f"Data before cleaning: {datos_iniciales}\n Data after cleaning: {datos_finales}")
        
    
    
    return df