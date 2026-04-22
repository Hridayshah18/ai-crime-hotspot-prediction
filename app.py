import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Page config
st.set_page_config(page_title="Crime Hotspot Dashboard", layout="wide")

st.title("🚔 AI Crime Hotspot Prediction Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/Crimes_-_2020_to_Present_2026.csv")
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Latitude', 'Longitude', 'Date'])
    df['Hour'] = df['Date'].dt.hour
    df['Primary Type'] = df['Primary Type'].astype(str)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

crime_type = st.sidebar.multiselect(
    "Select Crime Type",
    options=df['Primary Type'].unique(),
    default=df['Primary Type'].unique()[:5]
)

hour_range = st.sidebar.slider(
    "Select Hour Range",
    0, 23, (0, 23)
)

# Apply filters
filtered_df = df[
    (df['Primary Type'].isin(crime_type)) &
    (df['Hour'] >= hour_range[0]) &
    (df['Hour'] <= hour_range[1])
]

# Layout
col1, col2 = st.columns([2, 1])

# MAP SECTION
with col1:
    st.subheader("📍 Crime Heatmap")

    m = folium.Map(location=[41.8781, -87.6298], zoom_start=10)

    heat_data = filtered_df[['Latitude', 'Longitude']].values.tolist()
    HeatMap(heat_data).add_to(m)

    st_folium(m, width=700, height=500)

# CHART SECTION
with col2:
    st.subheader("📊 Crimes by Hour")

    hour_counts = filtered_df['Hour'].value_counts().sort_index()
    st.bar_chart(hour_counts)

# METRICS
st.subheader("📌 Key Insights")

col3, col4, col5 = st.columns(3)

col3.metric("Total Crimes", len(filtered_df))
col4.metric("Unique Crime Types", filtered_df['Primary Type'].nunique())
col5.metric("Peak Hour", hour_counts.idxmax() if not hour_counts.empty else "N/A")

# TABLE
st.subheader("📄 Sample Data")
st.dataframe(filtered_df.head(100))