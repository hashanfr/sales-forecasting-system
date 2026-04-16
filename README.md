# Time-Series Sales Forecasting System

A dynamic time-series forecasting application that predicts future sales using historical data and trend analysis. The system allows users to upload custom datasets, automatically preprocess data, and generate forecasts with interactive visualizations.

## Overview

This project implements a complete forecasting pipeline using Prophet, enabling businesses to analyze historical sales patterns and make informed decisions. The application is built with Streamlit to provide an interactive interface for data exploration and forecasting.

## Features

- Upload and analyze any CSV dataset
- Dynamic selection of date and target columns
- Automatic data preprocessing and aggregation
- Time-series forecasting using Prophet
- Visualization of actual vs predicted values
- Trend and seasonality decomposition
- Forecast insights including growth trends
- Interactive dashboard interface

## Tech Stack

- Python
- Pandas
- NumPy
- Prophet
- Streamlit
- Matplotlib

## Project Structure


sales-forecasting-system/
│
├── app/
│ └── app.py
│
├── data/
│ └── sample_data.csv
│
├── requirements.txt
├── README.md
└── .gitignore


## Installation

Clone the repository:

```bash
git clone https://github.com/hashanfr/sales-forecasting-system.git
cd sales-forecasting-system

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app/app.py
Usage
Upload a CSV file containing time-series data
Select the date column and target variable
Adjust the forecast horizon using the sidebar
View forecast results, trends, and insights
Input Requirements
A valid date column (any format convertible to datetime)
A numeric column representing the target variable (e.g., sales, revenue)
Methodology
Data cleaning and preprocessing using Pandas
Time-series aggregation by date
Forecasting using Prophet with built-in trend and seasonality modeling
Visualization of predictions and components
Results

The model captures key patterns such as trend and seasonality and generates future forecasts. It also provides insights into expected growth or decline in the next period.

Future Improvements
Incorporate additional regressors (temperature, fuel price, holidays)
Multi-store and multi-category forecasting
Model evaluation metrics (MAE, RMSE, MAPE)
Deployment using cloud platforms
Integration with Power BI dashboards
Use Cases
Sales forecasting
Demand planning
Inventory optimization
Business trend analysis
License

This project is open-source and available for educational and research purposes.
