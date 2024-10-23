import pandas as pd

# Load the cleaned CSV with low_memory=False to avoid mixed types issues
file_path = "C:/data/simplon_dev_ia_projects/flask_projects/cleaned_df.csv"
df = pd.read_csv(file_path, low_memory=False)

# List of columns to keep for Nutri-Score classification
columns_to_keep = [
    'nutriscore_score',       # Nutri-Score (numeric score)
    'nutriscore_grade',       # Nutri-Score grade (A, B, C, D, E)
    'nova_group',             # Degree of processing
    'energy-kcal_100g',       # Energy (calories)
    'fat_100g',               # Total fat
    'saturated-fat_100g',     # Saturated fat
    'monounsaturated-fat_100g',  # Monounsaturated fat
    'polyunsaturated-fat_100g',  # Polyunsaturated fat
    'trans-fat_100g',         # Trans fat
    'cholesterol_100g',       # Cholesterol
    'carbohydrates_100g',     # Carbohydrates
    'sugars_100g',            # Sugars
    'fiber_100g',             # Fiber
    'proteins_100g',          # Proteins
    'salt_100g',              # Salt
    'sodium_100g',            # Sodium
    'vitamin-a_100g',         # Vitamin A
    'vitamin-c_100g',         # Vitamin C
    'potassium_100g',         # Potassium
    'calcium_100g',           # Calcium
    'iron_100g',              # Iron
]

# List of columns to remove (metadata or irrelevant to classification)
columns_to_remove = [
    'code', 'url', 'creator', 'created_t', 'created_datetime',
    'last_modified_t', 'last_modified_datetime', 'last_modified_by',
    'last_updated_t', 'last_updated_datetime', 'product_name', 'brands',
    'brands_tags', 'categories', 'categories_tags', 'categories_en', 'labels',
    'labels_tags', 'labels_en', 'stores', 'countries', 'countries_tags', 
    'countries_en', 'ingredients_text', 'ingredients_tags', 
    'ingredients_analysis_tags', 'allergens', 'serving_size', 
    'serving_quantity', 'additives_n', 'additives_tags', 'additives_en',
    'ecoscore_score', 'ecoscore_grade', 'unique_scans_n', 'popularity_tags',
    'completeness', 'last_image_t', 'last_image_datetime', 'image_url',
    'image_small_url', 'image_nutrition_url', 'image_nutrition_small_url',
    'quantity', 'packaging', 'packaging_tags', 'packaging_en', 'product_quantity',
    'image_ingredients_url', 'image_ingredients_small_url', 'emb_codes', 
    'emb_codes_tags', 'first_packaging_code_geo', 'cities_tags',
    'generic_name', 'origins', 'origins_tags', 'origins_en', 'manufacturing_places',
    'manufacturing_places_tags', 'purchase_places', 'traces', 'traces_tags', 
    'traces_en', 'owner', 'abbreviated_product_name', 'alcohol_100g', 
    'fruits-vegetables-nuts_100g'
]

# List of columns with doubt (could be useful, need to be analyzed further)
columns_with_doubt = [
    'pnns_groups_1',          # General food category
    'pnns_groups_2',          # Specific food category
    'food_groups',            # Food groups
    'food_groups_tags',       # Food group tags
    'food_groups_en',         # Food group names in English
    'states',                 # States (product's lifecycle status)
    'states_tags',            # Tags for states
    'states_en',              # States in English
]

# DataFrames for each category
df_keep = df[columns_to_keep]
df_remove = df[columns_to_remove]
df_doubt = df[columns_with_doubt]

# Save each DataFrame to a CSV file
df_keep.to_csv("C:/data/simplon_dev_ia_projects/flask_projects/df_keep.csv", index=False)
df_remove.to_csv("C:/data/simplon_dev_ia_projects/flask_projects/df_remove.csv", index=False)
df_doubt.to_csv("C:/data/simplon_dev_ia_projects/flask_projects/df_doubt.csv", index=False)

# Print confirmation
print(f"DataFrames saved: df_keep.csv, df_remove.csv, df_doubt.csv")
