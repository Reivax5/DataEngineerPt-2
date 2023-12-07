# Data Engineering Part-1

---

## Introduction

Following the first part of this workshop, we will be continuing our journey in the world of data engineering.
With the previous workshop, you have learned how to create a dataframe from a csv, clean the data, and transform it.
Here you will learn some more complex data engineering concepts such as merging datasets, complex cleaning, data analysis, data visualization and data loading.


## 1. Merge Datasets

---

In this first step, we will be merging three new datasets.
The idea behind this is that in a company, a data engineer will have to get data from different sources
and merge them into one dataset to make the different manipulations on it.
Here, I will not give you any steps to follow, I will just give you the expected columns of the final datasets.
To know more about merging datasets,
go check the pandas documentation on [merging](https://pandas.pydata.org/docs/user_guide/merging.html).

The expected columns of the final dataset are:

- transaction_id
- customer_id
- product_id
- date
- amount
- payment_method
- transaction_status
- shipping_cost
- discount
- tax
- total_amount
- region
- name
- age
- gender
- country
- membership
- email
- phone
- product_name
- category
- price
- rating
- supplier
- stock_quantity
- release_date

Once you have this final dataset, you will have to add two new ones.

The first one is a column called "Total_Sales" that corresponds to the total amount of sales for each region.

The second one is a column called "Average_Rating" that corresponds to the average rating of the products in the regions.

Of course, sort the Total_Sales column in descending order.

## 2. Complex Cleaning

---

In this second step, we will be more complex cleaning than in the first part.
In a company, there are some scenarios that the data engineer will have to deal with.
The first one will be to handle null data.
This time we will not just drop the rows with null data.
We will replace them with the mean of the column if it is a numerical column
and with the mode of the column if it is a categorical column.

The second scenario is to handle outliers.
Outliers are data that are far from the means of the column which might be errors.
First of all, we need to identify the outliers.
For that, you will use the matplotlib library to plot a scatter plot of the Amount column as the xlabel and the Discount column as the ylabel.
Once this is done, you will be able to see that some prices are way bigger than the others. You will have to handle these amounts.

To handle outliers, we will use the [IQR](https://en.wikipedia.org/wiki/Interquartile_range) method.
You will cap the data that are bigger than the upper bound and smaller than the lower bound.
Like this, the outliers will be limited to the upper and lower bounds.

Once you have capped the outliers, you can reuse the plot you have done before to check if they have been handled correctly.

## 3. Data Analysis

---
The fourth step in a data pipeline is data analysis.
The data can be analyzed by using the pandas library to perform operations on the dataset.
This is also an important part because the analysis allows you to get some numbers and results on the dataset.
Now it is your turn to analyze the dataset, for this, we will simulate some real-life scenarios as a data engineer in a company.

### Scenario 1: Sales Department - New Customer Growth Analysis

**Company Request:** The sales department wants to understand the growth in new customer acquisition month-over-month.

**Query:** Extract the number of new customers each month.

**Analysis:** Calculate the month-over-month growth rate in new customer acquisition.


### Scenario 2: Marketing Team - High-Value Product Analysis

**Company Request:** The marketing team wants to know which products generate the most revenue and their respective contribution to total sales.

**Query:** Extract the top 10 revenue-generating products.

**Analysis:** Calculate the percentage contribution of each top product to total sales.

### Scenario 3: Customer Support - Identifying High-Interaction Customers

**Business Request:** Customer support wants to identify customers who have made a high number of transactions, indicating high interaction or potential issues.

**Query:** Extract the best customers that have the highest number of transactions with their total transactions and their total spending.

### Scenario 4: Operations Team - Inventory Planning Based on Seasonality

**Business Request:** The operations team needs to plan inventory based on seasonal purchase patterns.

**Query:** Extract product sales across different seasons. (Seasons: Spring, Summer, Fall, Winter)

**Analysis:** Determine which season has the highest sales for each product.


## 4. Data Visualization

---

The fifth step in a data pipeline is data visualization.
The data can be visualized by using the matplotlib library to plot graphs and charts.
This is also an important part because the visualization allows you to get some graphs and charts on the dataset.
You will have to produce some graphs and charts to visualize the data you have just calculated in the previous step.

- First Scenario: Plot a line graph of the number of new customers each month.
- Second Scenario: Plot a bar chart of the top 10 revenue-generating products.
- Third Scenario: Plot a scatter plot of the high interaction customers (Transaction Count vs Total Spending)
- Fourth Scenario: Plot a bar chart of the product sales across different seasons.

# 6.Data Loading

---

The last step of this workshop, is of course to save the resulting dataset into storage space, of course depending on the
needs and what the company needs, the storage space can vary, it can be a database, a csv file, a data warehouse or even a data lake.
Here, as it is just a simple workshop, we will save the dataset into a local database using SQLite.
To do this, we will be using the pandas library, and the to_sql() function.
Make a function called load_data() that takes a dataframe and the database name as parameters and saves the dataframe into the database.
Don't forget to first connect to the database using the connect() function from the sqlite3 library.

Once you execute the python script, you should have a database file in the same directory as the python script.
Open it, you will have your resulting dataset in the database.


## Conclusion

---

Congratulations, you have finished the second part of this workshop.
You have learned how to analyze and visualize data, and how to save the resulting dataset into a database.
