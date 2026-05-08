import ccxt
import pandas as pd

exchange = ccxt.okx({
    "enableRateLimit": True,
})

def get_ohlcv(symbol="ETH/USDT", timeframe="1h", limit=200):
    data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    df = pd.DataFrame(data, columns=[
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ])

    return df
