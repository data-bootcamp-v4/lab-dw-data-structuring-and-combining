def clean_data(data):
    import pandas as pd
    import numpy as np
    data = data.rename(columns = {'ST':'State'})
    data.columns = data.columns.str.replace(' ','_').str.lower()
    data.gender = data.gender.replace('Femal','F').replace('female','F').replace('Male','M')
    data.state = data.state.replace('AZ','Arizona').replace('Cali','California').replace('WA','Washington')
    data.education = data.education.replace('Bachelors','Bachelor')
    data.customer_lifetime_value = data.customer_lifetime_value.replace('%','',regex=True) #the replace looks for the whole str without regex true"
    data.customer_lifetime_value = data.customer_lifetime_value.astype(float)  
    data.vehicle_class = data.vehicle_class.replace(['Luxury SUV','Sports Car','Luxury Car'],'Luxury')
    data.customer_lifetime_value = data.customer_lifetime_value.astype(float)
    data.number_of_open_complaints = data.number_of_open_complaints.replace(['1/','/00'],'',regex=True).replace('00','0')
    data.number_of_open_complaints = pd.to_numeric(data.number_of_open_complaints,errors = 'coerce').astype('Int64')
    data = data.dropna(how='all')
    data.isnull().sum()
    data.customer_lifetime_value = data.customer_lifetime_value.fillna(data.customer_lifetime_value.mean())
    data.customer_lifetime_value.isnull().sum()
    data.gender = data.gender.fillna('Unknown')
    for column in data.select_dtypes(include = 'float').columns:
        data[column]= data[column].astype(int)
    data.compare = data.iloc[:, 1]==data.iloc[:, 11]
    data.compare
    false_rows = data.loc[data.compare == False]
    data[data.compare == False][['state']].reset_index(drop=True)
    data.iloc[:, 1] = data.iloc[:, 1].fillna(data.iloc[:, 11])
    data.columns.tolist()
    data = data.drop(data.columns[11], axis=1)
    data = data.drop(data.columns[-1], axis=1)

    return data