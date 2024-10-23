import pandas as pd

def visualize_dataframe(df):
    """
    Function to visualize key information about a DataFrame.
    
    Args:
    - df: The DataFrame to be visualized.
    """
    # Display general information about the DataFrame
    print("### General Information about the DataFrame ###")
    print(df.info())
    
    # Display the first few rows of the DataFrame
    print("\n### First 5 Rows of the DataFrame ###")
    print(df.head())
    
    # Display summary statistics for numerical columns
    print("\n### Summary Statistics for Numerical Columns ###")
    print(df.describe())
    
    # Display the data types of each column
    print("\n### Data Types of Each Column ###")
    print(df.dtypes)
    
    # Display unique values in each column
    print("\n### Unique Values in Each Column ###")
    for column in df.columns:
        print(f"Unique values in '{column}': {df[column].unique()[:5]}")  # Show only the first 5 unique values
    
    # Display the number of missing values in each column
    print("\n### Missing Values in Each Column ###")
    print(df.isnull().sum())

def load_and_visualize_csv(file_path):
    """
    Function to load a CSV file and visualize the DataFrame.
    
    Args:
    - file_path: Path to the CSV file.
    """
    # Load the DataFrame from the CSV
    df = pd.read_csv(file_path)
    
    # Call the visualization function
    visualize_dataframe(df)

# Example usage:
file_path = "C:/data/simplon_dev_ia_projects/flask_projects/df_keep.csv"
load_and_visualize_csv(file_path)


