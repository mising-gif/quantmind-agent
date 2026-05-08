from fastapi import FastAPI

from app.exchange import get_ohlcv
from app.indicators import apply_indicators
from app.strategy import generate_signal

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/analyze")
def analyze(symbol: str = "ETH/USDT"):
    df = get_ohlcv(symbol)

    df = apply_indicators(df)

    signal = generate_signal(df)

    latest = df.iloc[-1]

    return {
        "symbol": symbol,
        "price": float(latest["close"]),
        "rsi": float(latest["rsi"]),
        "signal": signal
    }
