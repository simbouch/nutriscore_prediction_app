# Filename: process_and_clean_csv_chunks.py

import pandas as pd
import os
import numpy as np

def process_and_clean_csv_chunks(input_folder, output_file, nan_threshold=0.3):
    """
    Loops through all CSV chunks in the input folder, cleans the data according to the following steps:
    - Cleans 'nutriscore_grade' by replacing 'unknown' and invalid values with NaN
    - Removes rows where all nutrient-related columns are NaN
    - Removes duplicates based on 'brands' and 'product_name'
    - Removes redundant columns (those ending with '_tags', '_en')
    - Removes columns with more than a specified percentage of NaN values (default: 70%) after concatenating the chunks.

    Args:
    - input_folder (str): Folder where the chunked CSV files are saved.
    - output_file (str): Path to save the cleaned DataFrame.
    - nan_threshold (float): Proportion of NaN values in columns (default is 70%, meaning 0.3 threshold).

    Returns:
    - cleaned_df (pd.DataFrame): A DataFrame containing the cleaned data.
    """
    # List to store data from each chunk
    chunks_list = []

    # Loop through all CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            print(f"Processing {file_name}")
            
            # Step 1: Read the chunk without removing any columns
            try:
                chunk = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', low_memory=False)
                print(f"Loaded {file_name} successfully.")
            except Exception as e:
                print(f"Failed to load {file_name}: {e}")
                continue
            
            # Step 2: Replace 'unknown' and 'not-applicable' in nutriscore_grade with NaN
            if 'nutriscore_grade' in chunk.columns:
                chunk['nutriscore_grade'].replace(['unknown', 'not-applicable'], np.nan, inplace=True)
                print(f"Replaced 'unknown' and 'not-applicable' in 'nutriscore_grade' for {file_name}.")
            else:
                print(f"'nutriscore_grade' column not found in {file_name}. Skipping replacement.")
            
            # Step 3: Filter rows with valid Nutri-Score grade (a, b, c, d, or e)
            valid_grades = ['a', 'b', 'c', 'd', 'e']
            if 'nutriscore_grade' in chunk.columns:
                initial_rows = chunk.shape[0]
                chunk = chunk[chunk['nutriscore_grade'].isin(valid_grades)]
                filtered_rows = initial_rows - chunk.shape[0]
                print(f"Filtered {filtered_rows} rows with invalid 'nutriscore_grade' in {file_name}.")
            else:
                print(f"'nutriscore_grade' column not present in {file_name}. Skipping grade filtering.")
            
            # Step 4: Remove rows where all nutrient-related columns are NaN (those ending in '_100g')
            nutrient_columns = [col for col in chunk.columns if col.endswith('_100g')]
            if nutrient_columns:
                initial_rows = chunk.shape[0]
                chunk_cleaned = chunk.dropna(subset=nutrient_columns, how='all')
                removed_rows = initial_rows - chunk_cleaned.shape[0]
                print(f"Dropped {removed_rows} rows with all nutrient columns NaN in {file_name}.")
            else:
                print(f"No nutrient columns found in {file_name}. Skipping row removal.")
                chunk_cleaned = chunk.copy()
            
            # Step 5: Remove duplicates based on 'brands' and 'product_name'
            if 'brands' in chunk_cleaned.columns and 'product_name' in chunk_cleaned.columns:
                before_duplicates = chunk_cleaned.shape[0]
                chunk_cleaned = chunk_cleaned.drop_duplicates(subset=['brands', 'product_name'])
                after_duplicates = chunk_cleaned.shape[0]
                duplicates_removed = before_duplicates - after_duplicates
                print(f"Removed {duplicates_removed} duplicate rows based on 'brands' and 'product_name' in {file_name}.")
            else:
                print(f"'brands' and/or 'product_name' columns not found in {file_name}. Skipping duplicate removal.")
            
            # Step 6: Remove redundant columns (those ending with '_tags' or '_en')
            redundant_columns = [col for col in chunk_cleaned.columns if col.endswith('_tags') or col.endswith('_en')]
            if redundant_columns:
                chunk_cleaned = chunk_cleaned.drop(columns=redundant_columns, errors='ignore')
                print(f"Removed {len(redundant_columns)} redundant columns from {file_name}.")
            else:
                print(f"No redundant columns to remove in {file_name}.")
            
            # Append the cleaned chunk to the list if it's not empty
            if not chunk_cleaned.empty:
                chunks_list.append(chunk_cleaned)
                print(f"Appended cleaned data from {file_name} to chunks list.")
            else:
                print(f"No data to append from {file_name} after cleaning.")
    
    # Concatenate all cleaned chunks into a single DataFrame
    if chunks_list:
        try:
            cleaned_df = pd.concat(chunks_list, ignore_index=True)
            print(f"Concatenated {len(chunks_list)} chunks successfully.")
        except Exception as e:
            print(f"Failed to concatenate chunks: {e}")
            cleaned_df = pd.DataFrame()
    else:
        cleaned_df = pd.DataFrame()  # Return empty DataFrame if no valid data
        print("No valid data found to concatenate.")
    
    # Step 7: Remove columns with more than specified proportion of NaN values after concatenating the chunks
    if not cleaned_df.empty:
        col_threshold = len(cleaned_df) * nan_threshold
        initial_columns = cleaned_df.shape[1]
        cleaned_df = cleaned_df.dropna(axis=1, thresh=col_threshold)
        removed_columns = initial_columns - cleaned_df.shape[1]
        print(f"Removed {removed_columns} columns with more than {nan_threshold*100}% NaN values.")
    else:
        print("Cleaned DataFrame is empty. Skipping column removal based on NaN threshold.")
    
    # Save the cleaned DataFrame to a CSV file with a unique name to avoid conflicts
    if not cleaned_df.empty:
        try:
            cleaned_df.to_csv(output_file, index=False)
            print(f"Cleaned DataFrame saved to {output_file}.")
        except PermissionError:
            # If permission error occurs, save to a different file
            alt_output_file = output_file.replace(".csv", "_backup.csv")
            try:
                cleaned_df.to_csv(alt_output_file, index=False)
                print(f"PermissionError occurred. DataFrame saved to {alt_output_file}.")
            except Exception as e:
                print(f"Failed to save to backup file '{alt_output_file}': {e}")
        except Exception as e:
            print(f"An error occurred while saving the cleaned data: {e}")
    else:
        print("No data available to save.")
    
    return cleaned_df

def main():
    """
    Main function to execute the CSV chunks processing and cleaning.
    """
    # Define the path to the data directory relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Navigate up to project root
    data_dir = os.path.join(project_root, 'data')
    
    # Define input and output file paths
    input_folder = os.path.join(data_dir, 'big', 'output_chunks')
    output_file = os.path.join(data_dir, 'cleaned_df.csv')
    
    # Debugging: Print the calculated paths
    print(f"Current Directory: {current_dir}")
    print(f"Project Root: {project_root}")
    print(f"Data Directory: {data_dir}")
    print(f"Input Folder Path: {input_folder}")
    print(f"Output File Path: {output_file}")
    
    # Check if the data directory exists
    if not os.path.isdir(data_dir):
        print(f"Error: The data directory '{data_dir}' does not exist.")
        return
    
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist. Please check the path.")
        return
    
    # Process the chunks, clean the data, and get the final cleaned DataFrame
    cleaned_df = process_and_clean_csv_chunks(input_folder, output_file)
    
    if not cleaned_df.empty:
        print("DataFrame processing completed successfully.")
        print(f"Cleaned DataFrame Shape: {cleaned_df.shape}")
        print("Preview of the Cleaned DataFrame:")
        print(cleaned_df.head())
    else:
        print("DataFrame processing resulted in an empty DataFrame.")

if __name__ == "__main__":
    main()
