import pandas as pd  # Library for data manipulation

# Load the CSV files
steam_data = pd.read_csv('steam_store_data_2024.csv')
sales_data = pd.read_csv('Video Games Sales.csv')

# Display basic information about the datasets
print("Steam Store Data Info:")
print(steam_data.info())  # Overview of columns, data types, and non-null values

print("\nSteam Store Data Sample:")
print(steam_data.head())  # View the first 5 rows

print("\nVideo Game Sales Data Info:")
print(sales_data.info())  # Overview of columns, data types, and non-null values

print("\nVideo Game Sales Data Sample:")
print(sales_data.head())  # View the first 5 rows

# Check for missing values in both datasets
print("\nMissing Values in Steam Store Data:")
print(steam_data.isnull().sum())

print("\nMissing Values in Video Game Sales Data:")
print(sales_data.isnull().sum())
