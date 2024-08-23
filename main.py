import pandas as pd
from data_cleaning import dataset_cleaning, save_cleaned_data

def main():
    url1 = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    url2 = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file2.csv"
    url3 = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file3.csv"
    
    df1 = pd.read_csv(url1)
    df2 = pd.read_csv(url2)
    df3 = pd.read_csv(url3)
    
    df1_clean = dataset_cleaning(df1)
    df2_clean = dataset_cleaning(df2)
    df3_clean = dataset_cleaning(df3)
    
    combined_df = pd.concat([df1_clean, df2_clean, df3_clean], ignore_index=True)
    
    save_cleaned_data(combined_df, 'cleaned_combined_data.csv')

if __name__ == "__main__":
    main()
