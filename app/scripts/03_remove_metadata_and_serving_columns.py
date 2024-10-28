# Filename: remove_metadata_and_serving_columns.py

import pandas as pd
import os

def remove_metadata_and_serving_columns(df):
    """
    Removes unnecessary metadata, image-related, and serving-related columns
    except for 'last_updated_datetime'.

    Args:
    - df (pd.DataFrame): DataFrame from which the columns should be removed.

    Returns:
    - pd.DataFrame: Cleaned DataFrame with specified columns removed.
    """
    # List of columns to remove, leaving 'last_updated_datetime'
    columns_to_remove = [
        'code', 'url', 'creator', 'last_modified_by', 'last_updated_t',
        'image_url', 'image_small_url', 'image_ingredients_url',
        'image_ingredients_small_url', 'image_nutrition_url', 'image_nutrition_small_url',
        'completeness', 'unique_scans_n', 'states', 'serving_size', 'serving_quantity'
    ]
    
    # Remove the columns
    df_cleaned = df.drop(columns=columns_to_remove, errors='ignore')
    print(f"Removed {len(columns_to_remove)} columns from the DataFrame.")
    
    return df_cleaned

def main():
    """
    Main function to execute the removal of specified columns.
    """
    # Define the path to the data directory relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Navigate up to project root
    data_dir = os.path.join(project_root, 'data')
    input_file = os.path.join(data_dir, 'cleaned_df_2.csv')
    output_file = os.path.join(data_dir, 'cleaned_df_3.csv')
    
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
    
    # Load the cleaned_df_2.csv
    try:
        df_cleaned_2 = pd.read_csv(input_file)
        print(f"Data loaded successfully from {input_file}.")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return
    
    # Apply the function to remove specified columns
    df_cleaned_3 = remove_metadata_and_serving_columns(df_cleaned_2)
    
    # Save the cleaned DataFrame to a new CSV file
    try:
        df_cleaned_3.to_csv(output_file, index=False)
        print(f"Cleaned DataFrame saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred while saving the cleaned data: {e}")
        return
    
    print("Column removal process completed successfully.")

if __name__ == "__main__":
    main()
