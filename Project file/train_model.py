import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "Data" / "T1.csv")

df.rename(columns={
    "Date/Time": "Time",
    "LV ActivePower (kW)": "ActivePower",
    "Wind Speed (m/s)": "WindSpeed",
    "Theoretical_Power_Curve (KWh)": "TheoreticalPower"
}, inplace=True)

df.drop(
    ["Wind Direction (°)", "Time"],
    axis=1,
    inplace=True
)

df.dropna(inplace=True)

X = df[["TheoreticalPower", "WindSpeed"]]
y = df["ActivePower"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(
    y_test,
    y_pred
) ** 0.5)

Path("models").mkdir(exist_ok=True)

joblib.dump(
    model,
    "models/power_prediction.pkl"
)

print("Model Saved Successfully")
