import pandas as pd
import re

df_list = []
df_combined = pd.DataFrame()

for i in range(348):
    df = pd.read_csv(f'CSV/openfoodfacts_{i}.csv', sep=',', header=0)

    # First duplicates delete
    df_cleaned = df.drop_duplicates(keep = 'first', inplace = False)
    
    # Cleaning nutriscore_grade
    index_ng = df.columns.get_loc('nutriscore_grade')

    for j in range(df_cleaned.shape[0]):
        if df_cleaned.iloc[j, index_ng] not in ["a", "b", "c", "d", "e"]:
            df_cleaned.iloc[j, index_ng] = None

    df_cleaned.dropna(subset=['nutriscore_grade'], axis=0, how='any', inplace= True)

    # Delete columns with at least 70% NaN
    percentage = 0.70

    threshold = int((1 - percentage) * df_cleaned.shape[0])

    df_cleaned.dropna(thresh=threshold, inplace= True, axis=1)

    # Delete rows with empty nutrients
    columns_100g = [col for col in df_cleaned.columns if '_100g' in col]

    df_cleaned = df_cleaned[~df_cleaned[columns_100g].isna().all(axis=1)]

    # Delete duplicates on 'brands' and 'product_name'
    df_cleaned.drop_duplicates(subset=['brands', 'product_name'], keep = 'first', inplace=True)

    print(df_cleaned.info())

    print(df_cleaned.shape)

    df_list.append(df_cleaned)

df_combined = pd.concat(df_list, ignore_index=True)

df_combined.to_csv(f'cleaned_csv/openfoodfacts_cleaned.csv', index=False)
