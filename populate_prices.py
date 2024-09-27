import sqlite3, config

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

client = CryptoHistoricalDataClient()
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Day,
  start="2024-09-01",
  end="2024-09-07"
)

btc_bars = client.get_crypto_bars(request_params)
print(btc_bars.df)