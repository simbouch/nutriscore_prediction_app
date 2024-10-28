import pandas as pd
import os

def previsualisation(df, num_rows=5):
    """
    Function to display a clear and structured preview of a DataFrame.
    
    Args:
    - df (pd.DataFrame): The input pandas DataFrame.
    - num_rows (int): Number of rows to display (default: 5).
    """
    # Show the first few rows of the DataFrame
    print("### Aperçu des premières lignes du DataFrame ###")
    print(df.head(num_rows))
    
    # Show the general information about the DataFrame
    print("\n### Informations générales sur le DataFrame ###")
    df_info = df.info()
    print("\n")
    
    # Display the shape (rows, columns) of the DataFrame
    print("### Shape du DataFrame (lignes, colonnes) ###")
    print(df.shape)
    
    # Display the column names
    print("\n### Colonnes du DataFrame ###")
    print(df.columns.tolist())
    
    # Show the data types of the columns
    print("\n### Types de données des colonnes ###")
    print(df.dtypes)
    
    # Display summary statistics for numerical columns
    print("\n### Résumé statistique (colonnes numériques) ###")
    print(df.describe())
    
    # Display the number of unique values in each column
    print("\n### Nombre de valeurs uniques par colonne ###")
    print(df.nunique())
    
    # Display the number of missing values in each column
    print("\n### Nombre de valeurs manquantes par colonne ###")
    print(df.isnull().sum())
    
    # Display a summary of missing values per row
    print("\n### Valeurs manquantes par ligne ###")
    print(df.isnull().sum(axis=1).value_counts())


def process_all_chunks_in_folder(folder_path, sep='\t'):
    """
    Loop over all CSV files in a folder and apply the previsualisation function on each.
    
    Args:
    - folder_path (str): Path to the folder containing CSV chunks.
    - sep (str): Separator used in the CSV files (default: '\t').
    """
    # List all CSV files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    if not files:
        print(f"No CSV files found in the folder: {folder_path}")
        return
    
    # Loop through each file and apply previsualisation
    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f"\nProcessing file: {file}")
        
        # Read the CSV file
        try:
            df = pd.read_csv(file_path, sep=sep, on_bad_lines='skip', low_memory=False)
            # Call the previsualisation function
            previsualisation(df)
        except Exception as e:
            print(f"Error processing file {file}: {e}")


def main():
    """
    Main function to execute the previsualisation on all CSV chunks in a specified folder.
    """
    # Define the path to the data directory relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Navigate up to project root
    data_dir = os.path.join(project_root, 'data')
    input_folder = os.path.join(data_dir, 'big', 'output_chunks')
    
    # Define separator
    sep = '\t'  # Modify if your CSVs use a different separator
    
    # Debugging: Print the calculated paths
    print(f"Current Directory: {current_dir}")
    print(f"Project Root: {project_root}")
    print(f"Data Directory: {data_dir}")
    print(f"Input Folder Path: {input_folder}")
    print(f"Separator Used: '{sep}'")
    
    # Check if the data directory exists
    if not os.path.isdir(data_dir):
        print(f"Error: The data directory '{data_dir}' does not exist.")
        return
    
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist. Please check the path.")
        return
    
    # Process all chunks in the input folder
    process_all_chunks_in_folder(input_folder, sep=sep)


if __name__ == "__main__":
    main()
