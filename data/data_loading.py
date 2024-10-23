import pandas as pd

def chunk_large_csv(input_file, output_folder, chunk_size=50000):
    """
    Reads a large CSV file in chunks and saves each chunk into separate CSV files.
    Skips any bad lines that have inconsistent field counts using `on_bad_lines='skip'`.
    
    Parameters:
    - input_file: Path to the large CSV file.  
    - output_folder: Folder where the chunked CSV files will be saved.
    - chunk_size: Number of rows per chunk (default is 50,000 rows).
    """
    chunk_iter = pd.read_csv(input_file, chunksize=chunk_size, on_bad_lines='skip', sep='\t', low_memory=False)
    
    for i, chunk in enumerate(chunk_iter):
        output_file = f"{output_folder}/chunk_{i + 1}.csv"
        chunk.to_csv(output_file, index=False, sep='\t')
        print(f"Chunk {i + 1} saved to {output_file}")
    
    print("All chunks have been saved.")

# Example usage
input_file = "C:/data/simplon_dev_ia_projects/flask_projects/big/big.csv"
output_folder = "C:/data/simplon_dev_ia_projects/flask_projects/big/output_chunks"
chunk_large_csv(input_file, output_folder, chunk_size=50000)
