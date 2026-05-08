from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_market(df, symbol="ETH"):
    latest = df.iloc[-1]

    prompt = f'''
你是专业加密货币量化分析师。

币种: {symbol}

价格: {latest['close']}
RSI: {latest['rsi']}
MACD: {latest['macd']}
EMA20: {latest['ema20']}
EMA50: {latest['ema50']}

请输出：
1. 当前趋势
2. 做多还是做空
3. 风险等级
4. 止损建议
'''

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
