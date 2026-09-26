import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame


stock_client = StockHistoricalDataClient("PK2LK3MT3JML5FUC6KIVGSU447", "2UdawYXSW8VW1n77qXCbqRZ5fNHM61yz4xzQzi6HJMNN")


stock_bar_request = StockBarsRequest(
    symbol_or_symbols="AAPL",
    timeframe=TimeFrame.Day,
    start="2023-01-01",
    end="2023-12-31"
)

bars = stock_client.get_stock_bars(stock_bar_request)
print(bars.df)  # .df gives you a clean pandas DataFrame