from algo_trading.strategy.moving_average import MovingAverageStrategy
from algo_trading.models.candle import Candle
from algo_trading.models.signal import Signal, SignalType

import pytest
from datetime import datetime

@pytest.fixture
def valid_candle_data():
    return {
        "symbol": "MSFT",
        "timestamp": datetime(2025, 3, 10),
        "open": 412.35,
        "high": 418.90,
        "low": 409.80,
        "close": 417.25,
        "volume": 28765432
        }

def test_not_enough_candles(valid_candle_data):
    base = valid_candle_data.copy()

    candles = [
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 411.25}),
        Candle(**{**base, "close": 412.16}),
        Candle(**{**base, "close": 414.34}),
        Candle(**{**base, "close": 418.63}),
    ]

    with pytest.raises(ValueError):
        MovingAverageStrategy(window=1000).generate_signal(candles)

def test_buy_signal(valid_candle_data):
    base = valid_candle_data.copy()

    candles = [
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 411.25}),
        Candle(**{**base, "close": 412.16}),
        Candle(**{**base, "close": 414.34}),
        Candle(**{**base, "close": 418.63}),
    ]
    signal = MovingAverageStrategy(window=5).generate_signal(candles)
    assert signal == Signal(signal=SignalType.BUY)

def test_sell_signal(valid_candle_data):
    base = valid_candle_data.copy()

    candles = [
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 418.25}),
        Candle(**{**base, "close": 412.16}),
        Candle(**{**base, "close": 414.34}),
        Candle(**{**base, "close": 409.9}),
    ]
    signal = MovingAverageStrategy(window=5).generate_signal(candles)
    assert signal == Signal(signal=SignalType.SELL)

def test_hold_signal(valid_candle_data):
    base = valid_candle_data.copy()

    candles = [
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 410.17}),
        Candle(**{**base, "close": 410.17}),
    ]
    signal = MovingAverageStrategy(window=5).generate_signal(candles)
    assert signal == Signal(signal=SignalType.HOLD)
