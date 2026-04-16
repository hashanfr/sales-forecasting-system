## Time-Series Sales Forecasting System

An AI-powered web application that predicts future sales using historical data and time-series analysis. The system allows users to upload datasets, automatically preprocess data, and generate accurate forecasts with actionable insights.

## Features
- Supports custom CSV dataset uploads  
- Dynamic selection of date and target columns  
- Automatic data cleaning and preprocessing  
- Time-series forecasting using Prophet  
- Identifies trends and seasonality patterns  
- Generates future predictions for configurable time horizons  
- Provides growth insights and performance indicators  
- Displays results through an interactive dashboard  

## Tech Stack
- Python  
- Streamlit  
- Pandas  
- NumPy  
- Prophet  
- Matplotlib  

## Project Structure
sales-forecasting-system/
│
├── app/
│   └── app.py  
├── data/
│   └── sample_data.csv  
├── requirements.txt  
├── README.md  
└── .gitignore  

## How to Run
git clone https://github.com/hashanfr/sales-forecasting-system.git  
cd sales-forecasting-system  
pip install -r requirements.txt  
streamlit run app/app.py  

## How It Works
- Upload a dataset (CSV)  
- Select date and target columns  
- Clean and preprocess data automatically  
- Aggregate time-series data  
- Train forecasting model using Prophet  
- Generate future predictions  

Displays:
- Forecast vs actual trends  
- Growth insights  
- Seasonality and trend components  
- Forecast data table  

## Output
- Predicted future sales values  
- Growth percentage insights  
- Trend and seasonality visualization  
- Forecast confidence intervals  

## Future Improvements
- Incorporate external factors (temperature, fuel price, holidays)  
- Add multi-store and category-level forecasting  
- Include model evaluation metrics (MAE, RMSE, MAPE)  
- Deploy as a live web application  
- Integrate with business intelligence tools  

## Author
Hashanthra K  
