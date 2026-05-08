import time
import schedule

from app.exchange import get_ohlcv
from app.indicators import apply_indicators
from app.strategy import generate_signal
from app.ai_engine import analyze_market
from app.notifier import send_telegram
from app.utils import now_time

def run_agent(symbol="ETH/USDT"):
    try:
        df = get_ohlcv(symbol=symbol)

        df = apply_indicators(df)

        signal = generate_signal(df)

        ai_result = analyze_market(df, symbol=symbol)

        latest = df.iloc[-1]

        message = f'''
AI QUANT AGENT

时间: {now_time()}
币种: {symbol}
价格: {latest['close']}
信号: {signal}
RSI: {round(latest['rsi'], 2)}

AI分析:
{ai_result}
'''

        print(message)

        send_telegram(message)

    except Exception as e:
        print("ERROR:", e)

schedule.every(10).minutes.do(run_agent, symbol="ETH/USDT")
schedule.every(10).minutes.do(run_agent, symbol="BTC/USDT")

print("AI AGENT STARTED...")

while True:
    schedule.run_pending()
    time.sleep(1)
