import streamlit as st
import pandas as pd
import plotly.express as px


from api import fetch_crypto_data
from analysis import calculate_kpis


st.set_page_config(
    page_title="Real-Time Crypto Dashboard",
    layout="wide"
)

st.title("📊 Real-Time Cryptocurrency Dashboard")

df = fetch_crypto_data()

# KPIs
total_market_cap, average_price, highest_crypto = calculate_kpis(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Market Cap", f"${total_market_cap:,.0f}")

col2.metric("Average Price", f"${average_price:,.2f}")

col3.metric("Highest Crypto", highest_crypto)

# Table
st.subheader("Live Cryptocurrency Data")

st.dataframe(df)

# Bar Chart
fig = px.bar(
    df,
    x='name',
    y='current_price',
    title='Current Price of Cryptocurrencies'
)

st.plotly_chart(fig, use_container_width=True)

# Line Chart
fig2 = px.line(
    df,
    x='name',
    y='market_cap',
    title='Market Cap Analysis'
)

st.plotly_chart(fig2, use_container_width=True)

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name='crypto_data.csv',
    mime='text/csv'
)

coin = st.selectbox(
    "Select Cryptocurrency",
    df['name']
)

filtered_df = df[df['name'] == coin]

st.dataframe(filtered_df)

try:
    df = fetch_crypto_data()

except Exception as e:
    st.error(f"Error Fetching Data: {e}")