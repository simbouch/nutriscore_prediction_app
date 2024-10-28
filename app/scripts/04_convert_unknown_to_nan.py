# Filename: convert_unknown_to_nan.py

import pandas as pd
import numpy as np
import os

def convert_unknown_to_nan(input_file, output_file):
    """
    Converts 'unknown' values to NaN in the DataFrame and saves the cleaned DataFrame.

    Args:
    - input_file (str): Path to the input CSV file (cleaned_df_3.csv).
    - output_file (str): Path to save the cleaned CSV file (cleaned_df_4.csv).

    Returns:
    - df_cleaned_4 (pd.DataFrame): DataFrame with 'unknown' values replaced by NaN.
    """
    try:
        # Load the DataFrame
        df_cleaned_3 = pd.read_csv(input_file)
        print(f"Data loaded successfully from {input_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the path.")
        return
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return

    # Replace 'unknown' with NaN
    df_cleaned_4 = df_cleaned_3.replace('unknown', np.nan)
    print("Replaced 'unknown' values with NaN.")

    try:
        # Save the cleaned DataFrame
        df_cleaned_4.to_csv(output_file, index=False)
        print(f"Cleaned DataFrame saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred while saving the cleaned data: {e}")
        return

    return df_cleaned_4

def main():
    """
    Main function to execute the conversion of 'unknown' to NaN.
    """
    # Define the path to the data directory relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Navigate up to project root
    data_dir = os.path.join(project_root, 'data')

    # Define input and output file paths
    input_file = os.path.join(data_dir, 'cleaned_df_3.csv')
    output_file = os.path.join(data_dir, 'cleaned_df_4.csv')

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

    # Perform the conversion
    df_cleaned_4 = convert_unknown_to_nan(input_file, output_file)

    if df_cleaned_4 is not None:
        print("Conversion completed successfully.")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    main()
