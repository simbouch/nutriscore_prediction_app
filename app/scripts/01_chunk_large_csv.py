# Filename: chunk_large_csv.py

import pandas as pd
import os

def chunk_large_csv(input_file, output_folder, chunk_size=50000, sep='\t'):
    """
    Reads a large CSV file in chunks and saves each chunk into separate CSV files.
    Skips any bad lines that have inconsistent field counts using `on_bad_lines='skip'`.
    
    Parameters:
    - input_file (str): Path to the large CSV file.
    - output_folder (str): Folder where the chunked CSV files will be saved.
    - chunk_size (int): Number of rows per chunk (default is 50,000 rows).
    - sep (str): Separator used in the CSV files (default is tab '\t').
    
    Returns:
    - None
    """
    # Ensure the output folder exists; create it if it doesn't
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
            print(f"Created output folder at: {output_folder}")
        except Exception as e:
            print(f"Failed to create output folder '{output_folder}': {e}")
            return
    
    # Attempt to read and chunk the CSV file
    try:
        chunk_iter = pd.read_csv(
            input_file,
            chunksize=chunk_size,
            on_bad_lines='skip',
            sep=sep,
            low_memory=False
        )
        print(f"Started processing '{input_file}' in chunks of {chunk_size} rows.")
    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist. Please check the path.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The input file '{input_file}' is empty.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading '{input_file}': {e}")
        return
    
    # Process each chunk
    chunk_count = 0
    for i, chunk in enumerate(chunk_iter):
        chunk_count += 1
        output_file = os.path.join(output_folder, f"chunk_{i + 1}.csv")
        try:
            chunk.to_csv(output_file, index=False, sep=sep)
            print(f"Chunk {i + 1} saved to {output_file}")
        except PermissionError:
            # If permission error occurs, save to a different file
            alt_output_file = output_file.replace(".csv", "_backup.csv")
            try:
                chunk.to_csv(alt_output_file, index=False, sep=sep)
                print(f"PermissionError: Chunk {i + 1} saved to {alt_output_file} instead.")
            except Exception as e:
                print(f"Failed to save chunk {i + 1} to both '{output_file}' and '{alt_output_file}': {e}")
        except Exception as e:
            print(f"An error occurred while saving chunk {i + 1} to '{output_file}': {e}")
    
    print(f"All chunks have been processed and saved. Total chunks created: {chunk_count}")


def main():
    """
    Main function to execute the chunking of a large CSV file.
    """
    # Define the path to the data directory relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Navigate up to project root
    data_dir = os.path.join(project_root, 'data')
    
    # Define input and output file paths
    input_file = os.path.join(data_dir, 'big', 'big.csv')
    output_folder = os.path.join(data_dir, 'big', 'output_chunks')
    
    # Define chunk size and separator
    chunk_size = 50000  # Modify if you want a different chunk size
    sep = '\t'  # Modify if your CSVs use a different separator (e.g., ',' for CSV)
    
    # Debugging: Print the calculated paths
    print(f"Current Directory: {current_dir}")
    print(f"Project Root: {project_root}")
    print(f"Data Directory: {data_dir}")
    print(f"Input File Path: {input_file}")
    print(f"Output Folder Path: {output_folder}")
    print(f"Chunk Size: {chunk_size}")
    print(f"Separator Used: '{sep}'")
    
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The input file '{input_file}' does not exist. Please check the path.")
        return
    
    # Execute the chunking process
    chunk_large_csv(input_file, output_folder, chunk_size=chunk_size, sep=sep)


if __name__ == "__main__":
    main()
