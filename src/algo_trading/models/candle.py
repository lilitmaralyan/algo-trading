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
        if self.volume < 0:
            raise ValueError("Volume must be non-negative.")

        if self.high < self.low:
            raise ValueError("High price cannot be lower than low price.")

        if not (self.low <= self.open <= self.high):
            raise ValueError("Open price must be between low and high.")

        if not (self.low <= self.close <= self.high):
            raise ValueError("Close price must be between low and high.")