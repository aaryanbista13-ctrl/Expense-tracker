# Expense Tracker V1

A command line expense tracker built with Python and Pandas.

## Features
- Add new expenses with name, amount and category
- Remove expenses by name
- View all expenses with total and category breakdown
- Data saves permanently to CSV so nothing is lost after closing

## Categories
- Food
- Travel
- Shopping

## How to run
pip install pandas
expense_tracker_v1.py

## What I learned
- Pandas DataFrames for storing and managing data
- Reading and writing CSV files
- Passing DataFrames between functions

- # Expense Tracker Pro(v2)

An upgraded command line expense tracker built with Python, Pandas and Matplotlib.

## New features added in v2
- Update existing expenses — change name, amount or category individually
- Three visual charts saved as PNG files
- Added Fitness as a new category
- Cleaner menu with exit option

## All features
- Add new expenses with name, amount and category
- Remove expenses by name
- View all expenses with total and category breakdown
- Update any field of an existing expense
- Show three charts — individual expense amounts, spending by category pie chart, total per category bar chart
- Data saves permanently to CSV

## Categories
- Food
- Travel
- Shopping
- Fitness

## Charts generated
- chart1_Expenses.png — bar chart of each expense amount
- chart2_category.png — pie chart of spending by category
- chart3_category.png — bar chart of total spent per category

## How to run
pip install pandas matplotlib
python expense_tracker_v2.py

## What I learned
- df.loc for updating specific rows in a DataFrame
- Matplotlib bar charts and pie charts
- Dictionary pattern for clean category mapping
- Building on existing code and adding new features
- Saving charts as PNG image files
- Data validation and error handling
- Duplicate expense checking
