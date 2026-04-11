import pandas as pd
import numpy as np

def clean_column_values(df):
    """
    Cleans Customer Lifetime Value and Number of Open Complaints.
    Uses 'coerce' and string forcing to prevent Mixed Type errors.
    """
    # 1. Clean Customer Lifetime Value
    if 'customer_lifetime_value' in df.columns:
        # Convert to string first to ensure .replace works on all rows
        df['customer_lifetime_value'] = (
            df['customer_lifetime_value']
            .astype(str)
            .str.replace('%', '', regex=False)
            .replace(['nan', 'None', 'null'], np.nan)
        )
        # Safely convert to float; invalid values become NaN instead of crashing
        df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')

    # 2. Clean Number of Open Complaints
    if 'number_of_open_complaints' in df.columns:
        # Step A: Force everything to string to prevent 'str' vs 'int' errors
        temp_series = df['number_of_open_complaints'].astype(str)
        
        # Step B: Extract the middle value if a '/' exists
        def extract_middle(val):
            if '/' in val:
                try:
                    return val.split('/')[1]
                except (IndexError, AttributeError):
                    return val
            return val

        df['number_of_open_complaints'] = temp_series.apply(extract_middle)
        
        # Step C: Remove dots and convert to numeric
        df['number_of_open_complaints'] = (
            df['number_of_open_complaints']
            .str.replace('.', '', regex=False)
            .replace(['nan', 'None', 'null'], np.nan)
        )
        df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce')
        
    return df

def clean_categorical_data(df):
    """
    Vereinheitlicht Kategorien für Gender, State und Vehicle Class.
    """
    # 1. Definition der Mapping-Dicts
    # Tipp: Wir können hier direkt alle Varianten abfangen
    gender_map = {
        "F": "F", "Femal": "F", "female": "F", "Female": "F",
        "M": "M", "Male": "M", "male": "M"
    }
    
    state_map = {
        "Cali": "California", 
        "AZ": "Arizona", 
        "WA": "Washington"
    }
    
    vehicle_map = {
        "Luxury SUV": "Luxury", 
        "Sports Car": "Luxury", 
        "Luxury Car": "Luxury"
    }
    
    # 2. Anwendung der Mappings
    # Wir nutzen .replace(), damit Werte, die nicht im Dict stehen, 
    # unverändert bleiben (z.B. "California" bleibt "California").
    df['gender'] = df['gender'].replace(gender_map)
    df['state'] = df['state'].replace(state_map)
    df['vehicle_class'] = df['vehicle_class'].replace(vehicle_map)
    
    return df

def handle_nulls(df):
    """
    Füllt numerische Nullwerte mit dem Median und kategorische mit dem Modalwert.
    Verwendet sicherere Methoden, um KeyErrors zu vermeiden.
    """
    # 1. Numerische Spalten: Median
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        # median() gibt NaN zurück, wenn die Spalte leer ist, 
        # fillna() macht dann einfach nichts – das ist sicher.
        median_val = df[col].median()
        if pd.notna(median_val):
            df[col] = df[col].fillna(median_val)
        
    # 2. Kategorische Spalten: Mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        mode_series = df[col].mode()
        
        if not mode_series.empty:
            # Wir extrahieren den ersten Wert sicher mit .iloc[0]
            df[col] = df[col].fillna(mode_series.iloc[0])
        else:
            # Fallback, wenn die Spalte komplett leer/NaN ist
            df[col] = df[col].fillna("Unknown")
            
    return df

def remove_duplicates(df):
    """Removes exact duplicate rows and resets the index."""
    return df.drop_duplicates(keep='first').reset_index(drop=True)

def format_types(df):
    """Final cast of numeric variables to integers."""
    num_cols = df.select_dtypes(include=['number']).columns
    # Use fillna(0) before cast because you can't have an 'int' NaN
    df[num_cols] = df[num_cols].fillna(0).astype(int)
    return df