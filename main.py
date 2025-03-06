import pandas as pd 

def load_data(file_path):
    return pd.read_csv(file_path)

def inspect_data(df):
    print("Data Head:\n", df.head())
    print("\nData Info:\n", df.info())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nData Description:\n", df.decribe())

def clean_data(df):
    #drop rows with missing values
    df_cleaned = df.dropna()
    df_cleaned = pd.get_dummies(df_cleaned, drop_first=True)
    return df_cleaned

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)

def main():
    file_path = "StudentPerformanceFactors.csv"
    output_path = "StudentPerformanceFactors.csv"

    #load the data 
    df= load_data(file_path)

    #inspect the data 
    inspect_data(df)

    #clean the data
    df_cleaned = clean_data(df)

    #save cleaned data 
    save_clean_data(df_cleaned, output_path)
    print("\nData cleaning complete. Cleaned data saved to:", output_path)

    if __name__ =="__main__":
        main()