import pandas as pd
import os
import streamlit as st

@st.cache_data(show_spinner=False)
def load_clean_data(country: str) -> pd.DataFrame:
    """
    Load and preprocess cleaned solar data for the given country.

    Args:
        country: one of 'benin', 'sierra leone', 'togo'

    Returns:
        DataFrame with lowercase columns and parsed timestamp.
    """
    # build file path
    path = os.path.join('data', 'clean', f"{country}_clean.csv")
    df = pd.read_csv(path)

    # normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # parse timestamp column
    # find any column containing 'time'
    time_col = next((c for c in df.columns if 'time' in c), None)
    if time_col is None:
        raise KeyError(f"no timestamp column found in {country} data")
    df['timestamp'] = pd.to_datetime(df[time_col])
    
    # ensure index sorted
    df = df.sort_values('timestamp')
    return df