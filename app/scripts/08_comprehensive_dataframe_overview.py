# Filename: comprehensive_dataframe_overview.py

import pandas as pd
from IPython.display import display
import os

def comprehensive_dataframe_overview(df):
    """
    Provides a comprehensive overview of the given DataFrame, including:
    - First 5 rows (head)
    - Last 5 rows (tail)
    - General info
    - Missing values per column (count and percentage)
    - Summary statistics for numerical columns
    - Unique values in each column
    - Data types of each column
    """

    print("### First 5 Rows of the DataFrame ###")
    display(df.head())
    
    print("\n### Last 5 Rows of the DataFrame ###")
    display(df.tail())
    
    print("\n### General Information about the DataFrame ###")
    df_info = df.info()
    print(df_info)
    
    print("\n### Summary Statistics for Numerical Columns ###")
    summary_stats = df.describe()
    print(summary_stats)
    
    print("\n### Missing Values in Each Column ###")
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    missing_summary = pd.DataFrame({
        'Missing Count': missing_values,
        'Missing Percentage': missing_percentage
    })
    print(missing_summary)
    
    print("\n### Data Types of Each Column ###")
    print(df.dtypes)
    
    print("\n### Unique Values in Each Column ###")
    for col in df.columns:
        unique_vals = df[col].unique()
        unique_count = df[col].nunique()
        display_count = min(len(unique_vals), 5)
        print(f"Unique values in '{col}' (showing up to 5): {unique_vals[:display_count]}")
        print(f"Total unique values in '{col}': {unique_count}\n")

def main():
    """
    Main function to load the DataFrame and run the comprehensive overview.
    """
    # Define the path to the cleaned CSV file relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, '..', '..', 'data')
    file_path = os.path.join(data_dir, 'cleaned_df_4.csv')
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please check the path.")
        return
    
    # Load the cleaned CSV
    try:
        cleaned_df_4 = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return
    
    # Run the comprehensive overview function on cleaned_df_4
    comprehensive_dataframe_overview(cleaned_df_4)

if __name__ == "__main__":
    main()
