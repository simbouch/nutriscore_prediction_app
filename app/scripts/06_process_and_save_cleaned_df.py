# Filename: process_and_save_cleaned_df.py

import pandas as pd
import numpy as np
import os

def process_and_save_cleaned_df(input_file, output_file):
    """
    Process the cleaned DataFrame by performing additional cleaning steps and saving it to a new CSV.
    
    Args:
    - input_file (str): Path to the cleaned CSV file (cleaned_df.csv).
    - output_file (str): Path to save the newly cleaned CSV file (cleaned_df_2.csv).
    
    Returns:
    - pd.DataFrame: The DataFrame after the second cleaning process.
    """
    try:
        # Load the CSV with low_memory=False to suppress dtype warnings
        df = pd.read_csv(input_file, low_memory=False)
        print(f"Data loaded successfully from {input_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the path.")
        return
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return
    
    # Step 1: Drop columns with more than 70% missing values
    threshold = len(df) * 0.3  # Keep columns with at least 30% non-null values
    initial_columns = df.shape[1]
    df_cleaned_2 = df.dropna(axis=1, thresh=threshold)
    removed_columns_step1 = initial_columns - df_cleaned_2.shape[1]
    print(f"Step 1: Dropped {removed_columns_step1} columns with more than 70% missing values.")
    
    # Step 2: Drop rows where all nutrient columns are NaN
    nutrient_columns = [
        'energy-kcal_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g',
        'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g'
    ]
    # Check if nutrient columns exist in the DataFrame
    existing_nutrient_columns = [col for col in nutrient_columns if col in df_cleaned_2.columns]
    df_cleaned_2 = df_cleaned_2.dropna(subset=existing_nutrient_columns, how='all')
    print(f"Step 2: Dropped rows where all nutrient columns {existing_nutrient_columns} are NaN.")
    
    # Step 3: Remove duplicates based on 'brands' and 'product_name'
    if 'brands' in df_cleaned_2.columns and 'product_name' in df_cleaned_2.columns:
        before_duplicates = df_cleaned_2.shape[0]
        df_cleaned_2 = df_cleaned_2.drop_duplicates(subset=['brands', 'product_name'])
        after_duplicates = df_cleaned_2.shape[0]
        duplicates_removed = before_duplicates - after_duplicates
        print(f"Step 3: Removed {duplicates_removed} duplicate rows based on 'brands' and 'product_name'.")
    else:
        print("Step 3: Columns 'brands' and/or 'product_name' not found. Skipping duplicate removal.")
    
    # Step 4: Remove redundant columns that end with '_tags' or '_en'
    redundant_columns = [col for col in df_cleaned_2.columns if col.endswith('_tags') or col.endswith('_en')]
    df_cleaned_2 = df_cleaned_2.drop(columns=redundant_columns, errors='ignore')
    print(f"Step 4: Removed {len(redundant_columns)} redundant columns ending with '_tags' or '_en'.")
    
    try:
        # Save the cleaned DataFrame to a new CSV file
        df_cleaned_2.to_csv(output_file, index=False)
        print(f"Cleaned DataFrame saved successfully to {output_file}.")
    except Exception as e:
        print(f"An error occurred while saving the cleaned data: {e}")
        return
    
    return df_cleaned_2

def main():
    """
    Main function to execute the DataFrame processing and saving.
    """
    # Define the path to the data directory relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Navigate up to project root
    data_dir = os.path.join(project_root, 'data')
    
    # Define input and output file paths
    input_file = os.path.join(data_dir, 'cleaned_df.csv')
    output_file = os.path.join(data_dir, 'cleaned_df_2.csv')
    
    # Debugging: Print the calculated paths
    print(f"Current Directory: {current_dir}")
    print(f"Project Root: {project_root}")
    print(f"Data Directory: {data_dir}")
    print(f"Input File Path: {input_file}")
    print(f"Output File Path: {output_file}")
    
    # Check if the data directory exists
    if not os.path.isdir(data_dir):
        print(f"Error: The data directory '{data_dir}' does not exist.")
        return
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The input file '{input_file}' does not exist. Please check the path.")
        return
    
    # Process and save the second cleaned DataFrame
    df_cleaned_2 = process_and_save_cleaned_df(input_file, output_file)
    
    if df_cleaned_2 is not None:
        print("DataFrame processing completed successfully.")
        print(f"Second Cleaned DataFrame Shape: {df_cleaned_2.shape}")
        print("Preview of the Second Cleaned DataFrame:")
        print(df_cleaned_2.head())
    else:
        print("DataFrame processing failed.")

if __name__ == "__main__":
    main()
