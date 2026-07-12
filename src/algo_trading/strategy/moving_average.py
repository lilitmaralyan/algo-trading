from algo_trading.models.candle import Candle
from algo_trading.strategy.base import Strategy
from algo_trading.models.signal import Signal, SignalType

import pandas as pd


class MovingAverageStrategy(Strategy):
    def __init__(self, window: int):
        self.window = window

    def generate_signal(
        self,
        candles: list[Candle],
    ) -> Signal:
        closes = [candle.close for candle in candles]
        closes = pd.Series(closes)
        if self.window <= len(closes):
            moving_average = closes.rolling(window=self.window).mean().iloc[-1]
            last_close = closes.iloc[-1]
            if last_close > moving_average:
                return Signal(signal=SignalType.BUY)
            elif last_close < moving_average:
                return Signal(signal=SignalType.SELL)
            else:
                return Signal(signal=SignalType.HOLD)
        else:
            raise ValueError(
                f"Not enough candles. Expected at least {self.window}, got {len(closes)}."
            )
        