import pytest
from datetime import datetime
from algo_trading.models.candle import Candle


@pytest.fixture
def valid_candle_data():
    return {
        "symbol": "SPY",
        "timestamp": datetime(2026, 6, 3),
        "open": 756.201867,
        "high": 756.850160,
        "low": 751.633619,
        "close": 752.301880,
        "volume": 51402500,
    }

def test_valid_candle_creation(valid_candle_data):
    candle = Candle(**valid_candle_data)
    assert candle.symbol == "SPY"
    assert candle.close == 752.301880
    assert candle.volume == 51402500

def test_negative_volume(valid_candle_data):
    data = valid_candle_data.copy()
    data["volume"] = -3
    with pytest.raises(ValueError):
        Candle(**data)

def test_high_lower_than_low(valid_candle_data):
    data = valid_candle_data.copy()
    data["high"] = 300.850160
    with pytest.raises(ValueError):
        Candle(**data)

def test_open_outside_range(valid_candle_data):
    data = valid_candle_data.copy()
    data["open"] = 758.201867
    with pytest.raises(ValueError):
        Candle(**data)

def test_close_outside_range(valid_candle_data):
    data = valid_candle_data.copy()
    data["close"] = 700.301880
    with pytest.raises(ValueError):
        Candle(**data)