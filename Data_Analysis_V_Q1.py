# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV files
steam_data = pd.read_csv('steam_store_data_2024.csv')
sales_data = pd.read_csv('Video Games Sales.csv')

# Display datasets info
print("Steam Store Data:")
print(steam_data.info())
print("\nVideo Game Sales Data:")
print(sales_data.info())

# Merge Data on Genre (common column)
# Ensure the Genre column exists in both datasets
if 'Genre' in steam_data.columns and 'Genre' in sales_data.columns:
    # Add placeholder 'Genre' column in steam_data based on `description` (example)
    steam_data['Genre'] = steam_data['description'].apply(lambda x: "Unknown" if pd.isna(x) else "Other")

    # Merge data
    merged_data = pd.merge(steam_data, sales_data, how="inner", on="Genre")
    print("\nMerged Data Sample:")
    print(merged_data.head())

    # Bar Plot: Average Global Sales by Genre
    avg_sales_by_genre = merged_data.groupby('Genre')['Global'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=avg_sales_by_genre.index, y=avg_sales_by_genre.values, palette="viridis")
    plt.title("Average Global Sales by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average Sales (in millions)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Heatmap: Correlation Between Metrics
    correlation_data = merged_data[['Global', 'North America', 'Europe', 'Japan', 'Rest of World']]
    correlation_matrix = correlation_data.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Between Regional Sales")
    plt.show()

else:
    print("The 'Genre' column is missing from one of the datasets.")
