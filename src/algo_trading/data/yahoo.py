from algo_trading.models.candle import Candle

from typing import Literal, List
from datetime import datetime
import yfinance as yf

def get_historical_data(
        symbol: str,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"],
        start: datetime,
        end: datetime
) -> List[Candle]:
    data = yf.Ticker(symbol)
    history = data.history(start=start, end=end, interval=interval)
    candles = []
    for index, row in history.iterrows():
        candle = Candle(
            symbol=symbol,
            timestamp=index,
            open=float(row["Open"]),
            high=float(row["High"]),
            low=float(row["Low"]),
            close=float(row["Close"]),
            volume=float(row["Volume"]),
        )
        candles.append(candle)
    return candles