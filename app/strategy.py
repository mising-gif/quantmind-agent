def generate_signal(df):
    latest = df.iloc[-1]

    signal = "HOLD"

    if latest["ema20"] > latest["ema50"] and latest["rsi"] < 70:
        signal = "LONG"

    if latest["ema20"] < latest["ema50"] and latest["rsi"] > 30:
        signal = "SHORT"

    return signal
