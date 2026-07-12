from algo_trading.models.candle import Candle

from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def generate_signal(
        self,
        candles: list[Candle]
    ): 
        pass