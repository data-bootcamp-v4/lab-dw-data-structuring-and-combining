def clean_clv_f(value):
    #Get rid of the % sign in the customer_lifetime_value column
    if type(value) == str:
        return float(value.replace("%",""))
    return value

def clean_data_f(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ","_")
    df.rename(columns={"st":"state"}, inplace=True)

def get_complaints_f(value):
    #Split the values in the number_of_open_complaints column to get only the number in the middle
    if type(value) == str:
        return int(value.split("/")[1])
    return value

def standardize_education_f(value):
    #Standardize the values in the education column all Bachelors should be 'Bachelor')
    if type(value) == str:
        return "Bachelor" if value[0].lower() == "b" else value.title()
    return value

def standardize_gender_f(value):
    #Standardize the values in the gender column
    if type(value) == str:
        if value[0].lower() == "m":
            return "M"
        else:
            return "F"
        
def standardize_state_f(value):
    #Standardize the values in the state column (we want the full name with title case)
    if type(value) == str:
        if value[0].lower() == "a":
            return "Arizona"
        elif value[0].lower() == "c":
            return "California"
        elif value[0].lower() == "w":
            return "Washington"
        else:
            return value.title()
        
def standardize_vehicle_classes_f(value):
    #Merge "Sport Cars", "Luxury SUV" and "Luxury Car" into just "Luxury"
    if type(value) == str:
        if value in ["Sports Car", "Luxury SUV", "Luxury Car"]:
            return "Luxury"
    return value