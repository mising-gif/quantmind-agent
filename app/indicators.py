import pandas_ta as ta

def apply_indicators(df):
    df["rsi"] = ta.rsi(df["close"], length=14)

    macd = ta.macd(df["close"])
    df["macd"] = macd["MACD_12_26_9"]
    df["macd_signal"] = macd["MACDs_12_26_9"]

    bb = ta.bbands(df["close"])
    df["bb_upper"] = bb["BBU_5_2.0"]
    df["bb_lower"] = bb["BBL_5_2.0"]

    df["ema20"] = ta.ema(df["close"], length=20)
    df["ema50"] = ta.ema(df["close"], length=50)

    return df
