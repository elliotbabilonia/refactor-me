import pandas as pd

# Function to calculate and print summary statistics for a column
def print_summary_statistics(data, column_name):
    column = data[column_name]
    print(f"Summary statistics on {column_name}")
    print("Mean:", column.mean())
    print("Median:", column.median())
    print("Max:", column.max())
    print("Min:", column.min())
    print("Standard Dev:", column.std())
    print()

# Function to filter and calculate summary statistics for a specific season
def print_season_summary(data, season_name, column_name):
    season_data = data[data['Season'] == season_name]
    print_summary_statistics(season_data, column_name)

# Function to find the most popular payment method in a location
def find_most_popular_payment_method(data, location):
    location_data = data[data['Location'] == location]
    popular_method = location_data['Payment Method'].mode()
    if not popular_method.empty:
        print(f"Most popular payment method in {location}: {popular_method.iloc[0]}")
    else:
        print(f"No payment method data available for {location}")
    print()

# Read in the data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# Calculate and print summary statistics for Purchase Amount and Age columns
columns_to_analyze = ["Purchase Amount (USD)", "Age"]
for column in columns_to_analyze:
    print_summary_statistics(df, column)

# Print summary statistics for different seasons
seasons_to_analyze = ["Winter", "Summer", "Spring", "Fall"]
for season in seasons_to_analyze:
    print_season_summary(df, season, "Purchase Amount (USD)")

# Keeping the selected columns in the file
columns_to_keep = [
    "Customer ID",
    "Age",
    "Gender",
    "Item Purchased",
    "Category",
    "Purchase Amount (USD)",
    "Location",
    "Size",
    "Color",
    "Season",
    "Review Rating",
    "Subscription Status",
    "Shipping Type",
    "Promo Code Used",
    "Previous Purchases",
    "Payment Method",
    "Frequency of Purchases"
]
df = df[columns_to_keep]

# Finding the most popular payment method in New York
find_most_popular_payment_method(df, "New York")

# Inputting the updated data into the csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
