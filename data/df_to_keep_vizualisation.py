import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV containing the columns to keep
df_keep = pd.read_csv("C:/data/simplon_dev_ia_projects/flask_projects/df_keep.csv")

# Set up the style for seaborn
sns.set(style="whitegrid")

# 1. Histogram of each numerical feature
def plot_histograms(df):
    df.hist(bins=20, figsize=(20, 15), edgecolor='black')
    plt.suptitle('Distribution of Numerical Features', fontsize=16)
    plt.show()

# 2. Boxplot for each numerical feature (to detect outliers)
def plot_boxplots(df):
    fig, axes = plt.subplots(len(df.columns)//3, 3, figsize=(20, 15))
    fig.suptitle('Boxplots of Numerical Features', fontsize=16)
    for i, column in enumerate(df.columns):
        sns.boxplot(data=df, x=column, ax=axes[i//3, i%3])
        axes[i//3, i%3].set_title(column)
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()

# 3. Correlation heatmap
def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap of Numerical Features')
    plt.show()

# Filter out only the numerical columns for visualization
numerical_columns = [
    'nutriscore_score', 'nova_group', 'energy-kcal_100g', 'fat_100g', 
    'saturated-fat_100g', 'monounsaturated-fat_100g', 'polyunsaturated-fat_100g',
    'trans-fat_100g', 'cholesterol_100g', 'carbohydrates_100g', 
    'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 
    'sodium_100g', 'vitamin-a_100g', 'vitamin-c_100g', 
    'potassium_100g', 'calcium_100g', 'iron_100g'
]

df_numerical = df_keep[numerical_columns]

# Show histograms of all numerical columns
plot_histograms(df_numerical)

# Show boxplots of all numerical columns
plot_boxplots(df_numerical)

# Show correlation heatmap
plot_correlation_heatmap(df_numerical)
