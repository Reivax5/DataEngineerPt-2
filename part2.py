import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales_data = pd.read_csv('sales_data.csv')
customer_data = pd.read_csv('customer_data.csv')
product_data = pd.read_csv('product_data.csv')


def merge_data(sales_data, customer_data, product_data):
    merged_data = pd.merge(sales_data, customer_data, how='inner', on=['customer_id', 'region'])
    merged_data = pd.merge(merged_data, product_data, how='left', on='product_id')
    aggregated_data = merged_data.groupby('region').agg(Total_Sales=('amount', 'sum'), Average_Rating=('rating', 'mean')).reset_index()
    aggregated_data = aggregated_data.sort_values(by=['Total_Sales'], ascending=False)
    merged_data = pd.merge(merged_data, aggregated_data, how='inner', on='region')
    return merged_data


def advanced_filtering(merged_data):
    for col in merged_data.select_dtypes(include='number').columns:
        merged_data[col].fillna(merged_data[col].mean(), inplace=True)

    for col in merged_data.select_dtypes(include='object').columns:
        merged_data[col].fillna(merged_data[col].mode()[0], inplace=True)

    return merged_data


def visualize_outliers(merged_data):
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['amount'], merged_data['discount'])
    plt.title('Scatter Plot of Amount vs. Discount')
    plt.xlabel('Amount')
    plt.ylabel('Discount')
    plt.show()


def cap_outliers(merged_data):
    Q1 = merged_data['amount'].quantile(0.25)
    Q3 = merged_data['amount'].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    merged_data['amount'] = np.where(merged_data['amount'] < lower_limit, lower_limit, merged_data['amount'])
    merged_data['amount'] = np.where(merged_data['amount'] > upper_limit, upper_limit, merged_data['amount'])
    return merged_data


# Step 1: Merge the three datasets
merged_data = merge_data(sales_data, customer_data, product_data)

# Step 2: Advanced filtering
merged_data = advanced_filtering(merged_data)
visualize_outliers(merged_data)
merged_data = cap_outliers(merged_data)
visualize_outliers(merged_data)


# Step 3: Analyze data
# Scenario 1: Sales Department - New Customer Growth Analysis

merged_data['date'] = pd.to_datetime(merged_data['date'])
merged_data['month_year'] = merged_data['date'].dt.to_period('M')
first_purchase = merged_data.groupby('customer_id')['month_year'].min().reset_index()
new_customers_per_month = first_purchase.groupby('month_year').count()

new_customers_per_month['growth_rate'] = new_customers_per_month['customer_id'].pct_change()

new_customers_per_month.to_csv('new_customers_per_month.csv')

# Converting Period to string
new_customers_per_month.reset_index(inplace=True)
new_customers_per_month['month_year'] = new_customers_per_month['month_year'].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(data=new_customers_per_month, x='month_year', y='customer_id')
plt.title('New Customers Growth Over Time')
plt.xlabel('Month and Year')
plt.ylabel('Number of New Customers')
plt.xticks(rotation=45)
plt.show()

# Scenario 2: Marketing Team - High-Value Product Analysis

top_products = merged_data.groupby('product_id').agg(Total_Revenue=('amount', 'sum')).nlargest(10, 'Total_Revenue')

total_revenue = merged_data['amount'].sum()
top_products['percent_contribution'] = (top_products['Total_Revenue'] / total_revenue) * 100

top_products.to_csv('top_products.csv')

top_products.plot(kind='bar', y='percent_contribution', legend=False)
plt.title('Top 10 Products by Revenue Contribution')
plt.xlabel('Product ID')
plt.ylabel('Percentage Contribution to Total Revenue')
plt.show()

# Scenario 3: Customer Support - Identifying High-Interaction Customers

threshold = 3

high_interaction_customers = merged_data.groupby('customer_id').agg(Transaction_Count=('transaction_id', 'count'))
high_interaction_customers = high_interaction_customers[high_interaction_customers['Transaction_Count'] > threshold]

high_interaction_customers = high_interaction_customers.merge(merged_data.groupby('customer_id').agg(Total_Spending=('amount', 'sum')), on='customer_id')

high_interaction_customers.to_csv('high_interaction_customers.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=high_interaction_customers, x='Transaction_Count', y='Total_Spending')
plt.title('High Interaction Customers: Transaction Count vs Total Spending')
plt.xlabel('Transaction Count')
plt.ylabel('Total Spending')
plt.show()

# Scenario 4: Inventory Management - Seasonal Sales Analysis

merged_data['season'] = merged_data['date'].dt.month // 3 + 1
merged_data['season'] = merged_data['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
seasonal_sales = merged_data.groupby(['product_id', 'season']).agg(Seasonal_Sales=('amount', 'sum')).reset_index()

seasonal_sales['rank'] = seasonal_sales.groupby('product_id')['Seasonal_Sales'].rank("dense", ascending=False)
top_season_per_product = seasonal_sales[seasonal_sales['rank'] == 1]

top_season_per_product.to_csv('top_season_per_product.csv')

plt.figure(figsize=(12, 6))
sns.barplot(data=seasonal_sales, x='product_id', y='Seasonal_Sales', hue='season')
plt.title('Seasonal Sales by Product')
plt.xlabel('Product ID')
plt.ylabel('Seasonal Sales')
plt.legend(title='Season')
plt.show()
