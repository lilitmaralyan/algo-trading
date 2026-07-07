from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Candle:
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self):
        self.volume >= 0
        self.high >= self.low
    