# Filename: scripts/feature_selection.py

import pandas as pd
import os

def load_data(file_path):
    """
    Loads the cleaned DataFrame from a CSV file.

    Parameters:
        file_path (str): Path to the cleaned CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the path.")
        raise
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        raise

def define_column_lists(df):
    """
    Defines lists of columns to keep, remove, and with doubt.

    Parameters:
        df (pd.DataFrame): The original DataFrame.

    Returns:
        tuple: Three lists containing column names to keep, remove, and with doubt.
    """
    # Define columns to keep
    columns_to_keep = [
        'nutriscore_grade',
        'nutriscore_score',
        'nutrition-score-fr_100g',
        'nova_group',
        'ecoscore_score',
        'energy-kcal_100g',
        'fat_100g',
        'saturated-fat_100g',
        'carbohydrates_100g',
        'sugars_100g',
        'fiber_100g',
        'proteins_100g',
        'salt_100g',
        'sodium_100g',
        'fruits-vegetables-nuts-estimate-from-ingredients_100g',
        'pnns_groups_1',
        'pnns_groups_2',
        'food_groups',
        'main_category'
    ]

    # Define columns to remove
    columns_to_remove = [
        'created_t',
        'created_datetime',
        'last_modified_t',
        'last_modified_datetime',
        'last_updated_datetime',
        'last_image_t',
        'last_image_datetime',
        'product_name',
        'brands',
        'categories',
        'labels',
        'ingredients_text',
        'quantity',
        'energy_100g'
    ]

    # Define columns with doubt
    columns_with_doubt = [
        'ecoscore_score',
        'ecoscore_grade',
        'food_groups'
    ]

    # Verify columns exist in the DataFrame
    existing_keep = [col for col in columns_to_keep if col in df.columns]
    existing_remove = [col for col in columns_to_remove if col in df.columns]
    existing_doubt = [col for col in columns_with_doubt if col in df.columns]

    missing_keep = set(columns_to_keep) - set(existing_keep)
    missing_remove = set(columns_to_remove) - set(existing_remove)
    missing_doubt = set(columns_with_doubt) - set(existing_doubt)

    if missing_keep:
        print(f"Warning: The following 'keep' columns are missing in the DataFrame and will be skipped: {missing_keep}")
    if missing_remove:
        print(f"Warning: The following 'remove' columns are missing in the DataFrame and will be skipped: {missing_remove}")
    if missing_doubt:
        print(f"Warning: The following 'doubt' columns are missing in the DataFrame and will be skipped: {missing_doubt}")

    return existing_keep, existing_remove, existing_doubt

def save_column_lists(keep_cols, remove_cols, doubt_cols, output_dir):
    """
    Saves the column lists as separate CSV files.

    Parameters:
        keep_cols (list): Columns to keep.
        remove_cols (list): Columns to remove.
        doubt_cols (list): Columns with doubt.
        output_dir (str): Directory where CSVs will be saved.
    """
    # Create DataFrames for each list
    df_keep = pd.DataFrame({'Columns_to_Keep': keep_cols})
    df_remove = pd.DataFrame({'Columns_to_Remove': remove_cols})
    df_doubt = pd.DataFrame({'Columns_with_Doubt': doubt_cols})

    # Define file paths
    keep_path = os.path.join(output_dir, 'columns_to_keep.csv')
    remove_path = os.path.join(output_dir, 'columns_to_remove.csv')
    doubt_path = os.path.join(output_dir, 'columns_with_doubt.csv')

    # Save to CSV
    df_keep.to_csv(keep_path, index=False)
    print(f"Columns to keep saved to {keep_path}.")

    df_remove.to_csv(remove_path, index=False)
    print(f"Columns to remove saved to {remove_path}.")

    df_doubt.to_csv(doubt_path, index=False)
    print(f"Columns with doubt saved to {doubt_path}.")

def save_selected_features(df, keep_cols, output_dir):
    """
    Saves the DataFrame with only the selected columns to a new CSV file.

    Parameters:
        df (pd.DataFrame): The original DataFrame.
        keep_cols (list): Columns to keep.
        output_dir (str): Directory where the CSV will be saved.
    """
    df_selected = df[keep_cols].copy()
    selected_features_path = os.path.join(output_dir, 'selected_features.csv')
    df_selected.to_csv(selected_features_path, index=False)
    print(f"Selected features saved to {selected_features_path}.")

def main():
    """
    Main function to execute feature selection and save column lists.
    """
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, '..', 'data', 'cleaned_df_4.csv')
    output_directory = os.path.join(current_dir, '..', 'data')

    # Load data
    df = load_data(input_file)

    # Define column lists
    keep_cols, remove_cols, doubt_cols = define_column_lists(df)

    # Save column lists as CSVs
    save_column_lists(keep_cols, remove_cols, doubt_cols, output_directory)

    # Save the selected features as a new CSV
    save_selected_features(df, keep_cols, output_directory)

if __name__ == "__main__":
    main()
