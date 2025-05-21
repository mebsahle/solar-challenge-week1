import streamlit as st
import pandas as pd
from utils import load_clean_data

# page configuration
st.set_page_config(
    page_title="Solar Data Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# header
st.title("🌞 Solar Data Discovery Dashboard")

# sidebar filters
country = st.sidebar.selectbox(
    "Select Country", ["Benin", "SierraLeone", "Togo"]
)
metric = st.sidebar.selectbox(
    "Select Metric", ["ghi", "dni", "dhi"]
)
# date range input
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [pd.to_datetime("2022-01-01"), pd.to_datetime("2022-12-31")]
)

# load and filter data
df = load_clean_data(country.lower())
mask = (df['timestamp'] >= pd.to_datetime(start_date)) & (df['timestamp'] <= pd.to_datetime(end_date))
df_filtered = df.loc[mask]

# layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Time Series of {metric.upper()}")
    ts = df_filtered.set_index('timestamp')[metric]
    st.line_chart(ts)

with col2:
    st.subheader(f"Distribution of {metric.upper()}")
    hist = df_filtered[metric].dropna()
    st.bar_chart(hist.value_counts().sort_index())

# summary stats
st.subheader("Summary Statistics")
st.dataframe(df_filtered[metric].describe().to_frame().T)
# footer
st.markdown(
    """
    ---
    Made with ❤️ by [Meba](
    [GitHub](github.com/mebsahle) |
    [LinkedIn](linkedin.com/in/mebsahle))
    """
)
# This is a simple Streamlit app that allows users to explore solar data for different countries.
# Users can select a country and a metric (GHI, DNI, DHI) to visualize the time series and distribution of the selected metric.
# The app also provides summary statistics for the selected metric within the specified date range.
# The app is designed to be user-friendly and visually appealing, with a clean layout and interactive elements.
# The app is built using Streamlit, a popular framework for creating web applications in Python.