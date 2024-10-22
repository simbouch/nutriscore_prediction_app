import pandas as pd
import glob

df_list = []
df_combined = pd.DataFrame()

for i in range(348):
    df = pd.read_csv(f'CSV/openfoodfacts_{i}.csv', sep=',', header=0)

    index_ng = df.columns.get_loc('nutriscore_grade')

    df_cleaned = df.drop_duplicates(keep = 'first', inplace = False)
    
    for j in range(df_cleaned.shape[0]):
        if df_cleaned.iloc[j, index_ng] not in ["a", "b", "c", "d", "e"]:
            df_cleaned.iloc[j, index_ng] = None

    df_cleaned.dropna(subset=['nutriscore_grade'], axis=0, how='any', inplace= True)

    percentage = 0.90

    threshold = int(percentage * df_cleaned.shape[1])

    df_cleaned.dropna(thresh=threshold, inplace= True, axis=1)

    print(df_cleaned.info())

    print(df_cleaned.shape)

    df_list.append(df_cleaned)

df_combined = pd.concat(df_list, ignore_index=True)

df_combined.to_csv(f'cleaned_csv/openfoodfacts_cleaned.csv', index=False) 
