import matplotlib.pyplot as plt
import seaborn as sns

steam_data = pd.read_csv('steam_store_data_2024.csv')
sales_data = pd.read_csv('Video Games Sales.csv')

# Set a seaborn style for better visuals
sns.set(style="whitegrid")

# Visualize Steam Store Data - Column Distributions
print("\nVisualizing Steam Store Data Columns")
steam_data.hist(figsize=(15, 10), bins=30)
plt.suptitle("Steam Store Data Distributions", fontsize=16)
plt.show()

# Visualize Video Game Sales Data - Column Distributions
print("\nVisualizing Video Game Sales Data Columns")
sales_data.hist(figsize=(15, 10), bins=30)
plt.suptitle("Video Game Sales Data Distributions", fontsize=16)
plt.show()

# Example: Visualizing Genres in Video Game Sales Dataset
if 'Genre' in sales_data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Genre', data=sales_data, order=sales_data['Genre'].value_counts().index)
    plt.title("Distribution of Game Genres")
    plt.xlabel("Count")
    plt.ylabel("Genre")
    plt.show()
