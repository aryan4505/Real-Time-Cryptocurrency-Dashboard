import pandas as pd
import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False,
    }

    response = requests.get(url, params=params)

    data = response.json()
    df = pd.DataFrame(data)
    return df