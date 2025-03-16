import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
from datetime import datetime

# Sample Trade Data
trade_data = [
    (1, "EUR/USD", 100000, 1.085, "2025-03-13T12:00:00"),
    (2, "EUR/USD", 100050, 1.085, "2025-03-13T12:01:00"),
    (3, "EUR/USD", 1000, 1.0235, "2025-03-13T12:02:00"),
    (4, "EUR/USD", 100000000, 1.0235, "2025-03-13T12:03:00"),
    (5, "EUR/USD", 100000000, 1.0235, "2025-03-13T12:04:00"),
    (6, "EUR/USD", 95000, 1.086, "2025-03-13T12:05:00"),
    (7, "EUR/USD", 102000, 1.087, "2025-03-13T12:06:00"),
    (8, "EUR/USD", 101500, 1.084, "2025-03-13T12:07:00"),
    (9, "EUR/USD", 105000, 1.120, "2025-03-13T12:08:00"),
    (10, "EUR/USD", 99000, 1.083, "2025-03-13T12:09:00"),
    (11, "EUR/USD", 50000, 1.045, "2025-03-13T12:10:00"),
    (12, "EUR/USD", 1000000, 1.090, "2025-03-13T12:11:00"),
    (1001, "EUR/USD", 100000000.0, 1.1250, "2024-03-13T14:30:00"),
]

# Convert to DataFrame
df = pd.DataFrame(trade_data, columns=["trade_id", "currency_pair", "volume", "price", "timestamp"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Streamlit UI
st.title("Forex Trade Outlier Detection 📊")

st.write("This app analyzes FX trades and detects outliers using **Z-score**.")

# Outlier Detection (Z-score)
df["volume_zscore"] = zscore(df["volume"])
df["price_zscore"] = zscore(df["price"])


outliers = df[(df["volume_zscore"].abs() > 1) | (df["price_zscore"].abs() > 2.5)]

# Display data
st.subheader("Trade Data")
st.write(df)

st.subheader("Outliers Detected")
st.write(outliers)

# Visualization
st.subheader("Trade Volume Outliers")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["timestamp"], df["volume"], label="Normal Trades", color="blue")
ax.scatter(outliers["timestamp"], outliers["volume"], label="Outliers", color="red", marker="x")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Trade Volume")
ax.set_title("Trade Volume Outlier Detection")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)
