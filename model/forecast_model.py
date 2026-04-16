import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error


def load_data(path):
    df = pd.read_csv(path)

    # Convert to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    df = df.groupby('Date')['Weekly_Sales'].sum().reset_index()

    df.rename(columns={'Date': 'ds', 'Weekly_Sales': 'y'}, inplace=True)

    return df


def train_model(df):
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )
    model.fit(df)
    return model


def make_forecast(model, periods=90):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


def evaluate_model(df, forecast):
    # Align last 100 points
    df_actual = df.tail(100)
    df_pred = forecast.tail(100)

    mae = mean_absolute_error(df_actual['y'], df_pred['yhat'])
    return mae


if __name__ == "__main__":
    df = load_data("data/sales.csv")

    model = train_model(df)
    forecast = make_forecast(model, periods=90)

    mae = evaluate_model(df, forecast)

    print("Model Evaluation:")
    print(f"MAE: {mae:.2f}")