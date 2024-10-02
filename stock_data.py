from datetime import datetime, timedelta
import sqlite3, config
from zoneinfo import ZoneInfo

from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

symbols = ['AAPL']

stock_historical_data_client = StockHistoricalDataClient(config.API_KEY, config.SECRET_KEY, url_override = None)

now = datetime.now(ZoneInfo("America/New_York"))
request = StockBarsRequest(
    symbol_or_symbols=symbols,
    timeframe=TimeFrame(amount=1, unit=TimeFrameUnit.Hour),
    start=now - timedelta(days=5),
    limit=1000
)

barsets = stock_historical_data_client.get_stock_bars(request)

for symbol in barsets.data:
    print(symbol)
    for bar in barsets.data[symbol]:
        print(f"Timestamp: {bar.timestamp}, Open: {bar.open}, High: {bar.high}, Low: {bar.low}, Close: {bar.close}, Volume: {bar.volume}")