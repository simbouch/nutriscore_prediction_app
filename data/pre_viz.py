import pandas as pd
import os
from IPython.display import display

def previsualisation_bouchaib(df, num_rows=5):
    """
    Function to display a clear and structured preview of a DataFrame.
    
    Args:
    - df: The input pandas DataFrame.
    - num_rows: Number of rows to display (default: 5).
    """
    # Show the first few rows of the DataFrame
    print("### Aperçu des premières lignes du DataFrame ###")
    display(df.head(num_rows))
    
    # Show the general information about the DataFrame
    print("### Informations générales sur le DataFrame ###")
    df_info = df.info()  # 'info()' directly prints; can't be displayed as output
    print("\n")

    # Display the shape (rows, columns) of the DataFrame
    print("### Shape du DataFrame (lignes, colonnes) ###")
    display(df.shape)
    
    # Display the column names
    print("### Colonnes du DataFrame ###")
    display(df.columns.tolist())
    
    # Show the data types of the columns
    print("### Types de données des colonnes ###")
    display(df.dtypes)
    
    # Display summary statistics for numerical columns
    print("### Résumé statistique (colonnes numériques) ###")
    display(df.describe())
    
    # Display the number of unique values in each column
    print("### Nombre de valeurs uniques par colonne ###")
    display(df.nunique())
    
    # Display the number of missing values in each column
    print("### Nombre de valeurs manquantes par colonne ###")
    display(df.isnull().sum())
    
    # Display a summary of missing values per row
    print("### Valeurs manquantes par ligne ###")
    display(df.isnull().sum(axis=1).value_counts())


def process_all_chunks_in_folder(folder_path, sep='\t'):
    """
    Loop over all CSV files in a folder and apply the previsualisation function on each.
    
    Args:
    - folder_path: Path to the folder containing CSV chunks.
    - sep: Separator used in the CSV files (default: '\t').
    """
    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # Loop through each file and apply previsualisation_bouchaib
    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f"\nProcessing file: {file}")
        
        # Read the CSV file
        try:
            df = pd.read_csv(file_path, sep=sep, on_bad_lines='skip', low_memory=False)
            # Call the previsualisation function
            previsualisation_bouchaib(df)
        except Exception as e:
            print(f"Error processing file {file}: {e}")

# Example usage:
folder_path = 'C:/data/simplon_dev_ia_projects/flask_projects/big/output_chunks'  # Modify the folder path as needed
process_all_chunks_in_folder(folder_path)
