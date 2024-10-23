import pandas as pd
import os
import numpy as np

def process_and_clean_csv_chunks(input_folder, output_file):
    """
    Loops through all CSV chunks in the input folder, filters rows based on the 'nutriscore_grade',
    replaces 'unknown' with NaN, removes columns with more than 90% NaN values, 
    and removes rows that don't have valid Nutri-Score grades ('a', 'b', 'c', 'd', 'e').
    
    Args:
    - input_folder: Folder where the chunked CSV files are saved.
    - output_file: Path to save the cleaned DataFrame.
    
    Returns:
    - cleaned_df: A DataFrame containing the cleaned data.
    """
    # List to store data from each chunk
    chunks_list = []

    # Loop through all CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            print(f"Processing {file_name}")
            
            # Read the chunk without removing any columns
            chunk = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', low_memory=False)
            
            # Replace 'unknown' with NaN
            chunk.replace('unknown', np.nan, inplace=True)
            
            # Filter rows with valid Nutri-Score grade (a, b, c, d, or e)
            valid_grades = ['a', 'b', 'c', 'd', 'e']
            chunk = chunk[chunk['nutriscore_grade'].isin(valid_grades)]
            
            # Remove columns with more than 90% NaN values
            threshold = len(chunk) * 0.1  # Remove columns with more than 90% NaN values
            chunk_cleaned = chunk.dropna(axis=1, thresh=threshold)
            
            # Append the cleaned chunk to the list
            if not chunk_cleaned.empty:
                chunks_list.append(chunk_cleaned)

    # Concatenate all cleaned chunks into a single DataFrame
    if chunks_list:
        cleaned_df = pd.concat(chunks_list, ignore_index=True)
    else:
        cleaned_df = pd.DataFrame()  # Return empty DataFrame if no valid data

    # Save the cleaned DataFrame to a CSV file with a unique name to avoid conflicts
    try:
        cleaned_df.to_csv(output_file, index=False)
        print(f"Cleaned DataFrame saved to {output_file}")
    except PermissionError:
        # If permission error occurs, save to a different file
        alt_output_file = output_file.replace(".csv", "_backup.csv")
        cleaned_df.to_csv(alt_output_file, index=False)
        print(f"PermissionError occurred. DataFrame saved to {alt_output_file}")
    
    return cleaned_df

# Example usage:
input_folder = "C:/data/simplon_dev_ia_projects/flask_projects/big/output_chunks"
output_file = "C:/data/simplon_dev_ia_projects/flask_projects/cleaned_df.csv"

# Process the chunks, clean the data, and get the final cleaned DataFrame
cleaned_df = process_and_clean_csv_chunks(input_folder, output_file)

# Display the resulting cleaned DataFrame
print("Cleaned DataFrame Shape:", cleaned_df.shape)
print("Preview of the Cleaned DataFrame:")
print(cleaned_df.head())
