from datetime import datetime, timedelta
import sqlite3, config
from zoneinfo import ZoneInfo

from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

# Connect to the database
connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    SELECT id, symbol, name FROM stock
""")
rows = cursor.fetchall()

symbols = [row['symbol'] for row in rows]

stock_historical_data_client = StockHistoricalDataClient(config.API_KEY, config.SECRET_KEY, url_override = None)
now = datetime.now(ZoneInfo("America/New_York"))

chunks = [symbols[i:i + 200] for i in range(0, len(symbols), 200)]

for chunk in chunks:
  request = StockBarsRequest(
      symbol_or_symbols=chunk,
      timeframe=TimeFrame(amount=1, unit=TimeFrameUnit.Day),
      start=now - timedelta(days=365),
      end=now - timedelta(days=1),
  )
  barsets = stock_historical_data_client.get_stock_bars(request)
  for symbol in barsets.data:
      print(f"Processing {symbol}")
      for bar in barsets.data[symbol]:
          cursor.execute("""
              INSERT INTO stock_price (stock_id, date, open, high, low, close, volume)
              VALUES (?, ?, ?, ?, ?, ?, ?)
          """, (rows[symbols.index(symbol)]['id'], bar.timestamp.date(), bar.open, bar.high, bar.low, bar.close, bar.volume))

connection.commit()