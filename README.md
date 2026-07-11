# algo-trading
Personal algorithmic trading project for research, backtesting, and automated execution.

## Overview

`algo-trading` is a Python framework for building, testing, and running algorithmic trading strategies.

The project is designed around a modular architecture where each component has a single responsibility:

- **Data Layer** — retrieves and normalizes historical and live market data from different providers.
- **Domain Models** — represents financial objects such as candles, orders, trades, and positions.
- **Strategy Layer** — generates trading signals independently of the data source or broker.
- **Backtesting Engine** — simulates strategy execution on historical market data.
- **Performance Analysis** — evaluates strategies using trading and risk metrics.
- **Broker Layer** — executes orders in paper-trading and live-trading environments.

The long-term goal is to provide a reusable trading framework where strategies, data providers, and brokers can be exchanged independently without changing the rest of the system.
