import config
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, config.API_URL)

barsets = api.get_bars(['AAPL', 'MSFT'], TimeFrame.Hour)
print(barsets)