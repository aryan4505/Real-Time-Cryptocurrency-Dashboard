import pandas as pd

def calculate_kpis(df):
    total_market_cap= df['market_cap'].sum()
    average_price= df['current_price'].mean()
    highest_crypto=df.loc[df['current_price'].idxmax(), 'name']
    return total_market_cap, average_price, highest_crypto



