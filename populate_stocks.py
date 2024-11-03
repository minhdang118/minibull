import sqlite3, config

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

from alpaca.trading.enums import ( 
    AssetClass,
    AssetStatus, 
    AssetExchange, 
    OrderSide, 
    OrderType, 
    TimeInForce, 
    OrderClass, 
    QueryOrderStatus
)
from alpaca.common.exceptions import APIError

# Connect to the database
connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    SELECT symbol, name FROM stock
""")

rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]

# Search for stock assets
trading_client = TradingClient(config.API_KEY, config.SECRET_KEY)

search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY, exchange=AssetExchange.NYSE, status=AssetStatus.ACTIVE)

assets = trading_client.get_all_assets(search_params)

for asset in assets:
    try:
        if asset.symbol not in symbols and asset.status == 'active' and asset.tradable:
            print(f"Added a new stock: {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, name) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)

connection.commit()